from final.facturation import CalculateurFacturation
from final.taches import TacheSimple, Projet

def main():
    """Démonstration du calculateur"""
    print("=" * 60)
    print(" DÉMONSTRATION SYSTÈME DE FACTURATION ")
    print("=" * 60)
    
    # Initialisation
    calculateur = CalculateurFacturation()
    
    # Création d'éléments de travail
    
    # FIXME : Aucune façon de spécifier un taux horaire personnalisé ou ajouter
    # une autre priorité. Voir le FIXME des méthodes cout_total des classes
    # TacheSimple et Projet qui est en lien avec ce problème.
    tache1 = TacheSimple("Développer API", "urgent", 12.5)
    tache2 = TacheSimple("Tests unitaires", "normale", 8.0)

    projet = Projet("Module Authentification", "urgent", 5.0)

    # Tests de facturation
    print("\nTest 1: Tâche simple")
    calculateur.afficher_facturation(projet=None, taches=tache1)

    print("\nTest 2: Projet")
    calculateur.afficher_facturation(projet=projet, taches=[tache1, tache2])

    # Tests du système de notes
    tache1.notes.ajouter_note("API doit être RESTful")
    tache1.notes.ajouter_note("Utiliser OAuth2 pour l'authentification")
    print("\nNotes pour la tâche 1:")
    while tache1.notes.nb_notes() > 0:
        note = tache1.notes.obtenir_prochaine_note()
        print(f" - {note}")

if __name__ == "__main__":
    main()