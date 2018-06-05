class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else: 
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: " + str(self.tax) + "\n"
        return self


car1 = Car(2000, '35 mph', 'Full', '15 mpg')
car2 = Car(2000, '5 mph', 'Not Full', '105 mpg')
car3 = Car(2000, '15 mph', 'Kind of Full', '95 mpg')
car4 = Car(2000, '25 mph', 'Full', '25 mpg')
car5 = Car(2000, '435 mph', 'Empty', '25 mpg')
car1 = Car(20000000, '35 mph', 'Empty', '15 mpg')