"""Le modèle d'IA : un classifieur de texte.

Principe (en 3 étapes) :
1. TF-IDF transforme chaque texte en nombres (l'ordinateur ne comprend que les nombres).
2. La régression logistique apprend, à partir des exemples, quels mots
   indiquent quelle catégorie.
3. Pour un nouveau texte, le modèle donne une probabilité par catégorie.

C'est du "machine learning supervisé" : on lui donne des exemples avec la bonne réponse.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# En dessous de ce score, on préfère demander une vérification humaine.
MIN_CONFIDENCE = 0.40


class TicketClassifier:
    """Une CLASSE regroupe des données (attributs) et des actions (méthodes).

    `self` désigne l'objet lui-même : c'est ainsi qu'une méthode accède
    à ses propres attributs (par exemple self.pipeline).
    """

    def __init__(self) -> None:
        # Un Pipeline enchaîne les étapes : texte -> nombres -> prédiction.
        self.pipeline = Pipeline(
            [
                ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
                ("clf", LogisticRegression(C=10.0, max_iter=1000)),
            ]
        )
        self.is_trained = False

    def train(self, data: list[tuple[str, str]]) -> "TicketClassifier":
        """Entraîne le modèle avec une liste de tuples (texte, catégorie)."""
        if not data:
            raise ValueError("Les données d'entraînement sont vides.")

        # Compréhensions de liste : on sépare les textes et les catégories.
        texts = [text for text, _ in data]
        labels = [label for _, label in data]

        self.pipeline.fit(texts, labels)
        self.is_trained = True
        return self  # permet d'écrire TicketClassifier().train(data)

    def predict(self, text: str) -> dict[str, Any]:
        """Prédit la catégorie d'un ticket et renvoie un DICTIONNAIRE."""
        if not self.is_trained:
            raise RuntimeError("Le modèle n'est pas entraîné.")

        text = (text or "").strip()
        if not text:
            raise ValueError("Le texte du ticket est vide.")

        probabilities = self.pipeline.predict_proba([text])[0]
        classes = self.pipeline.classes_

        # dict(zip(...)) associe chaque catégorie à sa probabilité.
        scores = {str(c): round(float(p), 3) for c, p in zip(classes, probabilities)}
        best = max(scores, key=scores.get)

        return {
            "category": best,
            "confidence": scores[best],
            "needs_review": scores[best] < MIN_CONFIDENCE,
            "scores": scores,
        }

    def save(self, path: str | Path) -> None:
        """Sauvegarde le modèle entraîné dans un fichier."""
        joblib.dump(self.pipeline, Path(path))

    @classmethod
    def load(cls, path: str | Path) -> "TicketClassifier":
        """Recharge un modèle sauvegardé (méthode de classe : pas besoin d'objet)."""
        instance = cls()
        instance.pipeline = joblib.load(Path(path))
        instance.is_trained = True
        return instance
