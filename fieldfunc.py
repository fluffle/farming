def fieldfunc(size, func):
	y = 0
	inc = 1
	ret = []
	for x in range(size):
		for n in range(size):
			if n > 0:
				y += inc
			move_to(x,y)
			ret.append([func(), [x,y]])
		inc = -inc
	return ret