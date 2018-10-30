# python3

import sys

def main():
    hand = input().split()
    suits = ['C', 'D', 'H', 'S']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    hand_suit = hand[0][1]

    hand.sort(key=lambda card: ranks.index(card[0]))
    if hand[4][0] == 'K' and hand[0][0] == 'A':
        hand = hand[1:] + [hand[0]]
    # print("hand: ", hand)

    i = 0
    for card in hand[1:]:
        # print(card)
        d = ranks.index(card[0]) - ranks.index(hand[i][0])
        i += 1
        # print(d)
        if d != 1 and d != -12:
            print('NO')
            return

        if card[1] != hand_suit:
            print('NO')
            return

    print('YES')

if __name__ == '__main__':
    main()