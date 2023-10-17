import random


def main():
    cards = [
        "2","3","4","5","6","7","8","9","10","11",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
    ]
    player_cards = []
    pc_cards = []
    while True:
        try:
            start = str(input("Do you want to play BlackJack? Type 'y' for start: "))
            if start == "y":
                break
        except ValueError:
            pass
    # draw for player
    first_draft(cards, player_cards, pc_cards)
    print(f"Your cards: ", " ".join(player_cards))
    print(f"PC Card is: ",pc_cards[0])
    while True:
        try:
            start = str(
                input("Do you want draw another card? Type 'y' for yes or 'n' for no: ")
            )
            if start == "y":
                draft_additional_card(cards,player_cards)
                print(f"Your cards: ", " ".join(player_cards))
                continue
            else:
                calculate_score(player_cards, pc_cards)
                break

        except ValueError:
            pass


def first_draft(cards, player_card, pc_cards):
    for _ in range(2):
        card_index = random.randint(0, len(cards))
        card = cards[card_index]
        del cards[card_index]
        player_card.append(card)
    for _ in range(2):
        card_index = random.randint(0, len(cards))
        card = cards[card_index]
        del cards[card_index]
        pc_cards.append(card)


def calculate_score(player_cards, pc_cards):
    player_score = 0
    pc_score = 0
    for _ in range(len(player_cards)):
        player_score = player_score + int(player_cards[_])
    for _ in range(len(pc_cards)):
        pc_score = pc_score + int(pc_cards[_])
    if pc_score < player_score < 22 and pc_score < 22:
        print("Player win")
    else:
        print("Pc win")

    print("Your cards:", " ".join(player_cards))
    print("Player:", player_score)
    print("PC:", pc_score)


def draft_additional_card(cards, player_card):
    card_index = random.randint(0, len(cards))
    card = cards[card_index]
    del cards[card_index]
    player_card.append(card)


if __name__ == "__main__":
    main()
