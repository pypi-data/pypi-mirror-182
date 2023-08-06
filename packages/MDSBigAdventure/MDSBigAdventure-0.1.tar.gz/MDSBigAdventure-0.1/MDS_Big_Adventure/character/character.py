class character():

    #initialize
    def __init__(self, health, power):
        self.health = health
        self.power = power

    #display health and power
    def display(self):
        return "Health: {} power: {}".format(self.health, self.power)

    #return the power value
    def fight(self):
        return self.power 

    #deduct health by the alien attack
    def wound(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
