import random

ranks = ['2','3','4','5','6','7','8','9','10',"J","Q","K","A"]
cards = ranks * 4
'''random.shuffle(cards)
print(cards)'''
cards_value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, "J":10, "Q":10, "K":10, "A":10}

def getCards(player_deck, computer_deck):
    for i in range(2):
        player_deck.append(cards[0])
        cards.pop(0)
        computer_deck.append(cards[0])
        cards.pop(0)
    return player_deck, computer_deck

def calcValueP(player_deck):
    player_value = 0
    for i in range(0, len(player_deck)):
        player_value = cards_value.get(player_deck[i]) + player_value
    return player_value

def calcValueC(computer_deck):
    comp_value = 0
    for i in range(0, len(computer_deck)):
        comp_value = cards_value.get(computer_deck[i]) + comp_value
    return comp_value

def playerhit(player_deck):
    player_deck.append(cards[0])
    cards.pop(0)
    return player_deck

def display1(player_deck, computer_deck):
    print("----------------------------------------------")
    print("player's cards:", ' '.join(player_deck))
    print("Computer cards: ?", ' '.join(computer_deck[1:]))
    print("----------------------------------------------")

def display2(player_deck, computer_deck):
    print("player's cards:", ' '.join(player_deck))
    print("Computer cards:", ' '.join(computer_deck))
    print("----------------------------------------------")

def comp_draw_card(computer_deck):
    computer_deck.append(cards[0])
    cards.pop(0)
    return computer_deck

def playerBlackJack(player_deck):
    if len(player_deck) == 2:
        picture = False
        ace = False
        for card in player_deck:
            if card == "10" or card == "J" or card == "Q" or card == "K":
                picture = True
            elif card == "A":
                ace = True
        if ace and picture == True:
            print("Players wins; Blackjack!!!")
            blackjack()

def compBlackJack(computer_deck):
    if len(computer_deck) == 2:
        picture = False
        ace = False
        for card in computer_deck:
            if card == "10" or card == "J" or card == "Q" or card == "K":
                picture = True
            elif card == "A":
                ace = True
        if ace and picture == True:
            print("Computer wins; Blackjack!!!")
            blackjack()

def playerDouble(player_deck):
    if len(player_deck) == 2:
        if player_deck[0] == player_deck[1]:
            print("Player wins; Double!!")
            blackjack()

def compDouble(computer_deck):
    if len(computer_deck) == 2:
        if computer_deck[0] == computer_deck[1]:
            print("Computer Wins; Double!!")
            blackjack()

def declare_winner(player_deck, computer_deck):
    player_value = calcValueP(player_deck)
    comp_value = calcValueC(computer_deck)
    if player_value > 21 and comp_value > 21:
        print("Draw")
    else:
        if player_value > 21:
            print("Computer Wins; Players busts")
        if comp_value > 21:
            print("Player Wins; Computer busts")
        else:
            if player_value > comp_value:
                print("player wins")
            else:
                print("computer wins")

def blackjack():
    '''ranks = ['2','3','4','5','6','7','8','9','10',"J","Q","K","A"]
    cards = ranks * 4'''
    random.shuffle(cards)
    player_deck = []
    computer_deck = []
    getCards(player_deck, computer_deck)
    display1(player_deck, computer_deck)
    while True:
        '''display1(player_deck, computer_deck)
        print(computer_deck)'''
        option = input("Hit (h) or Stand(s)")
        if option == "h":
            playerBlackJack(player_deck)
            compBlackJack(computer_deck)
            playerDouble(player_deck)
            compDouble(computer_deck)
            playerhit(player_deck)
            comp_value = calcValueC(computer_deck)
            if comp_value <= 16:
                comp_draw_card(computer_deck)
            else:
                pass
        elif option == "s":
            playerBlackJack(player_deck)
            compBlackJack(computer_deck)
            playerDouble(player_deck)
            compDouble(computer_deck)
            comp_value = calcValueC(computer_deck)
            if comp_value <= 16:
                comp_draw_card(computer_deck)
            else:
                declare_winner(player_deck, computer_deck)
                display2(player_deck, computer_deck)
                blackjack()
        else:
            pass
        display1(player_deck, computer_deck)

blackjack()
