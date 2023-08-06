class sparkLance():

    #initialize
    def __init__(self, name, hp, po, status):
        self.__name = name
        self.__hp = hp
        self.__po = po
        self.__status = status

    #multiply the health value to the player
    def betaTransform(self, p):
        try:
            p.health = p.health*self.__hp
        except Exception as ex:
            print(ex)
            print("Something is wrong with the player")

    #multiply the power value to the player
    def getSpacium(self, p):
        try:
            p.power = p.power*self.__po
        except Exception as ex:
            print(ex)
            print("Something is wrong with the player")

    #get the plot when sparklance is activated
    def getplot(self):
        return ["""
                                          As soon as you touched the Spark Lance, it started glowing and immersed you in light.
                                          You were startled at first, but soon you felt something, something strange but familiar.
                                          It felt like those sunny afternoons, when you look out from the window, 
                                          everything is so quite under the clear blue sky, you feel peaceful. 
                                          It then felt like the times when you finished the very last exam of the term, you are relieved, and hope
                                          is coming back to you agian.
                                          After that, you felt courage, it was like recieving an quiz score better than you had hoped, you started to believe
                                          in yourself.

                                          Suddenly, You heard a voice in the light: 

                                          "The only way to save the world, is you become the light"

                                          Yes, I can be the light! You thought.

                                          You raised the Spark Lance high:

                                          Ultraman !!!!!!!!!!

                                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Exciting BGM playing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                          *********************************************Fancy visual effects *************************************************

                                          You transformed into Ultraman with the power of the light, you now have special powers to save the world.
                          """,
                """
                                           "It is you..." The Tim Hortons staff said slowly.
                                           "Many years ago an old lady came here and ordered turkey bacon club,
                                           I told her we only have breakfast at this branch, but she came back again
                                           the following day and ordered the same thing. After I told her the
                                           that we really don't sell turkey bacon here, she smiled and gave something to me, wait here please." 
                                           The staff hurried into the storage room. He came back with a strange looking artifact in his hand.
                                           
                                           Strangly, your attantion is captured by it, as if it is speaking to you.
                                           
                                           "This is Spark Lance," said the staff, "the old lady said if one day this world is
                                           in trouble, someone would come here to order turkey bacon club, I should tell that
                                           person the same thing I told her at the first time. If that person came back again, 
                                           I should give this to them." 
                                           
                                           The Tim Horton's staff handed the artifact to you"""]

    #add status
    def check(self):
        self.__status += 1

    #return status
    def getstatus(self):
        return self.__status
