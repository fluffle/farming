P=0
V=1
NORTH=2
EAST=3
SOUTH=4
WEST=5

X=0
Y=1

ITEMS = {
	Items.Hay: {
		'limit': 3000,
		'plant': hay_field,
	},
	Items.Wood: {
		'limit': 3000,
		'plant': wood_field,
	},
	Items.Carrot: {
		'limit': 3000,
		'plant': carrot_field,
	},
	Items.Pumpkin: {
		'limit': 8000,
		'plant': pumpkin_field,
	},
	Items.Power: {
		'limit': 1000,
		'plant': sunflower_field,
	},
	Items.Gold: {
		'limit': 3000,
		'plant': maze_field,
	},
	Items.Cactus: {
		'limit': 5000,
		'plant': cactus_field,
	},
}
main(get_world_size())