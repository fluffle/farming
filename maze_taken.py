def all_untaken(maze, loc):
	dirs = []
	if loc[NORTH] == 0:
		dirs.append(North)
	if loc[EAST] == 0:
		dirs.append(East)
	if	loc[SOUTH] == 0:
		dirs.append(South)
	if loc[WEST] == 0:
		dirs.append(West)
	return dirs

def first_untaken(maze):
	loc = cur_loc(maze)
	all = all_untaken(maze, loc)
	if len(all) == 0:
		return None
	return all[0]

def distance(pos1, pos2):
	return (
		(pos2[X]-pos1[X])**2 +
		(pos2[Y]-pos1[Y])**2
	) ** 0.5 

def dist_to(loc):
	return distance(
		(get_pos_x(), get_pos_y()),
		loc[P])

def closest_unseen(maze):
	locs = []
	for loc in maze[1:]:
		if not loc[V]:
			locs.append(loc)
	# precalculate distances
	dists = []
	for loc in locs:
		dists.append([dist_to(loc), loc])
	def by_dist(d):
		return d[0]
	sort(dists, by_dist)
	print("unseen: ", dists[0][1])
	return dists[0][1]

def possible_dirs(maze, loc):
	# bias towards untaken dirs
	dirs = all_untaken(maze, loc)
	if loc[NORTH] > 0:
		dirs.append(North)
	if loc[EAST] > 0:
		dirs.append(East)
	if	loc[SOUTH] > 0:
		dirs.append(South)
	if loc[WEST] > 0:
		dirs.append(West)
	return dirs