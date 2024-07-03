def init_loc(pos):
	visited = (pos == (get_pos_x(), get_pos_y()))
	return [pos, visited, 0, 0, 0, 0]

def get_loc(maze, pos):
	size = maze[P]
	return maze[1 + pos[Y] + size*pos[X]]

def set_loc(maze, loc):
	pos = loc[P]
	size = maze[P]
	maze[1 + pos[Y] + size*pos[X]] = loc

def cur_loc(maze):
	return get_loc(maze, (get_pos_x(), get_pos_y()))