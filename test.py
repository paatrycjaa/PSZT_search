import numpy as np

class OnetoOne:
	def __init__(self, A, B):
		self.A=A
		self.B=B
		self.CardsValues=[x for x in range(1,11)]
		self.Piles=np.random.randint(2,size=10) # 0 - on A pile || 1 - on B pile

	def getCost(self,PilesVal):

		self.A_pile=[x for x,y in zip(self.CardsValues, PilesVal)if y==0]
		self.B_pile=[x for x,y in zip(self.CardsValues, PilesVal)if y==1]
		
		cost= abs(sum(self.A_pile)-self.A)+abs(sum(self.B_pile)-self.B)
		return cost

	def simulation(self):

		print(self.Piles)
		print(self.getCost(self.Piles))
		for x in range(10000):
			newPiles=np.random.randint(2,size=10)
			if self.getCost(self.Piles)>self.getCost(newPiles):
				self.Piles=newPiles
				print(self.getCost(self.Piles))

		print(self.Piles)
		print(self.getCost(self.Piles))



if __name__== "__main__":
	new=OnetoOne(30,25)
	#print(new.getCost(new.Piles))
	new.simulation()



	