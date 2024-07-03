def sunflower_field(size):
	fieldfunc(size, plant_sunflower)
	return harvest_sunflowers
	
def harvest_sunflowers(size):
	remaining = fieldfunc(size, measure)
	ordered = []
	while len(remaining) > 0:
		remaining, ordered = list_max(remaining, ordered)
	for pos in ordered:
		move_to(pos[0], pos[1])
		harvest()
	return choose

def list_max(totest, ordered):
	remaining = []
	max_size = max(totest)
	for flower in totest:
		if flower[0] == max_size[0]:
			ordered.append(flower[1])
		else:
			remaining.append(flower)
	return remaining, ordered