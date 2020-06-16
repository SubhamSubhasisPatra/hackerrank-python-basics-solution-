def avg(a,*args):
	total_sum = 0
	total_lenght = len(args)
	if total_lenght == 0:
		return a
	else:
		for x in args:
			total_sum += x
	return (total_sum + a)/(total_lenght + 1)
