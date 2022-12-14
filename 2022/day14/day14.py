from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in f.read().splitlines()]
    
	xMax, yMax = data[0][0][0], data[0][0][1]
	for line in data:
		for x, y in line:
			if x > xMax: xMax = x
			if y > yMax: yMax = y
	mat = [[False for _ in range(xMax+147)] for _ in range(yMax+3)]
	for line in data:
		for i in range(len(line)-1):
			x1, y1 = line[i][0], line[i][1]
			x2, y2 = line[i+1][0], line[i+1][1]
			if x1 == x2:
				y = min(y1, y2)
				for j in range(max(y1, y2) - y + 1):
					mat[y+j][x1] = True
			if y1 == y2:
				x = min(x1, x2)
				for j in range(max(x1, x2) - x + 1):
					mat[y1][x+j] = True

	matCopy = [x[:] for x in mat]
	flag = True
	rest = False
	sand = [0, 500]
	count = 0
	while (flag):
		count += 1
		while (not(rest)):
			if not(mat[sand[0]+1][sand[1]]):
				sand[0] += 1
			elif not(mat[sand[0]+1][sand[1]-1]):
				sand[0] += 1
				sand[1] -= 1
			elif not(mat[sand[0]+1][sand[1]+1]):
				sand[0] += 1
				sand[1] += 1
			else:
				mat[sand[0]][sand[1]] = True
				rest = True
			if sand[0] > yMax:
				flag = False
				rest = True
				count -= 1
		sand = [0, 500]
		rest = False
	print("Part 1:", count)

	mat = [x[:] for x in matCopy]
	for i in range(len(mat[0])):
		mat[yMax+2][i] = True
	flag = True
	rest = False
	sand = [0, 500]
	count = 0
	while (flag):
		count += 1
		while (not(rest)):
			if not(mat[sand[0]+1][sand[1]]):
				sand[0] += 1
			elif not(mat[sand[0]+1][sand[1]-1]):
				sand[0] += 1
				sand[1] -= 1
			elif not(mat[sand[0]+1][sand[1]+1]):
				sand[0] += 1
				sand[1] += 1
			else:
				mat[sand[0]][sand[1]] = True
				rest = True
				if mat[0][500]:
					flag = False
		sand = [0, 500]
		rest = False
	print("Part 2:", count)

if __name__ == "__main__":
	main()
