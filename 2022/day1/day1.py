from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = f.read().split("\n\n")

	totCalories = []
	for elf in data:
		calories = sum(map(int, elf.splitlines()))
		totCalories.append(calories)

	print("Part 1:", max(totCalories))

	totCalories = sorted(totCalories)
	print("Part 2:", sum(totCalories[-3:]))

if __name__ == "__main__":
	main()
