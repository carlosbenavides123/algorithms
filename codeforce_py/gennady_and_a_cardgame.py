
table_card = input()

my_hand = [card for card in input().split()]

def solve(table_card, hand):
    table_card = set(table_card)
    completed = False
    for card in hand:
        if card[1] in table_card or card[0] in table_card:
            print("YES")
            completed = True
            break
    if not completed:
        print("NO")
solve(table_card, my_hand)