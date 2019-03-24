# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40} # menu
DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}

# important to order from best deals to worst
DEALS['A'*5] = 200
DEALS['BEE'] = 80
DEALS['A'*3] = 130
DEALS['B'*2] = 45

INDEX = {} # 
for i in range(len(PRICES)):
	INDEX[PRICES[i]] = i

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	# first check input is valid
	for sku in skus:
		if sku not in PRICES:
			return -1

	shopping_list = [] # list of integers for each item
	for sku in PRICES:
		shopping_list.append(skus.count(sku))

	total_cost = 0
	for deal in DEALS:
		for sku in deal: # go through all shopping items
			if deal.count(sku) > shopping_list[INDEX[sku]] # deal cannot be made

	return total_cost