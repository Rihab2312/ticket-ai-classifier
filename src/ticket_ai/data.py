"""Données d'entraînement.

Chaque exemple est un TUPLE : (texte du ticket, catégorie).
Une liste de tuples est une structure de données Python très courante.
Ces exemples sont fictifs et écrits à la main pour l'apprentissage.
"""

CATEGORIES = ["facturation", "livraison", "acces", "bug"]

TRAINING_DATA = [
    # --- facturation ---
    ("La facture du mois dernier contient une erreur de TVA", "facturation"),
    ("Je n'arrive pas à télécharger ma facture en PDF", "facturation"),
    ("Le montant de mon avoir est incorrect", "facturation"),
    ("Il manque une ligne sur la facture client", "facturation"),
    ("Mon paiement n'apparaît pas sur la facture", "facturation"),
    ("Pouvez-vous annuler la facture et en refaire une nouvelle", "facturation"),
    ("Le devis a été converti en facture avec le mauvais tarif", "facturation"),
    ("Je souhaite une facture d'acompte pour la commande", "facturation"),
    ("La date d'échéance de la facture est fausse", "facturation"),
    ("Le client conteste le montant facturé", "facturation"),
    ("La remise n'a pas été appliquée sur la facture", "facturation"),
    ("Où trouver la balance âgée des clients", "facturation"),
    # --- livraison / stock ---
    ("Ma commande n'est toujours pas livrée", "livraison"),
    ("Le colis est arrivé endommagé", "livraison"),
    ("Le bon de livraison ne se génère pas", "livraison"),
    ("Le stock affiché est différent du stock réel", "livraison"),
    ("Il manque un article dans la livraison", "livraison"),
    ("Je voudrais suivre mon colis", "livraison"),
    ("La réception du fournisseur n'a pas été enregistrée", "livraison"),
    ("Le transporteur n'est pas passé aujourd'hui", "livraison"),
    ("Quantité livrée incorrecte par rapport à la commande", "livraison"),
    ("Le produit est en rupture de stock", "livraison"),
    ("Je dois modifier l'adresse de livraison", "livraison"),
    ("L'entrepôt ne trouve pas l'emplacement du produit", "livraison"),
    # --- accès / droits ---
    ("Je n'arrive pas à me connecter à mon compte", "acces"),
    ("J'ai oublié mon mot de passe", "acces"),
    ("Je n'ai pas accès au menu des notes de frais", "acces"),
    ("Mon groupe d'utilisateurs ne voit pas les dépenses", "acces"),
    ("Merci d'ajouter les droits de validation à mon collègue", "acces"),
    ("L'accès est refusé quand j'ouvre les commandes", "acces"),
    ("Je veux créer un nouvel utilisateur pour le stagiaire", "acces"),
    ("L'authentification à deux facteurs ne fonctionne plus", "acces"),
    ("Mon compte est bloqué après plusieurs tentatives", "acces"),
    ("Je ne vois plus les opportunités de mon équipe", "acces"),
    ("Il faut retirer les droits d'un ancien employé", "acces"),
    ("Impossible de modifier un client, droits insuffisants", "acces"),
    # --- bug technique ---
    ("L'application plante quand je valide la commande", "bug"),
    ("Une erreur s'affiche lors de l'impression du rapport PDF", "bug"),
    ("La page reste blanche après le clic sur enregistrer", "bug"),
    ("Le calcul du total est faux après avoir ajouté une ligne", "bug"),
    ("Le système est très lent depuis la mise à jour", "bug"),
    ("Message d'erreur serveur 500 à l'ouverture de la liste", "bug"),
    ("Le bouton confirmer ne réagit pas", "bug"),
    ("Les données ne se sauvegardent pas dans le formulaire", "bug"),
    ("Le module de synchronisation renvoie une exception", "bug"),
    ("Le champ calculé affiche une valeur incorrecte", "bug"),
    ("L'export Excel génère un fichier vide", "bug"),
    ("Le planificateur ne lance plus la tâche automatique", "bug"),
]
