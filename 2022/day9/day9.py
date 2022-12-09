from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

def isTouching(head: Point, tail: Point):
	if tail.x-1 <= head.x <= tail.x+1 and tail.y-1 <= head.y <= tail.y+1:
		return True
	return False

def findTail(head: Point, tail: Point):
	if not(isTouching(head, tail)):
		if head.x == tail.x:
			if head.y > tail.y:
				tail.y += 1
			else:
				tail.y -= 1
		elif head.y == tail.y:
			if head.x > tail.x:
				tail.x += 1
			else:
				tail.x -= 1
		else:
			if head.x > tail.x and head.y > tail.y:
				tail.x += 1
				tail.y += 1
			if head.x > tail.x and head.y < tail.y:
				tail.x += 1
				tail.y -= 1
			if head.x < tail.x and head.y < tail.y:
				tail.x -= 1
				tail.y -= 1
			if head.x < tail.x and head.y > tail.y:
				tail.x -= 1
				tail.y += 1
	return tail

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [[int(y) if y.isdigit() else y for y in x.split()] for x in f.read().splitlines()]

	head = Point(0, 0)
	tail = Point(0, 0)
	positions = []
	for dir, n in data:
		for _ in range(n):
			match dir:
				case "R":
					head.x += 1
				case "L":
					head.x -= 1
				case "U":
					head.y += 1
				case "D":
					head.y -= 1
			tail = findTail(head, tail)
			positions.append((tail.x, tail.y))
	print("Part 1:", len(set(positions)))

	knots = [Point(0, 0) for _ in range(10)]
	positions = []
	for dir, n in data:
		for _ in range(n):
			for i, _ in enumerate(knots):
				if i == 0:
					match dir:
						case "R":
							knots[i].x += 1
						case "L":
							knots[i].x -= 1
						case "U":
							knots[i].y += 1
						case "D":
							knots[i].y -= 1
				else:
					knots[i] = findTail(knots[i-1], knots[i])
			positions.append((knots[9].x, knots[9].y))
	print("Part 2:", len(set(positions)))

if __name__ == "__main__":
	main()
