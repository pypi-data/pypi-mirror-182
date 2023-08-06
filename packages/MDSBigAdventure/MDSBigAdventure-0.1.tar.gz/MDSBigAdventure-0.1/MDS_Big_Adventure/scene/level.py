class level():
    __status = 0
    __locked = 1

    #initialize
    def __init__(self, location, lines, alien):
        self.__location = location
        self.__lines = lines
        self.__alien = alien

    #return location    
    def getLoc(self):
        return self.__location

    #set status to 1 if the level is visited
    def visit(self):
        self.__status = 1

    #return the status of current level
    def getStatus(self):
        return self.__status
    
    #check if current level is visited
    def isVisited(self):
        return self.__status == 0

    #return alien at the current level
    def getAlien(self):
        return self.__alien
    
    #return the lines based on level status
    def getplot(self):
        if self.isVisited():
            return self.__lines[0]
        else:
            return self.__lines[1]

    #unlock the level if alien is dead
    def unlock(self):
        if self.__alien.isdead():
            self.__locked = 0

    #check if the level is locked
    def islocked(self):
        return self.__locked == 1
