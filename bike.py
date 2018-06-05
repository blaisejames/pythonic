class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "The price is $" + str(self.price)
        print "The maximum speed is " + self.max_speed
        print "The total miles are " + str(self.miles)
        # return self
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        if self.miles <= 0:
            self.miles = 0
        return self

bike1 = Bike(200, '25 mph').ride().ride().ride().displayinfo()
bike2 = Bike(200, '25 mph').ride().ride().reverse().reverse().displayinfo()
bike3 = Bike(200, '25 mph').reverse().reverse().reverse().displayinfo()