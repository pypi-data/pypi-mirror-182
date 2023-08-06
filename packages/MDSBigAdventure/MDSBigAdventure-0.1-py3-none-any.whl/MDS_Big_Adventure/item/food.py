class item():

    #initialize
    def __init__(self, name, hp, po, price, amount):
        self.__name = name
        self.__hp = hp
        self.__po = po
        self.__price = price
        self.__amount = amount

    #return health bonus of the item
    def gethp(self):
        return self.__hp

    #return power bonus of the item
    def getpo(self):
        return self.__po

    #return item price
    def getprice(self):
        return self.__price

    #add health to the player
    def addhealth(self, p):
        p.health += self.gethp()

    #add power to the player
    def addpower(self, p):
        p.power += self.getpo()  

    #return the item name
    def getname(self):
        return self.__name
    
    #return item amount
    def getamount(self):
        return self.__amount

    #set item amount
    def setamount(self, value):
        self.__amount = value

    #display item name and price
    def display(self):
        return "{}, price {}".format(self.getname(), self.getprice())

