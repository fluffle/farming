def sort(lst, fn):
	# insertion sort, ish
	for i in range(1, len(lst)):
		for j in range(0, i):
			if fn(lst[i]) < fn(lst[j]):
				itm = lst.pop(i)
				lst.insert(j, itm)
				
def by_self(itm):
	return itm