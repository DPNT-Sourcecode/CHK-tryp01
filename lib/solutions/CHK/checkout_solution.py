# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15} # menu
DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}
DEALS['A'] = [3, 130]
DEALS['B'] = [2, 45]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	# check input is valid
	for sku in skus:
		if sku not in PRICES:
			return -1

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
