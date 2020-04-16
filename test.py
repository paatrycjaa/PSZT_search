import numpy as np
import random
import itertools as it
from timeit import default_timer as timer

class OnetoOne:
	def __init__(self, A, B):
		self.A=A 				#parameter for A pile
		self.B=B 				#parameter for B pile
		self.CardsValues=[x for x in range(1,11)]	#values of cards SUM is 55
		self.Piles=np.random.randint(2,size=10) 	# 0 - on A pile || 1 - on B pile

	def getCost(self,PilesVal):

		self.A_pile=[x for x,y in zip(self.CardsValues, PilesVal)if y==0]
		self.B_pile=[x for x,y in zip(self.CardsValues, PilesVal)if y==1]
		
		cost= abs(sum(self.A_pile)-self.A)+abs(sum(self.B_pile)-self.B)
		return cost

	def simulation(self):
		
		for x in range(1024):
			newPiles=[1 if x+random.gauss(0,1)>=0.5 else 0 for x in self.Piles]
			if self.getCost(self.Piles)>self.getCost(newPiles):
				self.Piles=newPiles
			if self.getCost(self.Piles)==abs(55-(self.A+self.B)): break

		return self.getCost(self.Piles)

	def setAB(self,A,B):
		self.A=A
		self.B=B


class FullSearch:
	def __init__(self, A, B):
		self.A = A 				#parameter for A pile
		self.B = B 				#parameter for B pile
		self.CardsValues = [x for x in range(1,11)]	#values of cards SUM is 55
		self.Piles = None

	def getCost(self, PilesVal):
		self.A_pile = [x for x, y in zip(self.CardsValues, PilesVal) if y == 0]
		self.B_pile = [x for x, y in zip(self.CardsValues, PilesVal) if y == 1]
		cost = abs(sum(self.A_pile) - self.A) + abs(sum(self.B_pile) - self.B)
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

	def setAB(self,A,B):
		self.A=A
		self.B=B


def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail


if __name__== "__main__":

	one_to_one=OnetoOne(0,0)
	full_search=FullSearch(0,0)
	one_results=[]
	full_results=[]

	start_one=timer()
	for x in sum_to_n(55,2):
		one_to_one.setAB(x[0],x[1])
		one_results.append(one_to_one.simulation())
	t_one = timer() - start_one

	start_full=timer()
	for x in sum_to_n(55,2):
		full_search.setAB(x[0],x[1])
		full_results.append(full_search.simulation())
	t_full = timer() - start_full

	print(("%s : " + "%0.3g" + " seconds") % ("One_to_one",t_one))
	print(("%s : " + "%0.3g" + " seconds") % ("FullSearch",t_full))
	print("Are all results the same: " + str(one_results==full_results))

	