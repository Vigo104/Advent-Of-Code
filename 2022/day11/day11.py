from pathlib import Path
import copy

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [x.splitlines() for x in f.read().split("\n\n")]
    
	for i, monkey in enumerate(data):
		for j, line in enumerate(monkey):
			if j == 0:
				data[i][j] = int(data[i][j][:-1][-1:])
			elif j == 1:
				s = data[i][j].split(":")
				data[i][j] = [*map(int, s[1].split(","))]
			elif j == 2:
				s = data[i][j].split(" ")
				s = s[-2:]
				data[i][j] = [s[0], s[1]]
			elif j == 3:
				s = data[i][j].split(" ")
				data[i][j] = int(s[-1:][0])
			elif j == 4:
				data[i][j] = int(data[i][j][-1:][0])
			elif j == 5:
				data[i][j] = int(data[i][j][-1:][0])

	dataCopy = copy.deepcopy(data)
	monkeyBusiness = [0 for _ in range(len(data))]
	for monkey in data * 20:
		for n in monkey[1]:
			monkeyBusiness[monkey[0]] += 1
			if monkey[2][1].isdigit():
				if monkey[2][0] == "+":
					n += int(monkey[2][1])
				elif monkey[2][0] == "*":
					n *= int(monkey[2][1])
			else:
				n *= n
			n = n//3
			if n % monkey[3] == 0:
				data[monkey[4]][1].append(n)
			else:
				data[monkey[5]][1].append(n)
		data[monkey[0]][1].clear()
	result = sorted(set(monkeyBusiness), reverse=True)
	print("Part 1:", result[0] * result[1])

	data = copy.deepcopy(dataCopy)
	magicNumber = 1
	for monkey in data:
		magicNumber *= monkey[3]
	monkeyBusiness = [0 for _ in range(len(data))]
	for monkey in data * 10000:
		for n in monkey[1]:
			monkeyBusiness[monkey[0]] += 1
			if monkey[2][1].isdigit():
				if monkey[2][0] == "+":
					n += int(monkey[2][1])
				elif monkey[2][0] == "*":
					n *= int(monkey[2][1])
			else:
				n *= n
			n %= magicNumber
			if n % monkey[3] == 0:
				data[monkey[4]][1].append(n)
			else:
				data[monkey[5]][1].append(n)
		data[monkey[0]][1].clear()
	result = sorted(set(monkeyBusiness), reverse=True)
	print("Part 2:", result[0] * result[1])

if __name__ == "__main__":
	main()
