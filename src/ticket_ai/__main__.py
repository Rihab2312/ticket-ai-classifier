"""Utilisation en ligne de commande :  python -m ticket_ai "texte du ticket" """

from __future__ import annotations

import argparse
import json

from .data import TRAINING_DATA
from .model import TicketClassifier


def main() -> None:
    parser = argparse.ArgumentParser(description="Classer un ticket d'assistance.")
    parser.add_argument("text", help="Le texte du ticket entre guillemets")
    args = parser.parse_args()

    classifier = TicketClassifier().train(TRAINING_DATA)
    result = classifier.predict(args.text)
    print(json.dumps(result, ensure_ascii=False, indent=2))


# Ce bloc ne s'exécute que si on lance le fichier directement.
if __name__ == "__main__":
    main()
