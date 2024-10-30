# Peace Card Game
import random
import time
import os

cls = lambda: os.system("cls")

#Deck creation and cards
ranks = ["2", "3", "4" , "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["hearts", "diamonds", "clubs", "spades"]

deck = [(rank, suit) for rank in ranks for suit in suits]


random.shuffle(deck)

p1_deck = deck[::2]
p2_deck = deck[::-2]
random.shuffle(p1_deck)
random.shuffle(p2_deck)



def card_comparison(card1: tuple, card2: tuple) -> int:
    print(card1)
    print(card2)
    if (ranks.index(card1[0])) > (ranks.index(card2[0])):
        
        return 1
    elif (ranks.index(card2[0])) > (ranks.index(card1[0])):
        
        return 2
    else:
        return 0


def war(p1_deck: list, p2_deck: list):
    
    war_spoils = []
    x = 3
    if len(p1_deck) > 3 and len(p2_deck) > 3:
        print(len(p1_deck))
        print(len(p2_deck))
        while x != 0:
            war_spoils.append(p1_deck.pop(0))
            war_spoils.append(p2_deck.pop(0))
            x -= 1
        card1 = p1_deck.pop(0)
        card2 = p2_deck.pop(0)
        war_spoils.append(card1)
        war_spoils.append(card2)
        war_winner = card_comparison(card1, card2)
        if war_winner == 1:
            print("Player 1 has closed the peace talks.")
            for card in war_spoils:
                p1_deck.append(card)
            print(len(p1_deck))
                
        elif war_winner == 2:
            print("Player 2 has closed the peace talks.")
            for card in war_spoils:
                p2_deck.append(card)
            print(len(p2_deck))
        else: 
            print("Peace was a draw, redistributing cards")
            for card in war_spoils:
                if war_spoils.index(card) % 2 == 0:
                    p1_deck.append(card)
                if war_spoils.index(card) % 2 != 0:
                    p2_deck.append(card)
                random.shuffle(p1_deck)
                random.shuffle(p2_deck)
    elif len(p1_deck) == 3 or len(p2_deck) == 3:
        print("A triple trouble finale!")
        x = 2 
        while x != 0:
                war_spoils.append(p1_deck.pop(0))
                war_spoils.append(p2_deck.pop(0))
                x -= 1
        card1 = p1_deck.pop(0)
        card2 = p2_deck.pop(0)
        war_spoils.append(card1)
        war_spoils.append(card2)

        war_winner = card_comparison(p1_deck.pop(0), p2_deck.pop(0))
        if war_winner == 1:
                for card in war_spoils:
                    p1_deck.append(card) 
                    
        elif war_winner == 2:
                for card in war_spoils:
                    p2_deck.append(card)
                    
        else: 
            print("Peace was a draw, redistributing cards")
            for card in war_spoils:
                if war_spoils.index(card) % 2 == 0:
                    p1_deck.append(card)
                if war_spoils.index(card) % 2 != 0:
                    p2_deck.append(card)
                random.shuffle(p1_deck)
                random.shuffle(p2_deck)
    elif len(p1_deck) == 2 or len(p2_deck) == 2:
        print("Two versus the world, a tale old as time...")
        x = 1 
        while x != 0:
                war_spoils.append(p1_deck.pop(0))
                war_spoils.append(p2_deck.pop(0))
                x -= 1
        card1 = p1_deck.pop(0)
        card2 = p2_deck.pop(0)
        war_spoils.append(card1)
        war_spoils.append(card2)
        war_winner = card_comparison(card1, card2)
        if war_winner == 1:
                for card in war_spoils:
                    p1_deck.append(card) 
                    
        elif war_winner == 2:
                for card in war_spoils:
                    p2_deck.append(card)
                    
        else: 
            print("Peace was a draw, redistributing cards")
            for card in war_spoils:
                if war_spoils.index(card) % 2 == 0:
                    p1_deck.append(card)
                if war_spoils.index(card) % 2 != 0:
                    p2_deck.append(card)
                random.shuffle(p1_deck)
                random.shuffle(p2_deck)
    elif len(p1_deck) == 1 or len(p2_deck) == 1:
        print("A final stand for the honored card. \n")
        print("*fanfare*")
        card1 = p1_deck.pop(0)
        card2 = p2_deck.pop(0)
        winner = card_comparison(card1, card2)
        if winner == 1 and len(p1_deck) >= len(p2_deck):
            print("Player 1 made peace!")
            time.sleep(2)
            exit()
        elif winner == 2 and len(p1_deck) <= len(p2_deck):
            print("Player 2 made peace!")
            time.sleep(2)
            exit()
        elif winner == 1 and len(p1_deck) < len(p2_deck):
            print("Player 1 lives to peace another day...")
            p1_deck.append(card1, card2)
        elif winner == 2 and len(p1_deck) <= len(p2_deck):
            print("Player 2 lives to peace another day...")
            p2_deck.append(card1, card2)
        elif card1[0] == card2[0] and len(p1_deck) == len(p2_deck):
            print("A final draw. How poetic.")
            exit()
            


def play_round(p1_deck: list, p2_deck: list) :
    
    card1 = p1_deck.pop(0)
    card2 = p2_deck.pop(0)
    
    
    winner = card_comparison(card1, card2)
    if winner == 1:
        print("Player 1 won!")
        p1_deck.append(card2)
        
        
    elif winner == 2:
        print("Player 2 won!")
        p1_deck.append(card1)
        
        
    else:
        print("A draw, let us make peace!")
        war(p1_deck, p2_deck)

def play_game(p1_deck, p2_deck):
    
    print("""             ooooooooooo
         ooooooooooooooooooo
      oooooooo   oooo   oooooooo
    ooooooo      oooo      ooooooo
   oooooo        oooo        oooooo
  oooooo         oooo         oooooo
  ooooo          oooo          ooooo
 oooooo         oooooo         oooooo
 oooooo        oooooooo        oooooo
  ooooo      oooooooooooo      ooooo
  oooooo   oooo  oooo  oooo   oooooo
   oooooooooo    oooo    oooooooooo
    oooooooo     oooo     oooooooo
      oooooooo   oooo   oooooooo
         oooooooooooooooooooo
             oooooooooooo           8b,dPPYba,   ,adPPYba, ,adPPYYba,  ,adPPYba,  ,adPPYba,  
                                    88P'    "8a a8P_____88 ""     `Y8 a8"     "" a8P_____88  
                                    88       d8 8PP''''''' ,adPPPPP88 8b         8PP'''''''  
                                    88b,   ,a8" "8b,   ,aa 88,    ,88 "8a,   ,aa "8b,   ,aa   8b8b
                                    88`YbbdP"'   `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"'  `"Ybbd8"'   8b8b  
                                    88                                                       
                                    88    """)
    yes_or_no = False
    while  yes_or_no == False:
        game_playing = input("Start Game? \n Press Y  to start; press N to quit.")
        if game_playing.lower() == "n" :
            print("Have a good day!")
            exit()
        elif game_playing.lower() == "y" :
            yes_or_no = True
            print("Game starting...")
            t = 5
            while t > 0:
                timer = "{:02d}".format(t)
                print("In ", timer, end="\r" )
                time.sleep(1)
                t -= 1
            num_rounds = 1
            while len(p1_deck) >= 0 and len(p2_deck) >= 0:
                if len(p1_deck) == 0:
                    print(f"Player 1 is the winner!")
                    time.sleep(2)
                    exit()
                if len(p2_deck) == 0:
                    print(f"Player 2 is the winner!")
                    time.sleep(2)
                    exit()
                    
                print(f"Starting round {num_rounds}...")
                play_round(p1_deck, p2_deck)
                num_rounds += 1
                confirm = input("Start next round")
                if confirm is not None:
                    print("Starting next round...")
                cls()
        else:
            print("Please type Y or N.")
            
                

play_game(p1_deck, p2_deck)

        
