import numpy as np
import random
import itertools as it

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

		print(self.Piles)
		print(self.getCost(self.Piles))
		for x in range(100):
			#newPiles=np.random.randint(2,size=10)
			newPiles=[1 if x+random.gauss(0,1)>=0.5 else 0 for x in self.Piles]
			if self.getCost(self.Piles)>self.getCost(newPiles):
				self.Piles=newPiles
				print(self.getCost(self.Piles))
			if self.getCost(self.Piles)==abs(55-(self.A+self.B)): break #czy tu napewno abs?

		print(self.Piles)
		print(self.getCost(self.Piles))

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

		print(self.Piles)
		print(self.getCost(self.Piles))


from timeit import default_timer as timer


if __name__== "__main__":
	one_to_one = OnetoOne(42, 17)
	#print(new.getCost(new.Piles))
	start = timer()
	one_to_one.simulation()
	t = timer() - start
	print(("%s : " + "%0.3g" + " seconds") % ("One_to_one",t))
	full_search = FullSearch(42, 17)
	start = timer()
	full_search.simulation()
	t = timer() - start
	print(("%s : " + "%0.3g" + " seconds") % ("FullSearch", t))





	