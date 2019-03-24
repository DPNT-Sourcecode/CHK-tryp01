# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	# data
	prices = {'A':50, 'B':30, 'C':20, 'D':15}
	deals = [] # list of deals, 1 deal is a list in format [SKU, number required, price]
	deals.append(['A', 3, 130, 0])
	deals.append(['B', 2, 45, 0])

	# main loop
	total_cost = 0
	for sku in skus: # SKU is 1 character
		if sku in prices: # hopefully will avoid delimiter which I do not know

	return total_cost
