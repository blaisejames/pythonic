class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        self.tax = 0.07

    def sell(self):
        self.status = 'sold'
        return self
    
    def add_tax(self):
        self.price = self.price * (1.0 + self.tax)
        return self
    
    def return_reason(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        if reason == 'unsealed':
            self.status = 'for sale'
        if reason == 'open box':
            self.status = 'used'
            self.price = self.price * .8
        return self
    
    def displayinfo(self):
        print "The item name is: " + self.item_name 
        print "The price is $" + str(self.price)
        print "The weight is " + str(self.weight) + " lbs"
        print "The brand is " + self.brand
        print "The item's status is: " + self.status + "\n"

product1 = Product(79, 'deck umbrella', 25, 'Canco').sell().add_tax().displayinfo()
product2 = Product(59, 'plant table', 15, 'Barca').return_reason('defective').displayinfo()
product3 = Product(39, 'weatherproof rug', 22, 'DeFacto').return_reason('unsealed').displayinfo()
product4 = Product(199, 'deck table', 150, 'Empire').return_reason('open box').displayinfo()