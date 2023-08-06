from .character import character

#inheritance from class character
class alien(character):

    #initialize
    def __init__(self, health, power, name, money):
        character.__init__(self, health, power)
        self.__name = name
        self.__money = money

    #return alien name    
    def getName(self):
        return self.__name

    #set alien name
    def setName(self, string):
        self.__name = string

    #change alien attributes when alien is dead
    def die(self):
        self.health = 0
        self.power = 0
        self.setName("alien dead body")
        self.__money = 0
        

    #return if the alien is dead
    def isdead(self):
        return self.health == 0

    #display
    def display(self):
        if self.isdead():
            return "(x__x) " + character.display(self)
        else:
            return "(╰_╯) " + character.display(self)

    #when alien is dead, drop the money
    def dropMoney(self):
        return self.__money
