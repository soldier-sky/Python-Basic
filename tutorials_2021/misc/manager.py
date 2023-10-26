
class Manager:

    base_price=5  #base price per dish is 5rs per dish
    def __init__(self,table, seat):
        self.table=table
        self.seat=seat
        self.entree=[]

    def place_order(self, table, seat, entree=[]):
        self.table=table
        self.seat=seat
        self.entree=entree


    def get_check_total(self):
        return len(self.entree)*Manager.base_price






