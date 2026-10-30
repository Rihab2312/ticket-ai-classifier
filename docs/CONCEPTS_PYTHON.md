# Les notions Python utilisées dans ce projet

Chaque notion est illustrée par du code **réel de ce projet**. Pour bien comprendre,
ouvre le fichier indiqué et lis le code en même temps.

## 1. Tuples et listes (`data.py`)

```python
("La facture est fausse", "facturation")   # un TUPLE : 2 valeurs figées
TRAINING_DATA = [ (...), (...), ... ]      # une LISTE de tuples
```

- **Liste** `[ ]` : ordonnée, modifiable.
- **Tuple** `( )` : ordonné, non modifiable. Pratique pour regrouper deux valeurs liées.

## 2. Dictionnaires (`model.py`, méthode `predict`)

```python
{"category": "facturation", "confidence": 0.575}
```

- Un dictionnaire associe une **clé** à une **valeur**.
- Lire : `result["category"]`. Lire sans erreur si la clé peut manquer : `result.get("category")`.
- Dans le test Odoo : une commande est un dictionnaire, ses lignes sont une liste de dictionnaires.

## 3. Compréhensions de liste (`model.py`, méthode `train`)

```python
texts  = [text  for text, _     in data]
labels = [label for _,    label in data]
```

Lecture : « pour chaque (texte, étiquette) dans data, garde le texte (ou l'étiquette) ».
C'est l'équivalent compact d'une boucle `for` qui fait `append`.
Le `_` signifie : « cette valeur ne m'intéresse pas ».

## 4. Classes et `self` (`model.py`)

```python
class TicketClassifier:
    def __init__(self):
        self.is_trained = False

    def train(self, data):
        ...
        self.is_trained = True
```

- Une **classe** est un plan de fabrication ; un **objet** est un exemplaire (`TicketClassifier()`).
- `__init__` est le constructeur : il prépare l'objet.
- `self` = l'objet lui-même. Sans `self.`, on ne retrouve pas ses attributs.
- `@classmethod` (méthode `load`) : une méthode qui s'appelle sur la classe (`TicketClassifier.load(...)`).

## 5. Exceptions (`model.py`, `api.py`)

```python
if not text:
    raise ValueError("Le texte du ticket est vide.")
...
try:
    result = classifier.predict(text)
except ValueError as exc:
    return jsonify({"error": str(exc)}), 400
```

- `raise` : signaler une erreur.
- `try / except ValueError` : réagir à une erreur **précise**.
- À éviter : `except:` tout seul, qui cache les vraies erreurs.

## 6. Annotations de type (`model.py`)

```python
def predict(self, text: str) -> dict[str, Any]:
```

Elles décrivent ce que la fonction reçoit et renvoie. Python ne les impose pas,
mais elles documentent le code et aident l'éditeur.

## 7. `if __name__ == "__main__":` (`__main__.py`, `api.py`)

Ce bloc ne s'exécute que si on lance le fichier directement. S'il est **importé**
(par un test, par exemple), il est ignoré.

## 8. Fonctions de fabrique (`api.py`)

`create_app()` fabrique l'application. Avantage : on peut en créer une pour chaque test,
avec un modèle différent. C'est un modèle de conception très utilisé avec Flask.

## 9. Tests avec pytest (`tests/`)

```python
def test_empty_text_raises(classifier):
    with pytest.raises(ValueError):
        classifier.predict("   ")
```

- Un test est une fonction dont le nom commence par `test_`.
- `assert` vérifie une condition.
- `@pytest.fixture` prépare un objet partagé. `@pytest.mark.parametrize` répète un test avec plusieurs jeux de données.

## 10. Environnement virtuel (`README.md`)

```bash
python -m venv .venv
source .venv/bin/activate
```

Il isole les bibliothèques du projet pour ne pas mélanger les versions entre projets.

## 11. L'IA derrière le code (`model.py`)

1. **TF-IDF** compte les mots d'un texte (en donnant plus de poids aux mots rares et utiles).
2. **La régression logistique** apprend, à partir des exemples, quels mots poussent vers quelle catégorie.
3. **`predict_proba`** donne une probabilité par catégorie. On prend la plus haute.

Plus on donne d'exemples variés, meilleur est le modèle. Un modèle ne « comprend » pas le texte :
il repère des régularités statistiques dans les mots.

## Pour aller plus loin

- Lis chaque test dans `tests/` et devine ce qu'il vérifie **avant** de lancer pytest.
- Casse volontairement le code (retire un `:` ou change un `==`) et observe l'erreur.
- Ajoute des `print()` dans `predict` pour voir les probabilités avant `max`.
