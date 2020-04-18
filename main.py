from algorithms import OnetoOne, FullSearch
from test import test_1

def read_data(x):
	""""Read from console A and B pile """
	invalid = True
	while invalid :
		A = int(input("Wpisz wartość dla pierwszej kupki (1-55)"))
		if A >= 1 & A <= 55:
			x.append(A)
			invalid = False
	invalid = True
	while invalid :
		B = int(input("Wpisz wartość dla drugiej kupki (1-55) "))
		if B >= 1 & B <= 55:
			x.append(B)
			invalid = False


if __name__== "__main__":

	one_to_one=OnetoOne(0, 0)
	full_search=FullSearch(0, 0)
	piles =[]

	read_data(piles)
	one_to_one.setAB(piles[0], piles[1])
	full_search.setAB(piles[0], piles[1])
	cost_o = one_to_one.simulation()
	cost_f = full_search.simulation()
	if cost_f == cost_o :
		print("The same cost for solutions : {}".format(cost_f) )
		print('Solution one_to_one {0}'.format(one_to_one.get_result()))
		print('Solution full_search {0}'.format(full_search.get_result()))

	test_1(OnetoOne(0, 0), FullSearch(0, 0))




	