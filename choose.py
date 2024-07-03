def main(size):
	state = reset
	while True:
		state = state(size)

def choose(size):
	restock_tanks()
	# ensure minimum levels
	for itm in ITEMS:
		ITEMS[itm]['count'] = num_items(itm)
		v = ITEMS[itm]
		if v['count'] < v['limit']:
			return v['plant']
	# otherwise grow the thing we have least of
	def by_count(k):
		return ITEMS[k]['count'] - ITEMS[k]['limit']
	ks = sort_keys(ITEMS, by_count)
	return ITEMS[ks[0]]['plant']