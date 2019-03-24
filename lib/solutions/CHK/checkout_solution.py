# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15}
DEALS = [] # list of deals, 1 deal is a list in format [SKU, number required, price, number have]
DEALS.append(['A', 3, 130])
DEALS.append(['B', 2, 45])


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	sku_deals = [] 
	for deal in DEALS:
		sku_deals.append(deal[0])

	# main loop
	total_cost = 0


	return total_cost
