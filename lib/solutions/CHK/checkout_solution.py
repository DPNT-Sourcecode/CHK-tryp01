

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	# assumes input skus is in format ABDACB i.e. no delimeter

	# data
	prices = {'A':50, 'B':30, 'C':20, 'D':15}
	deals = [] # list of deals, 1 deal is a list in format [SKU, number required, price]
	deals.append(['A', 3, 130])
	deals.append(['B', 2, 45])
	for sku in skus:
