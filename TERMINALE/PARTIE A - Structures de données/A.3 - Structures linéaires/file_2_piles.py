from .pile_objets import Pile

class File:
    def __init__(self):
        self.pile1 = Pile()
        self.pile2 = Pile()
        self.derniere_action = "enfiler"

    def est_vide(self):
        if self.derniere_action == "enfiler":
            return self.pile1.est_vide()
        else:
            return self.pile2.est_vide()
        
    def enfiler(self, elt):
        if self.derniere_action == "defiler":
            while not self.pile2.est_vide():
                self.pile1.empiler(self.pile2.depiler())
        self.pile1.empiler(elt)
        self.derniere_action = "enfiler"
    
    def defiler(self, elt):
        assert not self.est_vide()
        if self.derniere_action == "enfiler":
            while not self.pile1.est_vide():
                self.pile2.empiler(self.pile1.depiler())
        self.derniere_action = "defiler"
        return self.pile2.defiler()