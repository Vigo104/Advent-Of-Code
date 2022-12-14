from pathlib import Path
import json

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def compare(left, right):
	lenLeft, lenRight = len(left), len(right)
	for i in range(min(lenLeft, lenRight)):
		if type(left[i]) == int and type(right[i]) == int:
			if left[i] < right[i]:
				return True
			if left[i] > right[i]:
				return False
		elif type(left[i]) == int or type(right[i]) == int:
			if type(left[i]) == int:
				left[i] = [left[i]]
			elif type(right[i]) == int:
				right[i] = [right[i]]
		if type(left[i]) == list or type(right[i]) == list:
			if not(compare(left[i], right[i])) and compare(left[i], right[i]) != None:
				return False
			if compare(left[i], right[i]):
				return True
	if lenLeft > lenRight:
		return False
	elif lenLeft < lenRight:
		return True

def main():
	with open(INPUT_FILE, mode="rt") as f:
		input = f.read()
	
	data1 = [[json.loads(x) for x in pair.splitlines()] for pair in input.split("\n\n")]
	indexes = []
	for i, pair in enumerate(data1):
		if compare(pair[0], pair[1]):
			indexes.append(i+1)
	print("Part 1:", sum(indexes))

	data2 = [json.loads(line) for line in input.replace("\n\n", "\n").splitlines()]
	data2.append([[2]])
	data2.append([[6]])
	stop = False
	while not(stop):
		stop = True
		for i in range(len(data2)-1):
			if not(compare(data2[i], data2[i+1])):
				stop = False
				temp = data2[i]
				data2[i] = data2[i+1]
				data2[i+1] = temp
	firstKey = 0
	secondKey = 0
	for i, line in enumerate(data2):
		if len(line) == 1 and len(line[0]) == 1 and len(line[0][0]) == 1 and len(line[0][0][0]) == 1:
			if line[0][0][0][0] == 2:
				firstKey = i+1
		if len(line) == 1 and len(line[0]) == 1 and len(line[0][0]) == 1 and len(line[0][0][0]) == 1:
			if line[0][0][0][0] == 6:
				secondKey = i+1
	print("Part 2:", firstKey * secondKey)

if __name__ == "__main__":
	main()
