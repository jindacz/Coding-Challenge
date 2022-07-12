# You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

# You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

# You will do the following steps repeatedly until all cards are revealed:

# Take the top card of the deck, reveal it, and take it out of the deck.
# If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
# If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.

# Note that the first entry in the answer is considered to be the top of the deck.

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        index = collections.deque(range(n))
        res = [None] * n

        for card in sorted(deck):
            # place first element, use dequeue method
            res[index.popleft()] = card
            if index:
                # simulate how cards are drawn, reveal fist, and put second to last
                index.append(index.popleft()) 
        return res