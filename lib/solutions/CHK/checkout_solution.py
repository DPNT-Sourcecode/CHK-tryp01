# data
PRICES = {'A':50, 'B':30, 'C':20, 'D':15}
DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}
DEALS['A'] = [3, 130]
DEALS['B'] = [2, 45]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	total_cost = 0
	for sku in PRICES:
		n = skus.count(sku)
		if sku in DEALS:
			deal = DEALS[sku]
			n_required, price = deal
			total_cost += price * n // n_required
			total_cost += n % n_required * PRICES[sku]
		else:
			total_cost += n*PRICES[sku]

	return total_cost

print(checkout('AAABBA'))

