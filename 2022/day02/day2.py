from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

# Rock     A X lose
# Paper    B Y draw
# Scissors C Z win

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = f.read().splitlines()
    
	for i, x in enumerate(data):
		data[i] = x.split()

	score = 0
	for match in data:
		if match[1] == 'X' and match[0] == 'A':
			score += 1 + 3
		elif match[1] == 'X' and match[0] == 'B':
			score += 1 + 0
		elif match[1] == 'X' and match[0] == 'C':
			score += 1 + 6
		elif match[1] == 'Y' and match[0] == 'A':
			score += 2 + 6
		elif match[1] == 'Y' and match[0] == 'B':
			score += 2 + 3
		elif match[1] == 'Y' and match[0] == 'C':
			score += 2 + 0
		elif match[1] == 'Z' and match[0] == 'A':
			score += 3 + 0
		elif match[1] == 'Z' and match[0] == 'B':
			score += 3 + 6
		elif match[1] == 'Z' and match[0] == 'C':
			score += 3 + 3
	print("Part 1:", score)

	score = 0
	for match in data:
		if match[1] == 'X' and match[0] == 'A':
			score += 3 + 0
		elif match[1] == 'X' and match[0] == 'B':
			score += 1 + 0
		elif match[1] == 'X' and match[0] == 'C':
			score += 2 + 0
		elif match[1] == 'Y' and match[0] == 'A':
			score += 1 + 3
		elif match[1] == 'Y' and match[0] == 'B':
			score += 2 + 3
		elif match[1] == 'Y' and match[0] == 'C':
			score += 3 + 3
		elif match[1] == 'Z' and match[0] == 'A':
			score += 2 + 6
		elif match[1] == 'Z' and match[0] == 'B':
			score += 3 + 6
		elif match[1] == 'Z' and match[0] == 'C':
			score += 1 + 6
	print("Part 2:", score)

if __name__ == "__main__":
	main()
