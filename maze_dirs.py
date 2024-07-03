def D(dir):
	# NO DICTS IS MEAN
	if dir == North:
		return NORTH
	if dir == East:
		return EAST
	if dir == South:
		return SOUTH
	if dir == West:
		return WEST

def O(dir):
	if dir == North:
		return SOUTH
	if dir == East:
		return WEST
	if dir == South:
		return NORTH
	if dir == West:
		return EAST

def R(dir):
	if dir == North:
		return South
	if dir == East:
		return West
	if dir == South:
		return North
	if dir == West:
		return East
			
def bounds_check(pos):
	if (pos[X] >= get_world_size() or
		pos[X] < 0 or
		pos[Y] >= get_world_size() or
		pos[Y] < 0):
		return None
	return pos

def pos_in_dir(pos, dir):
	if dir == North:
		return bounds_check((pos[X], pos[Y]+1))
	if dir == East:
		return bounds_check((pos[X]+1, pos[Y]))
	if dir == South:
		return bounds_check((pos[X], pos[Y]-1))
	if dir == West:
		return bounds_check((pos[X]-1, pos[Y]))

