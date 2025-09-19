class SystemeNotes:
    """
    Système de notes : L'objectif est de traiter les notes dans l'ordre de leur ajout.

    FIXME: Mal implémenté avec une liste qui grandit indéfiniment!
    Il existe dans la bibliothèque standard une structure de données plus appropriée.
    """
    def __init__(self):
        self._notes = []
        self._index_debut = 0
    
    def ajouter_note(self, note: str) -> None:
        """Ajoute une note au système"""
        self._notes.append(note)
    
    def nb_notes(self) -> int:
        """Retourne le nombre de notes actives"""
        return len(self._notes) - self._index_debut
    
    def obtenir_prochaine_note(self) -> str | None:
        """Retourne la plus ancienne note active"""
        if self.nb_notes() == 0:
            return None
        note = self._notes[self._index_debut]
        self._index_debut += 1
        return note