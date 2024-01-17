from itertools import combinations
import matplotlib.pyplot as plt

def is_eligible_badugi(hand):
    ranks = list(range(1, 14))  # Ace to King represented by 1 to 13
    
    def is_valid_rank(card):
        return card in ranks

    if 13 in hand:


        king_index = hand.index(13)
        # If there is a King in the hand, check if all other cards are Ace or 8 and below
        king_condition = all(index == king_index or (is_valid_rank(card) and card <= 8) for index, card in enumerate(hand))        
        # Check if the hand has exactly 4 unique cards
        unique_condition = len(set(hand)) == 4
        
        return king_condition and unique_condition

    elif 12 in hand:
        queen_index = hand.index(12)
        
        # Check that every other index has cards of rank 8 or lower
        queen_condition_1 = all(index == queen_index or (is_valid_rank(card) and card <= 8) for index, card in enumerate(hand))
        
        queen_condition_2 = (12 in hand) and (9 in hand) and all((is_valid_rank(card) and card <= 5) for card in hand if card not in {12, 9})

        unique_condition = len(set(hand)) == 4
        
        return (queen_condition_1 or queen_condition_2) and unique_condition

    else:
        # If there is neither King nor Queen, check if the hand has exactly 4 unique cards
        return len(set(hand)) == 4
def generate_badugi_combinations():
    all_cards = list(range(1, 14))  # Ace to King represented by 1 to 13
    pat_badugi_combinations = []

    for combo in combinations(all_cards, 4):
        hand = combo
        if is_eligible_badugi(hand):
            pat_badugi_combinations.append(hand)

    return pat_badugi_combinations

def group_by_highest_card(combinations):
    grouped_combinations = {}
    for combo in combinations:
        highest_card = max(combo)
        if highest_card not in grouped_combinations:
            grouped_combinations[highest_card] = [combo]
        else:
            grouped_combinations[highest_card].append(combo)

    return grouped_combinations

def main():
    pat_badugis = generate_badugi_combinations()
    grouped_combinations = group_by_highest_card(pat_badugis)

    cards = []
    combinations_count = []

    for card, combos in sorted(grouped_combinations.items()):
        cards.append(card)
        combinations_count.append(len(combos))

    plt.bar(cards, combinations_count, color='skyblue')
    plt.xlabel('Highest Card')
    plt.ylabel('Number of Combinations')
    plt.title('Number of Badugi Combinations by Highest Card')
    plt.show()

if __name__ == "__main__":
    main()
