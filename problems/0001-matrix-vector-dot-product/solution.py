def matrix_dot_vector(a, b):
	if not a:
		return []
	if len(a[0]) != len(b):
		return -1
	result = []

	for row in a:
		total = 0

		for x, y in zip(row, b):
			total += x * y
		
		result.append(total)

	
	return result


