class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print (self.name + "'s health is " + str(self.health))

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.name = name
        self.health = 150
    def _pet(self):
        self.health += 5   
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def _fly(self):
        self.health -= 10   
        return self
    def displayHealth(self):
        print (str(self.health) + " I am a Dragon.")

class Penguin(Animal):
    def __init__(self, name, health):
        super(Penguin, self).__init__(name, health)
    def displayHealth(self):
        print (str(self.health) + " I am a Penguin.")

a = Animal("Toby", 0).walk().walk().walk().run().run().displayHealth()
d = Dog("Patches", 0).walk().walk().walk().run().run()._pet().displayHealth()
dr = Dragon("Puff", 0)._fly().displayHealth()
p = Penguin("Chilly Willy", 0).displayHealth()
