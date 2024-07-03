def move_to(x, y):
	sz = get_world_size() - 1
	if x > sz:
		x = sz
	if y >= sz:
		y = sz
	while x > get_pos_x():
		move(East)
	while x < get_pos_x():
		move(West)
	while y > get_pos_y():
		move(North)
	while y < get_pos_y():
		move(South)


	