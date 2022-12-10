from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def checkShorter(data, k, l):
	visible = ahead = behind = line = row = True
	for i in range(len(data)):
		if data[i][l] >= data[k][l]:
			if i < k:
				ahead = False
			elif i > k:
				behind = False
	if not(ahead) and not(behind):
		line = False
	ahead = behind = row = True
	for j in range(len(data[0])):
		if data[k][j] >= data[k][l]:
			if j < l:
				ahead = False
			elif j > l:
				behind = False
	if not(ahead) and not(behind):
		row = False
	if not(line) and not(row):
		visible = False
	return visible

def countView(data, i, j, direction):
	score = 0
	if direction == "up":
		for k in reversed(range(i)):
			score += 1
			if data[i][j] <= data[k][j]:
				return score
	elif direction == "down":
		for k in range(i+1, len(data)):
			score += 1
			if data[i][j] <= data[k][j]:
				return score
	elif direction == "left":
		for k in reversed(range(j)):
			score += 1
			if data[i][j] <= data[i][k]:
				return score
	elif direction == "right":
		for k in range(j+1, len(data[0])):
			score += 1
			if data[i][j] <= data[i][k]:
				return score
	return score

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [[int(y) for y in x] for x in f.read().splitlines()]
	
	visibleTrees = 0
	for i, line in enumerate(data):
		for j, _ in enumerate(line):
			if i == 0 or i == len(data)-1 or j == 0 or j == len(data)-1:
				visibleTrees += 1
			elif checkShorter(data, i, j):
				visibleTrees += 1
	print("Part 1:", visibleTrees)

	scores = []
	up = down = left = right = 0
	for i, line in enumerate(data):
		for j, _ in enumerate(line):
			up = countView(data, i, j, "up")
			down = countView(data, i, j, "down")
			left = countView(data, i, j, "left")
			right = countView(data, i, j, "right")
			scores.append(up * down * left * right)
			up = down = left = right = 0
	print("Part 2:", max(scores))

	# Visualization
	plt.imshow(np.matrix(data), cmap='Greens')
	plt.axis('off')
	plt.title('trees')
	plt.show()
	visibleMat = [[False for y in range(len(data[0]))] for x in range(len(data))]
	for i, line in enumerate(data):
		for j, _ in enumerate(line):
			if i == 0 or i == len(data)-1 or j == 0 or j == len(data)-1:
				visibleMat[i][j] = True
			elif checkShorter(data, i, j):
				visibleMat[i][j] = True
	plt.imshow(np.matrix(visibleMat), cmap='Greens')
	plt.axis('off')
	plt.title('visibility')
	plt.show()

if __name__ == "__main__":
	main()
