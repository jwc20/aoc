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
	

	dict = {}


	for x in data_a:
		print(dict)
		i=0
		while i < len(data_b) - 1:
			if x == data_b[i]:
				print(type(dict[x]))
				dict[x] += 1
				data_b.pop(i)
			else:
				dict[x] = 1

			i+=1

	print(dict)
	return



if "__main__" == __name__:
	main()
