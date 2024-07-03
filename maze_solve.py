P=0
V=1
NORTH=2
EAST=3
SOUTH=4
WEST=5

X=0
Y=1

def init_maze(size):
	maze = [size]
	for x in range(size):
		for y in range(size):
			maze.append(init_loc((x,y)))
	return maze

def solve_maze(size):
	m = init_maze(size)
	state = unseen_state([])
	while m:
		state, m = state(m)
	return choose
		
def unseen_state(visited):
	def state(maze):
		dest = first_untaken(maze)
		if not dest:
			dest = closest_unseen(maze)
		return flood_state(dest, visited), maze
	return state
	
def flood_state(dest, visited):
	def state(maze):
		loc = cur_loc(maze)
		visited.append(loc[P])
		dirs = possible_dirs(maze, loc)
		for dir in dirs:
			new_pos = pos_in_dir(loc[P], dir)
			if not new_pos or new_pos in visited:
				continue
			if move_one(maze, dir):
				return check_state(dest, visited), maze
		return backtrack_state(dest, visited), maze
	return state

def check_state(dest, visited):
	def state(maze):
		if get_entity_type() == Entities.Treasure:
			harvest()
			return None, None
		if cur_loc(maze) == dest:
			return unseen_state(visited), maze
		return flood_state(dest, visited), maze
	return state

def backtrack_state(dest, visited):
	def state(maze):
		loc = cur_loc(maze)
		for i in range(len(visited)):
			if visited[i] == loc[P]:
				break
		if i == 0:
			return unseen_state(visted), maze
		prev = visited[i-1]
		move_to(prev[X], prev[Y])
		return flood_state(dest, visited), maze
	return state

solve_maze(6)