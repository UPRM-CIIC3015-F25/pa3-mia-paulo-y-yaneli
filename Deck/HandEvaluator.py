from Cards.Card import Card, Rank

def evaluate_hand(hand: list[Card]):

    # Collect ranks and suits
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    # Rank numerical values
    rankValue = {
        Rank.TWO: 2, Rank.THREE: 3, Rank.FOUR: 4, Rank.FIVE: 5,
        Rank.SIX: 6, Rank.SEVEN: 7, Rank.EIGHT: 8, Rank.NINE: 9,
        Rank.TEN: 10, Rank.JACK: 11, Rank.QUEEN: 12,
        Rank.KING: 13, Rank.ACE: 14
    }

    rankCount = {}
    for r in ranks:
        rankCount[r] = rankCount.get(r, 0) + 1

    counts = sorted(rankCount.values(), reverse=True)

    suitCounts = {}
    for s in suits:
        suitCounts[s] = suitCounts.get(s, 0) + 1

    flushSuit = None
    for s, c in suitCounts.items():
        if c >= 5:
            flushSuit = s
            break

    isFlush = flushSuit is not None

    uniqueRanks = sorted({rankValue[r] for r in ranks})

    if 14 in uniqueRanks:
        uniqueRanks_with_A1 = sorted(uniqueRanks + [1])
    else:
        uniqueRanks_with_A1 = uniqueRanks

    straight = False
    for i in range(len(uniqueRanks_with_A1) - 4):
        seq = uniqueRanks_with_A1[i:i + 5]
        if seq[-1] - seq[0] == 4 and len(seq) == len(set(seq)):
            straight = True
            break

    straightFlush = False
    if flushSuit:

        flush_ranks = [rankValue[c.rank] for c in hand if c.suit == flushSuit]

        flush_ranks = sorted(set(flush_ranks))

        if 14 in flush_ranks:
            flush_ranks_low = sorted(flush_ranks + [1])
        else:
            flush_ranks_low = flush_ranks

        for i in range(len(flush_ranks_low) - 4):
            seq = flush_ranks_low[i:i + 5]
            if seq[-1] - seq[0] == 4 and len(seq) == len(set(seq)):
                straightFlush = True
                break

    if straightFlush:
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


