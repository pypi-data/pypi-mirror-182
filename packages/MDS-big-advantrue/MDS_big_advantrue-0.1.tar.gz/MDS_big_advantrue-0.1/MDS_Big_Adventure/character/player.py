from .character import character
from ..exceptions.InvalidPriceException import InvalidPriceException

#inheritence from character
class player(character):

    #initial location at tim horton

    #4 fighting locations in total
    #one alien on the first floor
    #one alien on the second floor
    #and two aliens on the third floor
    endPos = 4

    #initialize
    def __init__(self, health, power,money, identity):
        character.__init__(self, health, power)
        self.money = money
        self.__identity = identity
        self.position = 0

    #advance one floor if player does not reach to top floor
    def advance(self):
        try:
            if self.position < self.endPos:
                self.position += 1

                print("""
                       վ'ᴗ' ի you advanced""")
            else:
                print("""
                       (;´・`)> Can't advance further""")
        except UnicodeEncodeError as ex:
            print(ex)
            print("can't process the emoticons")

    #retreat one floor if player does not reach to tim horton
    def retreat(self):
        try:
            if self.position >= 1:
                self.position -=1
                print("""
                      ヽ(*。>Д<)o゜ you retreated""")
            else:
                print("""
                       (;´・`)> There is no other place to go""")
        except UnicodeEncodeError as ex:
            print(ex)
            print("can't process the emoticons")

    #return current position 
    def locate(self):
        return self.position

    #if at tim horton return current money
    def buy(self):
        if self.locate() == 0:
            return self.money

    #print the lines when player is defeated
    def defeat(self):
        print(
        """
                    No... you can't get up any more...
                    
                    ~~~~~~~~~~~~Sad BGM playing~~~~~~~~~~~~~~~~~
                     
                    You are defeated by the alien...
                    Before you lose consciousness, you felt the alien lifting you up.
                    Where would he take you? You may never have a chance to find out...
                    
                    What would become of the fate of humanity? 
                    ~~~~~~~~~~~~flashback of good memories~~~~~~~~
                    
                    But more importly, your assignment... you are going to miss it...
                    
                    You lost consciousness...
                    
                    Game over
                    
                    
        """)

        
    #display health, power and money according to player's identity  
    def display(self):
        if self.__identity == 0:
            print("('ᴗ')", character.display(self), " Money: {}".format(self.showMoney()))
        elif self.__identity == 1:
            print(".( o|o)/", character.display(self), " Money: {}".format(self.showMoney()))

    #get the money from the dead alien
    def getMoney(self, money):
        try:
            print("""
                                    You reclaimed ${} from the dead alien, they must have stolen these cash
                                    from someone's backpack""".format(money))
            self.money += money
        except(TypeError):
            print("You found something strange from the alien")
    
    #return current money value
    def showMoney(self):
        return self.money

    #deduct money when buying items in tim horton
    def pay(self,price):
        try:
            if price < 0:
                raise InvalidPriceException
            self.money -= price
        except TypeError:
            return "Price has to be a number"
        except(InvalidPriceException):
            return "Price can't be negative"

    #upgrade player identity when player gets spark lance
    def transform(self):
        self.__identity = 1

    #check if player is dead
    def isdefeated(self):
        if self.health == 0:
            return True

    #return player's identity
    def getidentity(self):
        return self.__identity
