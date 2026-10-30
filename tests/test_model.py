import pytest

from ticket_ai.data import TRAINING_DATA
from ticket_ai.model import TicketClassifier


@pytest.fixture(scope="module")
def classifier():
    """Une fixture prépare un objet réutilisable par plusieurs tests."""
    return TicketClassifier().train(TRAINING_DATA)


# Phrases NON présentes dans les données d'entraînement : le modèle doit généraliser.
UNSEEN_EXAMPLES = [
    ("La facture client affiche un mauvais montant de TVA", "facturation"),
    ("Mon colis n'est pas arrivé, quand sera-t-il livré", "livraison"),
    ("Je ne peux plus me connecter, mot de passe refusé", "acces"),
    ("Une erreur serveur s'affiche quand je clique sur enregistrer", "bug"),
]


@pytest.mark.parametrize("text, expected", UNSEEN_EXAMPLES)
def test_predicts_expected_category(classifier, text, expected):
    assert classifier.predict(text)["category"] == expected


def test_result_structure(classifier):
    result = classifier.predict("La facture est fausse")
    assert set(result) == {"category", "confidence", "needs_review", "scores"}
    assert 0.0 <= result["confidence"] <= 1.0
    assert abs(sum(result["scores"].values()) - 1.0) < 0.01


def test_empty_text_raises(classifier):
    with pytest.raises(ValueError):
        classifier.predict("   ")


def test_untrained_model_raises():
    with pytest.raises(RuntimeError):
        TicketClassifier().predict("bonjour")


def test_empty_training_data_raises():
    with pytest.raises(ValueError):
        TicketClassifier().train([])


def test_save_and_load(classifier, tmp_path):
    path = tmp_path / "model.joblib"
    classifier.save(path)
    loaded = TicketClassifier.load(path)
    text = "Le stock est faux"
    assert loaded.predict(text)["category"] == classifier.predict(text)["category"]
