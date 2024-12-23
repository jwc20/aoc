"""
https://adventofcode.com/2024/day/1/input
"""

filename = "./data.txt"

def main():
	f = open(filename, 'r')
	lines = f.readlines()

	data_a, data_b = [], []

	for line in lines:
		#print(line)
		pair = line.split("   ")
		# print(pair, pair[0], pair[1])
		data_a.append(int(pair[0]))
		data_b.append(int(pair[1].replace("\n", "")))
	
	data_a.sort()
	data_b.sort()

	i = 0
	distances = []

	while i < len(data_a):
		distances.append(abs(data_a[i] - data_b[i]))
		i+=1

	# print(distances)

	print(sum(distances))

	return sum(distances)




if "__main__" == __name__:
	main()
