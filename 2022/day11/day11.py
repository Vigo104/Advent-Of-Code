from pathlib import Path
import copy

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

class Monkey():
	def __init__(self):
		self.index = 0
		self.items = []
		self.op = ["", ""]
		self.test = 0
		self.dest = [0, 0]

def parseInput(data):
	monkeys = [Monkey() for _ in data]
	for i, _ in enumerate(data):
		monkeys[i].index = int(data[i][0][:-1][-1:])
		s = data[i][1].split(":")
		monkeys[i].items = [*map(int, s[1].split(","))]
		s = data[i][2].split(" ")
		s = s[-2:]
		monkeys[i].op[0] = s[0]
		monkeys[i].op[1] = s[1]
		s = data[i][3].split(" ")
		monkeys[i].test = int(s[-1:][0])
		monkeys[i].dest[0] = int(data[i][4][-1:][0])
		monkeys[i].dest[1] = int(data[i][5][-1:][0])
	return monkeys

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [x.splitlines() for x in f.read().split("\n\n")]
	monkeys = parseInput(data)

	monkeysCopy = copy.deepcopy(monkeys)
	monkeyBusiness = [0 for _ in range(len(data))]
	for monkey in monkeys * 20:
		for worryLevel in monkey.items:
			monkeyBusiness[monkey.index] += 1
			if monkey.op[1].isdigit():
				if monkey.op[0] == "+":
					worryLevel += int(monkey.op[1])
				elif monkey.op[0] == "*":
					worryLevel *= int(monkey.op[1])
			else:
				worryLevel *= worryLevel
			worryLevel = worryLevel//3
			if worryLevel % monkey.test == 0:
				monkeys[monkey.dest[0]].items.append(worryLevel)
			else:
				monkeys[monkey.dest[1]].items.append(worryLevel)
		monkey.items.clear()
	result = sorted(set(monkeyBusiness), reverse=True)
	print("Part 1:", result[0] * result[1])

	monkeys = copy.deepcopy(monkeysCopy)
	magicNumber = 1
	for monkey in monkeys:
		magicNumber *= monkey.test
	monkeyBusiness = [0 for _ in range(len(data))]
	for monkey in monkeys * 10000:
		for worryLevel in monkey.items:
			monkeyBusiness[monkey.index] += 1
			if monkey.op[1].isdigit():
				if monkey.op[0] == "+":
					worryLevel += int(monkey.op[1])
				elif monkey.op[0] == "*":
					worryLevel *= int(monkey.op[1])
			else:
				worryLevel *= worryLevel
			worryLevel %= magicNumber
			if worryLevel % monkey.test == 0:
				monkeys[monkey.dest[0]].items.append(worryLevel)
			else:
				monkeys[monkey.dest[1]].items.append(worryLevel)
		monkey.items.clear()
	result = sorted(set(monkeyBusiness), reverse=True)
	print("Part 2:", result[0] * result[1])

if __name__ == "__main__":
	main()
