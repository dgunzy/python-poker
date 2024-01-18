from itertools import combinations

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
    sorted_badugis = sorted(pat_badugis, key=lambda x: (x[3], x[2], x[1], x[0]))

    grouped_combinations = group_by_highest_card(sorted_badugis)

    for card, combos in sorted(grouped_combinations.items()):
        new_combos = []
        for combo in combos:
            new_combo = ''.join(str(c) if c not in {1, 11, 12, 13} else 'A' if c == 1 else 'J' if c == 11 else 'Q' if c == 12 else 'K' for c in combo)
            new_combos.append(new_combo)
        
        print(f'{card}: {", ".join(new_combos)} ({len(combos)} combinations)')


if __name__ == "__main__":
    main()
