from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [x.split(" ") for x in f.read().splitlines()]
    
	directories = defaultdict(int)
	currDir = []
	for line in data:
		if line[0] == "$" and line[1] == "cd":
			if line[2] == "..":
				currDir.pop()
			else:
				currDir.append(line[2])
		elif line[0].isdigit():
			directories[tuple(currDir)] += int(line[0])
		else:
			directories[tuple(currDir)] += 0

	directoriesCopy = directories.copy()
	for x in directories.keys():
		for y in directories.keys():
			if str(y).count(str(x)[:-1]) != 0 and str(x) != str(y):
				directoriesCopy[x] += directories[y]
	directories = directoriesCopy.copy()
	
	result = sum(x for x in directories.values() if x <= 100000)
	print("Part 1:", result)

	neededSpace = 30000000 - (70000000 - directories[('/',)])
	print("Part 2:", min(x for x in directories.values() if x >= neededSpace))

if __name__ == "__main__":
	main()
