import numpy as np
import random
import itertools as it


class OnetoOne:
    def __init__(self, A, B):
        self.A = A  # parameter for A pile
        self.B = B  # parameter for B pile
        self.CardsValues = [x for x in range(1, 11)]  # values of cards SUM is 55
        self.Piles = np.random.randint(2, size=10)  # 0 - on A pile || 1 - on B pile

    def getCost(self, PilesVal):

        A_pile = [x for x, y in zip(self.CardsValues, PilesVal) if y == 0]
        B_pile = [x for x, y in zip(self.CardsValues, PilesVal) if y == 1]

        cost = abs(sum(A_pile) - self.A) + abs(sum(B_pile) - self.B)
        return cost

    def simulation(self):

        for x in range(1024):
            newPiles = [1 if x + random.gauss(0, 1) >= 0.5 else 0 for x in self.Piles]
            if self.getCost(self.Piles) > self.getCost(newPiles):
                self.Piles = newPiles
            if self.getCost(self.Piles) == abs(55 - (self.A + self.B)): break

        return self.getCost(self.Piles)

    def setAB(self, A, B):
        self.A = A
        self.B = B

    def get_result(self):
        A_pile = [x for x, y in zip(self.CardsValues, self.Piles) if y == 0]
        B_pile = [x for x, y in zip(self.CardsValues, self.Piles) if y == 1]
        return [A_pile,B_pile]


class FullSearch:
    def __init__(self, A, B):
        self.A = A  # parameter for A pile
        self.B = B  # parameter for B pile
        self.CardsValues = [x for x in range(1, 11)]  # values of cards SUM is 55
        self.Piles = []

    def getCost(self, PilesVal):
        A_pile = [x for x, y in zip(self.CardsValues, PilesVal) if y == 0]
        B_pile = [x for x, y in zip(self.CardsValues, PilesVal) if y == 1]
        cost = abs(sum(A_pile) - self.A) + abs(sum(B_pile) - self.B)
        return cost

    def simulation(self):
        permutation_with_replacment = [x for x in it.product([1, 0], repeat=10)]
        cost = 1000
        for combination in permutation_with_replacment:
            new_cost = self.getCost(combination)
            if cost > new_cost:
                cost = new_cost
                self.Piles = combination

        return self.getCost(self.Piles)

    def setAB(self, A, B):
        self.A = A
        self.B = B

    def get_result(self):
        A_pile = [x for x, y in zip(self.CardsValues, self.Piles) if y == 0]
        B_pile = [x for x, y in zip(self.CardsValues, self.Piles) if y == 1]
        return [A_pile,B_pile]
