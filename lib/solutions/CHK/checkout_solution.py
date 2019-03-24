# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40} # menu
DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}

# important to order from best deals to worst, could add sort function to do this for us
DEALS['A'*5] = 200
DEALS['BEE'] = 80
DEALS['A'*3] = 130
DEALS['B'*2] = 45

INDEX = {} # index dictionary used for shopping_list variable, 
# format {'A':0, 'B':1, etc...}
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
	for deal in DEALS: # check each deal in order of best to worst
		make_deal = True
		while make_deal: # while loop to ensure multiple deals can be made
			for sku in deal: # go through all shopping items in deal 
				# (can have duplicates which will slow things down)
				if deal.count(sku) > shopping_list[INDEX[sku]]: 
					# if there are more elements in deal than shopping list then deal cannot be made
					make_deal = False
					break
			if make_deal:
				total_cost += DEALS[deal] # add price of deal
				for sku in deal:
					shopping_list[INDEX[sku]] -= 1

	for sku in PRICES: # remaining shopping list
		total_cost += PRICES[sku] * shopping_list[INDEX[sku]]

	return total_cost