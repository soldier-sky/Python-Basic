# Sample program to place order for food

class Manager:
    ''' This class takes seat and table as int and order as string 
    '''
    def __init__(self, table, seat, order):
        self.table = table
        self.seat = seat
        self.order = order

    def place_order(self):
        print("\nTable no.: ",self.table)
        print("\nSear no.: ", self.seat)
        print("\nOrder: ",self.order)

    def check_total(self):
        print("\n Total bill for {} is :".format(self.order), 10)


if __name__ == "__main__":
    m_obj=Manager(1,1,"chicken")
    m_obj.place_order()
    m_obj.check_total()
