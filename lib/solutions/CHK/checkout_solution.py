# data
PRICES =  {'A':50,    
			'B':30,    
			'C':20,    
			'D':15,    
			'E':40,    
			'F':10,
			'G':20, 
			'H':10,
			'I':35, 
			'J':60, 
			'K':70, 
			'L':90, 
			'M':15, 
			'N':40, 
			'O':10, 
			'P':50,  
			'Q':30,  
			'R':50, 
			'S':20, 
			'T':20, 
			'U':40,  
			'V':50,  
			'W':20, 
			'X':17, 
			'Y':20, 
			'Z':21, 
	}

INDEX = {} # index dictionary used for shopping_list variable, 
# format {'A':0, 'B':1, etc...}
i=0
for sku in PRICES:
	INDEX[sku] = i
	i+=1

DEALS = {} # dictionary of deals, 1 deal is a list in format {SKU: [number required, price]}
# will be ordered later
DEALS['A'*3] = 130
DEALS['A'*5] = 200
DEALS['B'*2] = 45
DEALS['BEE'] = 80
DEALS['F'*3] = 20
DEALS['H'*5] = 45
DEALS['H'*10] = 80
DEALS['K'*2] = 150
DEALS['NNNM'] = 120
DEALS['P'*5] = 200
DEALS['Q'*3] = 80
DEALS['R'*3+'Q'] = 150
DEALS['U'*4] = 120
DEALS['V'*2] = 90
DEALS['V'*3] = 130

GROUP_DEALS = [] # elements are a list in format: [SKUs, n_elements, price]
GROUP_DEALS.append(['STXYZ', 3, 45])

# analyse group deals by creating a combination of n deals
# Warning - having a large number of deals could slow the initialising down considerably 
for group_deal in GROUP_DEALS:
	skus, n_elements, price = group_deal
	indexing = []  # used to keep tabs on things
	for i in range(n_elements):
		indexing.append(0) # should be list of zeros length n_elements e.g. [0,0,0]
	for i in range(n_elements**len(skus)): # loop over all possible group combinations
		carry = True
		for j in range(n_elements):
			if carry:
				indexing[j]+=1
				if indexing[j] == len(skus):
					indexing[j] -= len(skus)
				else:
					carry = False
			else:
				break
		sku_code = skus[indexing[0]] + skus[indexing[1]] + skus[indexing[2]]
		DEALS[sku_code] = price



def organise_deals(deals):
	# organises deals based on amount saved, 
	# input - dictionary in same format as 'DEALS' var defined above
	# returns - dictionary in same format but organised by how much price is saved
	# first analyse data and put into a list
	organised_deals = {}
	deal_list = [] # in format [sku code, price, amount saved] for sorting later
	for deal in deals: # deal is a string desribing sku code for deal
		price = deals[deal]
		raw_price = 0 # amount it would cost without deal
		for sku in deal:
			raw_price += PRICES[sku]
		deal_list.append([deal, price, raw_price - price])
	# now sort analysed data
	n_deals = len(deal_list)
	for i in range(n_deals):
		best_deal = deal_list[0]
		for deal_info in deal_list: #[sku code, price, amount saved]
			if deal_info[2] > best_deal[2]: # if it is a better deal
				best_deal = deal_info
		organised_deals[best_deal[0]] = best_deal[1]
		deal_list.remove(best_deal)
	return organised_deals


DEALS = organise_deals(DEALS) 

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



