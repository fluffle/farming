def reset(size):
	fieldfunc(size, harvest)
	return choose

def clear_field(size):
	fieldfunc(size, wait_harvest)
	return choose

def hay_field(size):
	fieldfunc(size, plant_hay)
	return clear_field
	
def wood_field(size):
	fieldfunc(size, plant_wood)
	return clear_field

def carrot_field(size):
	fieldfunc(size, plant_carrot)
	return clear_field
	
def maze_field(size):
	move_to(0,0)
	plant_maze()
	return solve_maze
	
def cactus_field(size):
	fieldfunc(size, plant_cactus)
	return cactus_sort