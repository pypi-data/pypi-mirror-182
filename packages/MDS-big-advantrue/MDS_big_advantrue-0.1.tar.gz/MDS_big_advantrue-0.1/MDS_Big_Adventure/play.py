import random

from .item.food import item
from .item.sparkLance import sparkLance
from .scene.level import level
from .scene.timhortons import timHortons
from .character.alien import alien
from .character.player import player


class play():

    #beginning scripture
    script0 = """
        It is an ordinary day in the MDS program, you finished the morning classes
        and went to Tim Hortons for lunch. All of a sudden, you hear a big bang sound
        tearing through the sky. You looked up, UFOs! Alien vessels are hovering over the
        science building, aliens are landing on the roof! People around you started screaming
        and running. You suddenly realized something important, your laptop is still in the building,
        and you haven't submitted the lab in it! You need to go get your laptop!
        
        You are at Tim Hortons
        What is your next move?
        
        """

    #initialize
    def __init__(self):
        #player with 100 health, 100 power, 0 moeny, general identity
        self.p1 = player(100, 100,0,0)

        #item named hashbrown with health bonus 10, power bonus 5, price $3, amount 2
        self.i1 = item("hashbrown", 10, 5, 3, 2)

        #item named maple bacon bagel belt with health bonus 30, power bonus 15, price $7, amount 1
        self.i2 = item("maple bacon bagel belt", 30, 15, 7, 1)

        #item named sausage farmer's wrap with health bonus 40, power bonus 25, price $8, amount 1
        self.i3 = item("sausage farmer's wrap", 40, 25, 8, 1)

        #item named Spark Lance with health multiply 100, power multiply 100, status 0
        self.sparklance = sparkLance("Spark Lance", 100, 100, 0)

        #create tim horton at location 0 with 3 items and a non-aggressive alien
        self.tim = timHortons(0, ["you are in tim's","you are in tim's"], alien(0,0,"place holder",0), [self.i1,self.i2,self.i3])

        #alien named alien scientist with health 100, power 80, money 3
        self.a1 = alien(100, 80, "alien scientist",3)

        #alien named alien infantry soldier with health 120, power 90, money 8
        self.a2 = alien(120, 90, "alien infantry soldier",8)

        #alien named alien infantry soldier with health 150, power 100, money 10
        self.a3 = alien(150, 100, "alien elite commando",10)

        #alien named alien captain with health 200, power 150, money 15
        self.a4 = alien(200,150, "alien captain", 15)

        #scriptures for each level
        self.cr1 = level(1, ["""
                                You are on the first floor of the science building
                                It is a huge mess. Most of the students have escaped from the building, some are still running around
                                looking for the exit. There is one still studying... wait... no... that's not a student!
                                A tall scientist looking alien is scanning the papers on the wall. "#$#^%*&statist*csss, %$#!@$%...", he is murmuring
                                to himself. Apparently, he is stealing, or mocking, the scientific progress of Earth. Either way, you need to
                                stop him! """,
                             """
                               You returned to the first floor, it is very quiet here
                              "turkey bacon club ~~~" You heard an indistinctive whisper, it might just be an illusion"""], self.a1)
        self.cr2 = level(2, ["""
                                You are on the 2nd floor
                                You found a soldier looking alien standing in front of he garbage bins, holding a weapon.
                                He looks puzzled, as if he is confused what garbage should go to which bin. "&*@&#(@)#&?", he murmured
                                with frustration. You can seize this chance to attack him by surprise!""",
                             """
                                 you returned to the second floor, there is nobody here, only over turned garbage bins
                                "turkey bacn club~~", you think you heard a whisper, but there is nobody here...
                                """], self.a2)
        self.cr3 = level(3, ["""
                                You are on the third floor
                                There is an alien in the chemistry lab drinking random chemicals.
                                "&#*!!!!!", he probably drank one of the acids. As he madly wiped his tongue, he spotted you!
                                """,
                             """
                                 you returned to the chemistry labs
                                 """], self.a3)
        self.cr4 = level(4, ["""
                                You finally entered SCI 396
                                An alien with fancy armor is in the classroom. He is...well...swiveling on one of the swivel chairs.
                                "Ahhh!!!! Well! come!! warrior of this PLANET!!!! I have been MONITORING your PROGRASS!!!" 
                                He got up and shouted to you in human language.
                                
                                "You can speak our language? What were you doing on the chair? And why are you shouting?" You are puzzled.
                                
                                "My universal TRANSLATOR have picked up some preliminary samples from the HUMANS screaming and running AROUND!!!
                                But the samples are limited to mostly shouting and CRYING! in despair， as you can imagine!!!
                                At least it WORKS for now!!! I AM! the captain OF the &^*(*^ vessel *((*^, We are ON our pilgrimage!!!"
                                
                                "OK, I see... what pilgrimage? And I am not a warrior, I just need my laptop to finish my assignment,
                                it is due in a few ours. "
                                
                                "Oh, what a brutal civilization! You torture your children at this kindergarten and force your warriors to do
                                children's work for no reason!" He is not shouting as much now, his universal translator must have sampled your
                                normal speaking.
                                
                                "What are you talking about, this is not a kindergarten, it is a university, and we don't torture our children!"
                                
                                "What?!, you are teaching Maximum likelihood estimation at a university? My 2-year-old daughter can do that.
                                And these swivel chairs are not for swiveling students who answered the questoin wrong for punishment? And what about
                                those cafeteria next door, the terrible foods are not for torturing the students?" Said the alien.
                                
                                "What? No, no the equations... the chairs...ah I don't even want to explain. And those labs next door are not cafeteria,
                                there are dangerous chemicals in it! Well... but you might be right about the foods on campus... "
                                
                                "Who would put chemicals in a kindergarten... ah!! never mind. Now, I should complete our pilgrimage and take you and some
                                other humans as offering to the god of (*&%$ before we nuke this entire planet. " The alien captain pulled out his weapon.
                                
                                "So your pilgrimage is to kidnap warriors from other planets before destroying them, what an envil civilization, I will 
                                not let you do that!"
                                
                                """, "You returned to the classroom, the alien vessel is gone, there are just broken glasses and swivel chairs swiveling"], self.a4)
        self.map = [self.tim, self.cr1, self.cr2, self.cr3, self.cr4]


    '''
    buy items at tim horton
    display items at tim horton
    ask player for what to order
    update player's health, power and money
    '''
    def buyItem(self):
        if self.p1.locate() == 0:
            for i in self.tim.getInv():
                print("""
                """,i.display())
            order = input("What do you want to order today? ")
            result = self.tim.checkStock(order)
            if result != 1 and result != 2 and result != 3:
                if self.p1.buy() >= result.getprice():
                    self.p1.pay(result.getprice())
                    self.tim.sell(result)
                    print("""
                                  You sat down and enjoyed the {}""".format(result.getname()))
                    print("""                           <(▰˘◡˘▰)>
                                  You feel better now, your health and power are restored""")
                    result.addhealth(self.p1)
                    result.addpower(self.p1)
                else:
                    print("""
                         Oh no you don't have enough money
                    """)

            elif result == 1:
                print("""
                               Sorry, we sold out {}, do you want to 3) order something else?""".format(order))
            elif result == 2:
                print("""
                                  Sorry, can you say again?""")
            elif result == 3:
                self.sparklance.check()
                if self.sparklance.getstatus() == 2:
                    print(self.sparklance.getplot()[1])
                    print(self.sparklance.getplot()[0])
                    self.sparklance.betaTransform(self.p1)
                    self.sparklance.getSpacium(self.p1)
                    self.p1.transform()
                else:
                    print("""
                                  Sorry, we only have breakfast at this branch""")
           
        else:
            print("""
                                  There is no store here""")



    '''
    4 fighting locations in total
    0 alien at location 0
    1 alien on the first floor
    1 alien on the second floor
    and 2 aliens on the third floor
    utilize random method to get random advantages for both player and allien
    calculate the fight result
    output scripture and fighting result depends on player's identity and calculated power
    unlock the level, and get the moeny when alien at that level is dead
    '''                
    def fight(self):
        if self.p1.locate() == 0:
            print("""
                                   There is no one to fight here""")
        else:
            for r in self.map[1:]:
                if r.getLoc() == self.p1.locate():
                    if self.p1.getidentity() == 0:
                        print("""
                                                (ง •̀_•́)ง   VS   (╰_╯)
                                                you are fighting the alien""")
                    else:
                        print("""
                                                <(o|o)>   VS   (╰_╯)
                                                you are fighting the alien""")
                        
                    dice1 = random.randint(1,6)
                    dice2 = random.randint(1,6)
                    result = int(self.p1.fight()*(1+dice1/10) - r.getAlien().fight()*(1+dice2/10))
                    print("""
                                             Your advantage: {}    Alien advantage: {}""".format(dice1, dice2))
                    if result > 0:
                        r.getAlien().wound(result)
                        if self.p1.getidentity() == 0:
                            print("""
                                               (╯°口°)╯︵ ┻━┻  {}
                                               you inflicted {} damage to the alien""".format( r.getAlien().display(),result))
                        else:
                            print("""
                                               ( o|o)ノ三三三三三三三三三  {}
                                               you inflicted {} damage to the alien""".format( r.getAlien().display(),result))

                        if r.getAlien().isdead():
                            print("""
                                             └(^o^)┘ you defeated the alien""")
                            self.p1.getMoney(r.getAlien().dropMoney())
                            r.getAlien().die()
                            r.unlock()
                    elif result == 0:
                        print("""
                                            (ꐦಠ ಠ)     {}
                                            The alien is as strong as you
                                            You had a draw with the alien""".format(r.getAlien().display()))
                    else:
                        print("""
                                            _(:\ 」∠)_      {}
                                            The alien knocked you off, inflicting {} damage on you
                                            you can still stand up to fight""".format(r.getAlien().display(), abs(result)))
                        self.p1.wound(abs(result))
                        if self.p1.isdefeated():
                            self.p1.defeat()


                        

    '''
    if player arrive at 4 location and alien's power at 4 location is 0, then player win the game
    '''
    def win(self):
        if self.p1.locate() == self.p1.endPos and self.cr4.getAlien().health == 0:
            print("""
                        You took your laptop from the dead alien captain, it still works! Your lab files are intact!
                        With its commander dead, the alien vessel fled to the space, they dare not to cross Earth again.
                        Without further delay, you submitted the lab to canvas and headed back home. Just another day in
                        the MDS program. -end
                        You can continue to walk around or just go back home
            """)



    '''
    advance one level up when the level is unlocked, display the alien and set the location status visited
    report error when the level us locked
    '''
    def advance(self):
        flag = 0
        for r in self.map:
            if flag == 1:
                break
            else:
                if r.getLoc() == self.p1.locate():
                    flag = 1
                    if r.islocked():
                        print("""
                              as you approach, the alien shouted at you, you can't advance further""")
                    else:
                        self.p1.advance()
                        for l in self.map: 
                            if l.getLoc() == self.p1.locate():
                                try:
                                    print("""
                                        {} 
                                        (/ﾟДﾟ)/ you found an {} ({}) in front of you
                                        """.format(l.getplot(), l.getAlien().getName(), str(l.getAlien().display())))
                                except Exception as ex:
                                    print(ex)
                                l.visit()
                            
    
            
    '''
    display the scripture and ask the player for 5 options of next steps
    option 1 advance
    option 2 retreat
    option 3 buy item at tim horton
    option 4 fight against alien
    option 0 exit the game
    '''
    def play(self):
        command = 0
        print(self.script0)
        while 1:
            self.win()
            print("____________________________________________________")
            print("1) advance  2) retreat  3)buy item 4) fight 0) exit")
            self.p1.display()
            try:
                command = int(input("what is your next move?"))
                if command > 4:
                    raise Exception

                if command == 1:
                    self.advance()
                elif command == 2:
                    self.p1.retreat()
                    for r in self.map:
                        if r.getLoc() == self.p1.locate():
                            try:
                                print("""
                                {}
                                """.format(r.getplot()))
                            except Exception as ex:
                                print(ex)
                elif command == 0:
                    print("game over")
                    break
                elif command == 3:
                    self.buyItem()

                elif command == 4:
                    self.fight()
                    if self.p1.isdefeated():
                        break
            except(ValueError):
                print("""
                          Please enter a number""")
            except Exception as ex:
                print(ex)
                print("""
                          Please select from available Options""")

