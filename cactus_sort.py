def cactus_sort(size):
	swapped = False
	for x in range(size):
		for y in range(size):
			move_to(x,y)
			if x > 0:
				swapped = cactus_swap(West) or swapped
			if y > 0:
				swapped = cactus_swap(South) or swapped
	if swapped:
		return cactus_sort
	harvest()
	return choose

def cactus_swap(dir):
	if measure() < measure(dir):
		swap(dir)
		return True
	return False