# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15}
DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}
DEALS['A'] = [3, 130]
DEALS['B'] = [2, 45]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	print('')
	total_cost = 0
	for sku in PRICES:
		n = skus.count(sku) # number of elements
		if sku in DEALS:
			deal = DEALS[sku] 
			n_required, deal_price = deal
			total_cost += deal_price * n // n_required
			print(1, deal_price * n // n_required)
			total_cost += (n % n_required) * PRICES[sku]
			print(2, (n % n_required) * PRICES[sku])
		else:
			total_cost += n*PRICES[sku]
			print(3, n*PRICES[sku])

	return total_cost

print(checkout('AA'))

