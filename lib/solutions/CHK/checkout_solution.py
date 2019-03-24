# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40} # menu
DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}

# important to order from best deals to worst
DEALS['A'*5] = 200
DEALS['BEE'] = 80
DEALS['A'*3] = 130
DEALS['B'*2] = 45

index = {} # 
for i in range(len(PRICES)):
	index[PRICES[i]] = i

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
	for sku in PRICES:
		n = skus.count(sku) # number of elements
		if sku in DEALS:
			deal = DEALS[sku] 
			n_required, deal_price = deal
			total_cost += deal_price * (n // n_required) # number of deals
			total_cost += (n % n_required) * PRICES[sku] # remainder
		else:
			total_cost += n*PRICES[sku] # no deals

	return total_cost






