
class AbstractOrder(object):
    species = None
    color = None
    imported = None
    shape = None
    seasons = []
    base_price = 5.00


    def __init__(self):
        print "Error. Don't make an AbstractOrder(). There are classes for specific melons."

    def get_price(self, qty):
        return self.base_price

class WatermelonOrder(AbstractOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def __init__(self):
        print "you made a watermelon order."

    def get_price(self, qty):
        total = super(WatermelonOrder, self).get_price(qty)
        if qty >= 3:
            total = total * .75

        return total

class CasabaOrder(AbstractOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def __init__(self):
        print "you made a casaba order."

    def get_price(self, qty):
        total = (super(CasabaOrder, self).get_price(qty) + 1) * 1.5

        return total

   
