# ticket-ai-classifier

Petit projet : un **classifieur de tickets d'assistance** en Python.
Il lit le texte d'un ticket (« La facture contient une erreur de TVA ») et prédit sa
catégorie (`facturation`, `livraison`, `acces`, `bug`), avec un score de confiance.


## Ce que ce projet démontre

- Python propre : classes, dictionnaires, compréhensions, exceptions, typage
- Un modèle de **machine learning** simple (TF-IDF + régression logistique, scikit-learn)
- Une **API REST** avec Flask (`/health`, `/predict`)
- Des **tests automatisés** avec pytest (13 tests)
- **Docker** et **Git** : projet reproductible et versionné

## Installation

```bash
git clone <url-de-ton-depot>
cd ticket-ai-classifier

python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Utilisation

### En ligne de commande

```bash
PYTHONPATH=src python -m ticket_ai "Le total de la facture est faux"
```

Résultat (exemple) :

```json
{
  "category": "facturation",
  "confidence": 0.575,
  "needs_review": false,
  "scores": {"acces": 0.17, "bug": 0.15, "facturation": 0.575, "livraison": 0.1}
}
```

### En API

```bash
PYTHONPATH=src python -m ticket_ai.api
```

```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "Mon colis est en retard"}'
```

### Avec Docker

```bash
docker build -t ticket-ai .
docker run -p 5000:5000 ticket-ai
```

## Tests

```bash
python -m pytest -q
```

## Structure du projet

```
ticket-ai-classifier/
├── src/ticket_ai/
│   ├── data.py        # exemples d'entraînement (texte, catégorie)
│   ├── model.py       # classe TicketClassifier : train / predict / save / load
│   ├── api.py         # API Flask
│   └── __main__.py    # ligne de commande
├── tests/             # tests pytest
├── docs/CONCEPTS_PYTHON.md   # les notions Python utilisées, expliquées
├── Dockerfile
├── pyproject.toml
└── requirements.txt
```

## Limites connues (honnêtes)

- Le jeu de données est **petit** (48 exemples fictifs) : le modèle est un exercice,
  pas un outil de production.
- Le modèle **choisit toujours une catégorie**, même pour un texte sans rapport
  (« bonjour »). Le champ `needs_review` aide, mais ne suffit pas : voir l'exercice 4.
- Le serveur Flask de développement n'est pas prévu pour la production.

## Exercices pour progresser

1. **Ajouter une catégorie** (ex. `question_fonctionnelle`) avec 12 exemples, puis un test.
2. **Ajouter des exemples** et observer l'évolution du score de confiance.
3. **Mesurer la qualité** : séparer les données en entraînement et test
   (`sklearn.model_selection.train_test_split`) et afficher la précision.
4. **Gérer les textes hors sujet** : ajouter une catégorie `hors_sujet`, ou augmenter
   `MIN_CONFIDENCE`, et écrire un test.
5. **Ajouter une priorité** (`urgent` / `normal`) avec un second modèle.
6. **Appeler l'API depuis Odoo** : un petit module qui envoie le texte d'un ticket à
   `/predict` et remplit un champ « catégorie » (avec `requests`, gestion des erreurs et timeout).
7. **Remplacer le modèle** par un appel à un LLM via API, et comparer les résultats.
8. **Ajouter une intégration continue** (GitHub Actions) qui lance les tests à chaque push.

## Licence

Projet d'apprentissage, libre d'utilisation.
