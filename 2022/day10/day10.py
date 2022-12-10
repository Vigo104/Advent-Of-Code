from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [x.split() for x in f.read().splitlines()]
	
	x = 1
	execute, add = True, False
	cycle = -1
	signalStrength = []
	for i in range(220):
		if (i+21)%40 == 0:
				signalStrength.append((i+1) * x)
		if execute:
			cycle += 1
			if cycle >= len(data):
				cycle -= len(data)
			if data[cycle][0] == "addx":
				add = True
				execute = False
				continue
		if add:
			x += int(data[cycle][1])
			add = False
			execute = True
	print("Part 1:", sum(signalStrength))

	x = 1
	execute, add = True, False
	cycle = -1
	iPixel = -1
	iRow = 0
	sprite = [["" for _ in range(40)] for _ in range(6)]
	for i in range(240):
		iPixel += 1
		if iPixel >= len(sprite[0]):
			iPixel -= len(sprite[0])
			iRow += 1
		if x-1 <= iPixel <= x+1:
			sprite[iRow][iPixel] = "██" # "#"
		else:
			sprite[iRow][iPixel] = "░░" # "."
		if execute:
			cycle += 1
			if cycle >= len(data):
				cycle -= len(data)
			if data[cycle][0] == "addx":
				add = True
				execute = False
				continue
		if add:
			x += int(data[cycle][1])
			add = False
			execute = True
	for s in sprite:
		for c in s:
			print(c, end='')
		print()
	print("Part 2: RBPARAGF")

if __name__ == "__main__":
	main()
