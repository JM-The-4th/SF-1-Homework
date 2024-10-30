#Uno!
import random
import os
import time


#TWO PLAYER UNO: TWONO HAHAAHAHAH IM FUNNY

cls = lambda: os.system("cls")

#Creating 1st deck
colours = ("Red", "Green", "Blue", "Yellow")
ranks = list(range(0,10))
deck = [(rank, colour) for rank in ranks for colour in colours]


#Creating a 2nd deck without zeros
no_zerodeck = list(filter(lambda a: a[0] != 0, deck))

#Creating a deck of all numbers
numdeck = deck + no_zerodeck

#Defining the action and wild cards
actions = ("Reverse", "Skip", "+2")
wild =  [("Wild")]
wild_actions = [("+4"),("Switch")]
action_deck = [(special, colour) for special in actions for colour in colours]
wild_deck = [(wild_action, colour) for wild_action in wild_actions for colour in wild] * 4
print(wild_deck)
full_deck = numdeck + wild_deck + action_deck

#Shuffle deck and assign hands
random.shuffle(full_deck)
p1_deck = full_deck[:7]
p2_deck = full_deck[7:14]
center_deck = full_deck[14:21]

#Flipping 1st card
face_up = [center_deck.pop(0)]

#Turn Counter
current = 0


#Defined functions
def valid_play(card: tuple, face_up: list,):
    if face_up[0][0] == card[0] or face_up[0][1] == card[1] or card[1] == "Wild":
        return True
    else:
        
        return False


def skipcheck(card: tuple):
    if card[0] == "Skip": return True
    else: return False


def plus2check(card: tuple):
    if card[0] == "+2": return True 
    else: return False

def reversecheck(card: tuple):
     if card[0] == "Reverse": return True
     else: return False
    
        
    
def wild_plus4check(card: tuple):
    if card[0] == "+4": return True
    else: return False

def wild_switchcheck(card: tuple):
    if card[0] == "Switch": return True
    else: return False

def wild_switch():
        while True:
            newcolor = input("Pick a new color.")
            if newcolor == face_up[1][1]:
                print("This is the same color")
            elif newcolor.lower() == "blue":
                face_up.insert(0, ("", "Blue"))
                break
            elif newcolor.lower() == "red":
                face_up.insert(0, ("", "Red"))
                break
            elif newcolor.lower() == "yellow":
                face_up.insert(0, ("", "Yellow"))
                break
            elif newcolor.lower() == "green":
                face_up.insert(0, ("", "Green"))
                break
            else: 
                print("Pick an actual game color dingus")


def ai_wild_switch():
        
        color_choices = ["Blue", "Green", "Yellow", "Red"]
        for color in color_choices:
            if color == face_up[1][1]:
                   face_up.insert(0, ("", color))
                   

def first_wild_switch():
     while True:
                                newcolor = input("Pick a new color.")
                                if newcolor == face_up[0][1]:
                                    print("This is the same color")
                                elif newcolor.lower() == "blue":
                                    face_up.insert(0, ("", "Blue"))
                                    break
                                elif newcolor.lower() == "red":
                                    face_up.insert(0, ("", "Red"))
                                    break
                                elif newcolor.lower() == "yellow":
                                    face_up.insert(0, ("", "Yellow"))
                                    break
                                elif newcolor.lower() == "green":
                                    face_up.insert(0, ("", "Green"))
                                    break
                                else: 
                                    print("Pick an actual game color dingus")


    
    



def call_UNO():
    
    t = 5
    print("Yuo'er Win!!!!")
    while t:
         timer = "{:02d}".format(t)
         print("Exiting in: ", timer, end="\r")
         time.sleep(5)
         t -=1
    exit()

def AI_Turn(p1, p2, center_deck, face_up) -> tuple:
    for card in p1:
         global current 
                            
         if valid_play(card, face_up) == True and (card[0] in actions or card[0] in wild_actions):
             face_up.insert(0, p1.pop(p1.index(card)))
             current = (current + 1) % 2
             print(f"Player 2 has played {card}.")
            #Skip
             return card
             
    for card in p1:  
         if valid_play(card, face_up) == True:
             print("Card is valid!")
             face_up.insert(0, p1.pop(p1.index(card)))
             print(f"Player 2 has played {card}.")
             current = (current + 1) % 2
             print(p1)
             p1, p2 = p2 , p1
             print(p1)
             return card
             
         
    p1.append(center_deck.pop(0))
    print("Player 2 has skipped their turn.")
    current = (current + 1) % 2
    
    print(p1)
    

             
             


    

#Main Game function


def main_loop(p1: list, p2:list, face_up: list, center_deck: list):
  
  global current #for some reason nothing works if it isn't global
  print("Welcome to TwoNO!\n")
  print("""⣰⣾⢿⣟⣿⠿⠿⢿⣿⣻⣟⣿⣻⣟⣿⣻⣟⣿⣻⢿⣻⢿⣻⢿⣻⢿⣶⡄
⣿⢯⡿⣾⠟⠃⠀⢰⣿⣳⣟⡾⣷⣻⣞⣷⡻⠞⠛⠉⠉⠉⠉⠙⠻⢟⣾⣽
⡿⣯⣿⣏⣀⠔⢿⣾⣟⡷⣯⣟⣷⠯⠋⢀⣤⣶⣶⢿⣿⣻⢿⣶⣦⡀⠙⢿
⣿⣻⡟⠟⠀⢀⣼⡿⣼⢿⣧⠟⠀⣠⣼⡿⣿⣼⣻⢿⣼⣻⢿⡼⣧⣿⡄⠘
⣿⣽⣇⣀⣐⣿⡿⣽⣯⠛⢀⣴⢿⣯⢷⣟⡷⣯⣟⡿⣾⡽⣯⢿⣳⣯⣷⡀
⣿⣞⣿⣻⢿⣯⣟⠗⢀⣴⣟⣯⢿⣞⡿⣞⣿⣳⣯⣟⡷⣟⣯⣿⣻⢾⡽⣧
⣷⣻⢾⣽⣻⡾⠁⣠⣿⣳⢿⣞⣯⡿⣽⣻⣞⣷⣻⣞⡿⣽⣳⣯⣟⣯⣟⣿
⣿⣽⣻⢾⠝⢀⣼⢯⣷⣻⣟⣾⣽⣿⠿⠷⠿⠿⠷⢿⣿⣽⣳⣟⣾⡽⣾⡟
⣟⣾⣽⠃⢠⣾⢯⣟⡷⣟⣾⡽⣿⣿⠗⠀⠀⠀⠀⣼⣿⢾⣽⢾⣳⣿⣳⡇
⣿⢾⠁⢠⣿⡽⣯⢿⣽⢯⣷⡿⠋⠁⠀⠀⢀⡄⠀⣿⣯⢿⣞⡿⣽⡾⡽⠀
⣿⠃⢠⣿⣳⢿⣽⣻⢾⣻⣿⠁⠀⠀⢀⡶⣿⣿⣶⣿⢯⡿⣞⣿⣳⢿⠏⢠
⡇⠀⣾⣷⢿⡿⣾⣏⣿⣿⣿⡆⢀⡾⠉⠀⢹⣿⣿⣹⣏⡿⣏⣷⡿⡏⠀⣾
⠁⣼⣟⣾⣻⣽⢷⣻⣿⠻⣿⡿⠋⠀⠀⠀⣸⣿⣳⣟⡾⣿⣽⣳⡿⠁⣰⣿
⢀⣿⣞⡷⣯⣟⣯⣿⡟⠀⠀⠀⠀⠀⣠⣾⡿⣯⢷⣻⣽⢷⣯⡷⠁⣰⣿⣻
⣸⡷⣯⢿⣳⣯⢿⣿⠇⠀⠀⠀⠐⢿⣿⢯⡿⣽⣻⣽⢾⣻⡞⠁⣰⣿⣳⣿
⣿⡽⣯⣟⡿⣞⣿⣿⣶⣶⣶⣶⣶⣾⡿⣯⢿⣽⣳⣯⢿⠟⢀⣾⣟⣷⣻⣞
⣷⣻⣽⢾⣻⣽⢯⣟⣿⣻⣟⣿⣻⣽⣻⡽⣟⣾⣽⡾⠋⣠⡿⣾⡽⣞⣷⣻
⣯⣷⣻⢯⣟⣾⢯⣟⣾⣳⣟⣾⣳⣯⢷⣟⣯⡷⠏⢀⣴⣿⡽⣷⣻⢯⡿⣽
⠸⣷⣻⢯⣟⡾⣿⡽⣾⣽⢾⣳⣟⣾⢯⣿⠚⢁⣴⣿⣻⣞⣿⡛⠛⢻⣟⣿
⠀⢹⣯⣿⣽⢻⣷⢻⣷⣯⡟⣿⣾⡝⠋⢠⣴⣿⢻⡞⣷⡟⠉⠀⣤⢸⣿⣾
⣧⡀⠙⠷⢟⣿⣞⡿⣾⡽⠻⠓⢁⣠⣶⢿⣻⡽⣯⣟⣿⣇⡠⠊⢻⣿⢷⣻
⣿⣻⣶⣤⣀⣀⣈⣁⣀⣤⣴⡾⣟⣯⣟⣯⢿⡽⣷⣻⠇⠁⢀⣴⣿⢯⣿⣻
⠻⢷⣻⣞⡿⣯⢿⣽⣻⣽⣳⢿⣯⢷⣯⣟⣯⡿⣽⢿⣶⣶⣾⣟⣯⣿⠾⠃
⠀⠀⠀⠈⠀⠁⠈⠀⠁⠀⠁⠈⠀⠁⠀⠈⠀⠁⠈⠀⠀⠀⠀⠈⠀⠀⠀⠀""")
  if face_up[0][0] == "Switch":  
                        first_wild_switch()
                        
                
  elif face_up[0][0] == "+4":
                    
                        print("Tough Luck bro ¯\_(ツ)_/¯ \n Added 4 Cards.")
                        x = 4
                        while x > 0:
                             p1.append(center_deck.pop(0))
                             x -= 1
                        print("Pick a color, I feel bad for you.")
                        first_wild_switch()
                        
  
        
             
    

    
            #Normal play
  while len(p1) > 0 and len(p2) > 0:
                print(face_up)
                if len(center_deck) == 0 and len(face_up) > 7:
                    print(face_up)
                    for card in face_up:
                        if card[0] == "":
                         face_up.remove(card)
                    center_deck = face_up
                    random.shuffle(center_deck)
                    face_up = [center_deck.pop(0)]
                elif len(center_deck) == 0 and len(face_up) <= 7:
                    print("Stop spam drawing cards")
                    while len(p1) > 7:
                            center_deck.insert(0, p1.pop(0))
                else:print("All good.")
                    
            #Card is unselected
                valid_card = False
            #Indicator
                print("\n")
                print("_____________________________________")
                print(f"It is player {current + 1 }'s turn.")
                print(f"The face up card is {face_up[0]}.")
                print(f"Player {current + 1}'s hand is {p1}")
                print("_____________________________________")
                print("\n")
    
    
            # If AI has UNO
                if current == 1 and len(p1) == 1 and valid_play(p1[0], face_up) == True:
                     print("AI wins, GG.")
                     time.sleep(3)
                     exit()
                      
                
        
                #Actual player game starts
                if current == 0:   
        
                            p1choice = input("Press D to draw a card, press P to play a card.")
                       
                            if len(p1) == 1 and valid_play(p1[0], face_up) == True:
                                   if p1choice.lower() == "uno":
                                       face_up.insert(0, p1.pop(0))
                                       call_UNO()
                                   else:
                                    print("You forgot to say UNO silly")
                                    rip_bozo = 2
                                    while rip_bozo > 0:
                                         p1.append(center_deck.pop())
                                         rip_bozo -= 1
                                    p1, p2 = p2, p1
                                    current = (current + 1) % 2
                                         
                            if  p1choice.lower() == "d":
                                   p1.append(center_deck.pop(0))
                                   print("You passed your turn.")
                                   p1, p2 = p2, p1
                       
                                   current = (current + 1) % 2
                            elif p1choice.lower() == "p" :
                                print("Pick a card by selecting its index from 1 to whatever your hand size is. To go back, type 000")
                                print(p1)
                                print([i for i in range(1, len(p1) + 1)])
                                #Ensures that player can retry if wrong card is selected
                                while valid_card == False:
                                        
                                    index = input("Pick a card:")
                                    if str.isdigit(index):
                                        played_index = (int(index) - 1)
                                        if played_index == -1:
                                            break
                                        if played_index <= len(p1):
                                            print("run")
                                            played_card = p1[played_index] 
                                            if valid_play(played_card, face_up) == True:
                                                    played_card = p1.pop(played_index)
                                                    face_up.insert(0, played_card)
                                                    print(face_up)
                                        #Skip
                                                    if skipcheck(played_card) == True:
                                                        p1, p2 = p2, p1
                                                        
                                                        current += 1
                                        #Reverse
                                                    if reversecheck(played_card) == True:
                                                        p1, p2 = p2, p1
                                                        
                                                        current += 1
                                                         
                
                                        #+2 Card
                                                    if plus2check(played_card) == True:
                                                        print("+2")
                                                        x = 2
                                                        while x != 0:
                                                            p2.append(center_deck.pop(0))
                                                            x -= 1
                                                        p1, p2 = p2, p1
                                                        current += 1
                                        #Wild +4
                                                    if wild_plus4check(played_card) == True:
                                                        print("+4")
                                                        x = 4
                                                        while x != 0:
                                                            p2.append(center_deck.pop(0))
                                                            x -= 1
                                                        wild_switch()
                                                        p1, p2 = p2, p1
                                                        current += 1
                                                        
                
                                        #Wild Color Change
                                                    if wild_switchcheck(played_card) == True:
                                                        wild_switch()
                                
                                                    
                                                    
                                                    current = (current + 1) % 2
                
                                                    p1, p2 = p2, p1
                                                    valid_card = True
                                                    
                                                           
                                        else:
                                                print("This is not a valid card.")
                                    else:
                                        print("Enter a number only please.")
                        
                            
                            else:
                                   print("Invalid input")
                                   
                elif current == 1:
            #AI TURN
                    AI_played_card = ("" , "")
                    AI_played_card = AI_Turn(p1, p2, center_deck, face_up)
                    if AI_played_card is not None:
                        print(AI_played_card)
                        if skipcheck(AI_played_card) == True:
                            p1, p2 = p2, p1
                            current += 1
            #Reverse
                        if reversecheck(AI_played_card) == True:
                            p1, p2 = p2, p1
                            
                            current += 1
                             

            #+2 Card
                        if plus2check(AI_played_card) == True:
                            print("+2")
                            x = 2
                            while x != 0:
                                p2.append(center_deck.pop(0))
                                x -= 1
                            p1, p2 = p2, p1
                            
                            current += 1
            #Wild +4
                        if wild_plus4check(AI_played_card) == True:
                            print("+4")
                            x = 4
                            while x != 0:
                                p2.append(center_deck.pop(0))
                                x -= 1
                            ai_wild_switch()
                            p1, p2 = p2, p1
                            
                            current += 1
                            

            #Wild Color Change
                        if wild_switchcheck(AI_played_card) == True:
                            ai_wild_switch()
                            
                    p1, p2 = p2, p1
                        
                    
                    
        
   
                        
                        
        
main_loop(p1_deck, p2_deck, face_up, center_deck)
