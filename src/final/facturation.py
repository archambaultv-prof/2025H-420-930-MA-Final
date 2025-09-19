from final.taches import TacheSimple, Projet

class CalculateurFacturation:

    # FIXME: La signature de la fonction est confuse, soit un projet avec
    # plusieurs tâches, soit une seule tâche simple. Ceci ne devrait pas être
    # nécessaire si le patron Composite était utilisé.

    # FIXME: Cette signature ne permet pas des projets composés de sous-projets
    # et tâches. Ceci ne devrait pas être nécessaire si le patron Composite
    # était utilisé.
    def afficher_facturation(self, projet: Projet | None, taches: TacheSimple | list[TacheSimple]) -> None:
        """
        Affiche la facturation pour un projet avec ses tâches ou une tâche simple.
        """
        # FIXME: Ce test ne devrait pas être nécessaire si le patron Composite était utilisé.
        if projet:
            if not isinstance(taches, list):
                raise ValueError("Une liste de tâches doit être fournie si un projet est spécifié")
            nom_tache = projet.nom
        else:
            if not isinstance(taches, TacheSimple):
                raise ValueError("Une seule tâche doit être fournie si aucun projet n'est spécifié")
            nom_tache = taches.nom
        print(f"📊 Facturation pour {nom_tache}")

        temps_total = 0
        cout_total = 0.0
        # FIXME: Ce test ne devrait pas être nécessaire si le patron Composite était utilisé.
        if projet:
            temps_total += projet.temps_total()
            cout_total += projet.cout_total()
            for tache in taches: # type: ignore
                temps_total += tache.temps_total()
                cout_total += tache.cout_total()
        else:
            temps_total += taches.temps_total() # type: ignore
            cout_total += taches.cout_total() # type: ignore
        
        print(f"   ⏳ Nb heures: {temps_total:.2f} heures")
        print(f"   💰 Coût total: {cout_total:.2f}$")
