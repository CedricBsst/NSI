class Graphe:
    def __init__(self):
        listes_adjacences = {}
    
    def ajouter_sommet(self, sommet):
        if sommet not in self.listes_adjacences:
            self.listes_adjacences[sommet] = []
    
    def supprimer_sommet(self, sommet):
        if sommet in self.listes_adjacences:
            self.listes_adjacences.pop(sommet)
            for sommets in self.listes_adjacences:
                if sommet in self.listes_adjacences[sommets]:
                    self.listes_adjacences[sommets].remove(sommet)
    
    def ajouter_arete(self, s1, s2):
        if s1 in self.listes_adjacences and s2 in self.listes_adjacences:
            self.listes_adjacences[s1].append(s2)
            self.listes_adjacences[s2].append(s1)
    
    def supprimer_arete(self, s1, s2):
        if s1 in self.listes_adjacences and s2 in self.listes_adjacences:
            self.listes_adjacences[s1].remove(s2)
            self.listes_adjacences[s2].remove(s1)
    
    def afficher(self):
        for sommet in self.listes_adjacences:
            print(sommet, ":", self.listes_adjacences[sommet])
    
    def voisins(self, sommet):
        if sommet in self.listes_adjacences:
            return self.listes_adjacences[sommet]
        return []