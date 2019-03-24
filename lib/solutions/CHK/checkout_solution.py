# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15}
DEALS = [] # list of deals, 1 deal is a list in format [SKU, number required, price, number have]
DEALS.append(['A', 3, 130])
DEALS.append(['B', 2, 45])


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	sku_deals = '' # will be a list of all SKUs in a deal
	for deal in DEALS:
		sku_deals = sku_deals + deal[0]

	total_cost = 0
	for sku in PRICES:
		if SKU in sku_deals:


	return total_cost
