from final.notes import SystemeNotes

class TacheSimple():
    def __init__(self, nom: str, priorite: str, heures: float):
        self.nom = nom
        self.priorite = priorite
        self.heures = heures
        self.notes = SystemeNotes() # Vous n'avez pas à modifier cette ligne pour utiliser l'injection de dépendances.
    
    def temps_total(self) -> float:
        """
        Retourne le temps total en heures pour cette tâche.
        """
        return self.heures
    
    def cout_total(self) -> float:
        """
        Retourne le coût total pour cette tâche en fonction de sa priorité.
        """
        # FIXME: Arbre if/elif -> code difficile à étendre pour une nouvelle priorité
        # ou un taux horaire personnalisé
        if self.priorite == "urgent":
            return self.heures * 75.0
        elif self.priorite == "élevé":
            return self.heures * 62.5
        elif self.priorite == "normale":
            return self.heures * 50.0
        else:
            raise ValueError("Priorité inconnue")

# FIXME: Cette classe n'implémente pas le patron Composite
class Projet():
    def __init__(self, nom: str, priorite: str, heures: float):
        self.nom = nom
        self.priorite = priorite
        self.heures = heures
        self.notes = SystemeNotes() # Vous n'avez pas à modifier cette ligne pour utiliser l'injection de dépendances.
    
    def temps_total(self) -> float:
        """
        Retourne le temps alloué à la gestion du projet, sans compter les sous-tâches.
        """
        return self.heures
    
    def cout_total(self) -> float:
        """
        Retourne le coût alloué à la gestion du projet, sans compter les sous-tâches.
        """
        # FIXME: Arbre if/elif -> code difficile à étendre pour une nouvelle priorité
        if self.priorite == "urgent":
            return self.heures * 85.0
        elif self.priorite == "élevé":
            return self.heures * 70.0
        elif self.priorite == "normale":
            return self.heures * 55.0
        else:
            raise ValueError("Priorité inconnue")
