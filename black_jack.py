import random

def get_card():

    c = random.randint(2,11)

    return c



def starting_cards():

    c1 = get_card()
    c2 = get_card()
    
    start_cards = c1 + c2
    return start_cards



def comparator(p,d):
    if p > d:
        #print("YOU WON")
        return 1
    elif p < d:
        #print("YOU LOST")
        return 2
    else:
        #print("DRAW")
        return 0



def player():

    players_cards = starting_cards()
    print(f"Your starting cards: {players_cards} \n")
    print("Press [1] to Hit")
    print("Press [2] to Stay")

    
    while players_cards <= 21:
        try:    
            print(f"Your cards: {players_cards}")
            players_move = int(input("Choose option: "))
            print()

            if players_move == 1:
                players_hit = get_card()
                print(f"Your hit: {players_hit}")
                players_cards += players_hit
                continue
            elif players_move == 2:
                print("You stayed")
                break
            else:
                print()
                print("Wrong choice! Try again \n")
                continue
        except Exception:
            print()
            print(f"Wrong choice! Try again")

    print(f"Your final cards: {players_cards}")
    if players_cards > 21:
        players_cards = 0

    return players_cards



def dealer():

    dealers_cards = get_card()
    print(f"Dealers starting card: {dealers_cards}")

    players_final_cards = player()

    while dealers_cards < players_final_cards:
        
        if dealers_cards < 17:
            dealers_hit = get_card()
            print(f"Dealer hit: {dealers_hit}")
            dealers_cards += dealers_hit
        else:
            break
    
    print(f"Dealers cards: {dealers_cards} \n")

    if dealers_cards > 21:
        dealers_cards = 0

    return dealers_cards, players_final_cards



def bet(money):
    while True:
        try:
            bet = int(input(f"Bet between 1 to {money}: "))
        except Exception:
            print("Your bet is not integer \n")
            continue
        if bet in range(1,money + 1):
            print(f"Your bet is {bet} \n")
            break

        else:
            print(f"Your bet is out of the range. Please bet between 1 to {money} \n")
            continue
    return bet

def ender():
    print("Press [1] to continue")
    print("Press [2] to leave")

    while True:
        try:    
            move = int(input("Choose option: "))
            print()

            if move == 1:
                print("Game Continues")
                return 1

                
            elif move == 2:
                print("Game Ended")
                return 2
            else:
                print()
                print("Wrong choice! Try again \n")
                continue
        except Exception:
            print()
            print(f"Wrong choice! Try again")



money = 1000
while money > 0:
    bets = bet(money)


    executed = False
    for i in dealer():
        if executed == False:
            d = i
            executed = True
        p = i


    c = comparator(p, d)

    if c == 1:
        money += bets
        print(f"YOU WON {bets} | You have {money} now")
    elif c == 2:
        money -= bets
        print(f"YOU LOST {bets} | You have {money} now")
    elif c == 0:
        print(f"DRAW | You have {money}")
    
    end = ender()

    if end == 1:
        continue

    elif end == 2:
        if money > 1000:
            print(f"You have Won {money-1000}")
            break

        elif money < 1000:
            print(f"You have Lost {1000 - money}")
            break
        
        else:
            print("You didn't won anything")