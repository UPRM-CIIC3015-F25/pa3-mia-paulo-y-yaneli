from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    rankValue = {
        Rank.TWO: 2, Rank.THREE: 3, Rank.FOUR: 4, Rank.FIVE: 5,
        Rank.SIX: 6, Rank.SEVEN: 7, Rank.EIGHT: 8, Rank.NINE: 9,
        Rank.TEN: 10, Rank.JACK: 11, Rank.QUEEN: 12,
        Rank.KING: 13, Rank.ACE: 14
    }

    rankCount = {}
    for r in ranks:
        rankCount[r] = rankCount.get(r, 0) + 1

    counts = sorted(rankCount.values(), reverse =True)

    suitCounts = {}
    for s in suits:
        suitCounts[s] = suitCounts.get(s, 0) + 1

    isFlush = max(suitCounts.values()) >= 5
    uniqueRanks = sorted({rankValue[r] for r in ranks})
    straight = False

    if 14 in uniqueRanks:
        uniqueRanks_with_A1 = sorted(uniqueRanks + [1])
    else:
        uniqueRanks_with_A1 = uniqueRanks

    for i in range(len(uniqueRanks_with_A1) - 4):
        sequence = uniqueRanks_with_A1[i:i + 5]
        if sequence[-1] - sequence[0] == 4 and len(sequence) == len(set(sequence)):
            straight = True
            break

    if isFlush and straight:
        return "Straight Flush"

    if 4 in counts:
        return "Four of a Kind"

    if 3 in counts and 2 in counts:
        return "Full House"

    if isFlush:
        return "Flush"

    if straight:
        return "Straight"

    if 3 in counts:
        return "Three of a Kind"

    if counts.count(2) == 2:
        return "Two Pair"

    if 2 in counts:
        return "One Pair"

    return "High Card"


