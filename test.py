import numpy as np
import random

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
		for x in range(10000):
			#newPiles=np.random.randint(2,size=10)
			newPiles=[1 if x+random.gauss(0,1)>=0.5 else 0 for x in self.Piles]
			if self.getCost(self.Piles)>self.getCost(newPiles):
				self.Piles=newPiles
				print(self.getCost(self.Piles))
			if self.getCost(self.Piles)==abs(55-(self.A+self.B)): break

		print(self.Piles)
		print(self.getCost(self.Piles))

	def setAB(self,A,B):
		self.A=A
		self.B=B



if __name__== "__main__":
	one_to_one=OnetoOne(40,15)
	#print(new.getCost(new.Piles))
	one_to_one.simulation()



	