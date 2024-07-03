def restock_tanks():
	while (
		num_items(Items.Wood) > 50 and
		(num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)) < 200
	):
		trade(Items.Empty_Tank)
		