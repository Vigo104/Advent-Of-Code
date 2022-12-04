from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [[[int(x) for x in elf.split("-")] for elf in line.split(",")] for line in f.read().splitlines()]
	
	contains = 0
	for a, b in data:
		if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
			contains += 1
	print("Part 1:", contains)

	overlaps = 0
	for a, b in data:
		if (a[1] >= b[0] and a[0] <= b[1]):
			overlaps += 1
	print("Part 2:", overlaps)

if __name__ == "__main__":
	main()
