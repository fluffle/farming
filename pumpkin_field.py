def pumpkin_field(size):
	fieldfunc(size, plant_pumpkin)
	return replant_pumpkins

def replant_pumpkins(size):
	ps = fieldfunc(size, maybe_replant)
	tofix = []
	for p in ps:
		if not p[0]:
			tofix.append(p[1])
	while len(tofix) > 0:
		tofix = replant_list(tofix)
	harvest()
	return choose

def maybe_replant():
	if not get_entity_type():
		plant_pumpkin()
	return can_harvest()
			
def replant_list(totest):
	tofix = []
	for pos in totest:
		move_to(pos[0], pos[1])
		if not maybe_replant():
			tofix.append(pos)
	return tofix