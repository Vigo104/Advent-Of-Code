from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def createStack(crates: list[str]):
	s = int(max(set(crates[len(crates)-1])))
	stack = [[] for n in range(s)]
	for i in reversed(range(len(crates)-1)):
		for j, x in enumerate(crates[i][1::4]):
			if x != " ": stack[j].append(x)
	return stack

def main():
	with open(INPUT_FILE, mode="rt") as f:
		crates, instr = [x.splitlines() for x in f.read().split("\n\n")]
    
	for i, x in enumerate(instr):
		x = x.split(" ")
		a, b, c = int(x[1]), int(x[3])-1, int(x[5])-1
		instr[i] = [a, b, c]
	
	stack = createStack(crates)
	stackCopy = [x[:] for x in stack]

	for x in instr:
		a, b, c = x[0], x[1], x[2]
		for n in range(a):
			stack[c].append(stack[b].pop())
	
	result = "".join(x[-1] for x in stack)
	print("Part 1:", result)

	stack = [x[:] for x in stackCopy]
	for x in instr:
		a, b, c = x[0], x[1], x[2]
		stack[c].extend(stack[b][-a:])
		stack[b] = stack[b][:-a]
	
	result = "".join(x[-1] for x in stack)
	print("Part 2:", result)

if __name__ == "__main__":
	main()
