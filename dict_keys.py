def keys(d):
	ks = []
	for k in d:
		ks.append(k)
	return ks
	
def sort_keys(d, fn):
	ks = keys(d)
	sort(ks, fn)
	return ks
