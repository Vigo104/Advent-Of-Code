from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def priority(x: str):
	return ord(x)-ord("a")+1 if x.islower() else ord(x)-ord("A")+27

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = f.read().splitlines()
    
	priorities = []
	for rucksack in data:
		first = rucksack[:int(len(rucksack)/2)]
		second = rucksack[int(len(rucksack)/2):]
		for letter in first:
			if letter in second:
				priorities.append(priority(letter))
				break
	
	print("Part 1:", sum(priorities))

	priorities = []
	for i in range(0, len(data), 3):
		for letter in data[i]:
			if letter in data[i+1]:
				if letter in data[i+2]:
					priorities.append(priority(letter))
					break
	
	print("Part 2:", sum(priorities))

if __name__ == "__main__":
	main()
