def move_one(maze, dir):
	old_loc = cur_loc(maze)
	if old_loc[D(dir)] == -1:
		# Can't go this way already.
		return False
	new_pos = pos_in_dir(old_loc[P], dir)
	if not new_pos:
		# out of bounds
		old_loc[D(dir)] = -1
		set_loc(maze, old_loc)
		return False
	new_loc = get_loc(maze, new_pos)
	moves = old_loc[D(dir)]
	ok = move(dir)
	if ok:
		new_loc[V] = True
		old_loc[D(dir)] = old_loc[D(dir)] + 1
	else:
		old_loc[D(dir)] = -1
		new_loc[O(dir)] = -1
	set_loc(maze, old_loc)
	set_loc(maze, new_loc)
	return ok