"""API REST (Flask) pour utiliser le modèle depuis une autre application.

Exemple d'usage depuis un système externe (comme Odoo) :
    POST /predict   {"text": "La facture contient une erreur"}
"""

from __future__ import annotations

from flask import Flask, jsonify, request

from .data import TRAINING_DATA
from .model import TicketClassifier


def create_app(classifier: TicketClassifier | None = None) -> Flask:
    """Fabrique l'application (pattern « application factory »).

    On peut lui passer un modèle déjà prêt, ce qui facilite les tests.
    """
    app = Flask(__name__)

    if classifier is None:
        classifier = TicketClassifier().train(TRAINING_DATA)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.post("/predict")
    def predict():
        # silent=True : si le JSON est invalide, on obtient None au lieu d'une erreur.
        payload = request.get_json(silent=True) or {}
        text = payload.get("text", "")

        try:
            result = classifier.predict(text)
        except ValueError as exc:
            # 400 = requête invalide (la faute vient de l'appelant)
            return jsonify({"error": str(exc)}), 400

        return jsonify(result)

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
