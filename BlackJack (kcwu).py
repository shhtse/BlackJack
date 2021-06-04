import random
user = input("Hello, What's your name?")

def restore_card():
    global card
    card = dict()
    face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    fv = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
    for s in ["♠", "♥", "♣", "♦"]:
        for i in range(13):
            card[s + face[i]] = fv[i]

def restore_lst():
    global name_lst, name_pt, name_card, sum, remove_lst
    sum = 0
    name_lst = ["🤴", "🤵", "👳", "💰", user]
    remove_lst = ["🤴", "🤵", "👳", "💰", user]
    name_pt = {}
    name_card = {}

def spacing():
    print("\n")

def drawing():
    for player in name_lst:
        global draw     # make a local variable global
        draw = random.choice(list(card))
        if player not in name_card:
            name_card[player] = draw
        elif player in name_card:
            name_card[player] += "," + draw
        val = card[draw]
        if player not in name_pt:
            name_pt[player] = 0
        if val == "(1, 11)":
            if name_pt[player] > 10:
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        card.pop(draw, None)  # drawing without replacement
        name_pt[player] += pt

def hitting():
    for player in remove_lst:
        draw = random.choice(list(card))
        name_card[player] += "," + draw
        val = card[draw]
        if card[draw] == "(1, 11)":
            if name_pt[player] > 10:
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        card.pop(draw, None)  # drawing without replacement
        name_pt[player] += pt
        if player == user:
            print(player, "hit, gets", draw)
            print(player, ":", name_card[player], "total point", name_pt[player])
        else:
            print(player, "hit, gets", draw)

def showing_card():
    spacing()
    print("dealer is now distributing the first card")
    drawing()
    for player in name_lst:
        print(player, ":", name_card[player], "total point", name_pt[player])

def not_showing_card():
    spacing()
    print("dealer is now distributing the second card")
    for player in name_lst:
        if player != user:
            print(player, ": ???", "with point: ???")
            continue
        drawing()
        print(player, ":", name_card[player], "total point", name_pt[player])

def hit_and_stand():
    spacing()
    while len(remove_lst) > 0:
        action = input("stand or hit?       :").lower()
        if action == "hit":
            for player in remove_lst:
                if player != user:
                    if name_pt[player] >= 16:
                        print(player, ": stand")
                        remove_lst.remove(player)
            hitting()
        elif action == "stand":
            while len(remove_lst) > 0:
                for player in remove_lst:
                    if player != user:
                        if name_pt[player] >= 16:
                            print(player, ": stand")
                            remove_lst.remove(player)
                            continue
                    elif player == user:
                        if name_pt[player] >= 16:
                            print(player, ": stand")
                            remove_lst.remove(player)
                            continue
                    elif player == user:
                        if name_pt[player] < 16:
                            print(player, ": stand")
                            remove_lst.remove(player)
                            continue
                hitting()
        else:
            print("Sorry, I don't understand.")

def choosing_winner():
    spacing()
    largest = []
    print("Result")
    for key, value in name_pt.items():
        if value > 21:
            print(key, "Bust")
            continue
        largest.append(value)
        large = max(largest)

    for player in name_lst:
        if name_pt[player] == large:
            print(player, "is the winner, with points:", large)
        print(player, "has:", name_card[player], "             with total point:", name_pt[player])

def again():
    while True:
        try:
            again = input("would you like to start a New Round?").lower()
            if again == "yes":
                main()
            elif again == "no":
                print("See U")
                break
        except:
            print("Sorry, I don't understand. Please try again")

def main():
    restore_card()
    restore_lst()
    showing_card()
    not_showing_card()
    hit_and_stand()
    choosing_winner()
    again()

main()