# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15}
DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}
DEALS['A'] = [3, 130]
DEALS.append(['B', 2, 45])


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	sku_deals = [] # will be a list of all SKUs in a deal
	for deal in DEALS:
		sku_deals.append(deal[0])

	total_cost = 0
	for sku in PRICES:
		n = skus.count(sku)
		if sku in sku_deals:
			pass
		else:


	return total_cost
