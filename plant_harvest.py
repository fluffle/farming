def water():
	if get_water() < 0.4 and num_items(Items.Water_Tank) > 0:
		use_item(Items.Water_Tank)

def wait_harvest():
	tries = 2
	while not can_harvest() and tries > 0:
		do_a_flip()
		tries -= 1
	harvest()

def plant_hay():
	plant(Entities.Grass)

def plant_wood():
	if get_pos_x() % 2 == get_pos_y() % 2:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def plant_carrot():
	plant_seed(Items.Carrot_Seed, Entities.Carrots)

def plant_sunflower():
	plant_seed(Items.Sunflower_Seed, Entities.Sunflower)

def plant_pumpkin():
	plant_seed(Items.Pumpkin_Seed, Entities.Pumpkin)

def plant_cactus():
	plant_seed(Items.Cactus_Seed, Entities.Cactus)

def plant_seed(seed, entity):
	if num_items(seed) < 1:
		trade(seed)
	if get_ground_type() != Grounds.Soil:
		till()
	water()
	plant(entity)
	
def plant_maze():
	plant(Entities.Bush)
	while not can_harvest():
		do_a_flip()
	while get_entity_type() != Entities.Hedge:
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
