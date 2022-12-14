from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def bfs(graph, start, end):
	visited = []
	visited.append(start)
	queue = []
	queue.append(start)
	parent = {}
	parent[start] = None

	found = False
	while queue:
		current = queue.pop(0)
		if current == end:
			found = True
			break
		for neighbor in graph[current]:
			if neighbor not in visited:
				visited.append(neighbor)
				queue.append(neighbor)
				parent[neighbor] = current

	path = []
	if found:
		path.append(end)
		while parent[end] is not None:
			path.append(parent[end]) 
			end = parent[end]
		path.reverse()
	return path

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = f.read().splitlines()
	
	start = []
	end = []
	heightmap = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == "S":
				start = (i, j)
				heightmap[i][j] = 1
			elif data[i][j] == "E":
				end = (i, j)
				heightmap[i][j] = 26
			else:
				heightmap[i][j] = ord(data[i][j]) - 96

	rows = len(heightmap)
	cols = len(heightmap[0])
	graph = {}
	for i in range(rows):
		for j in range(cols):
			graph[(i,j)] = []
			if (i-1 >= 0) and (heightmap[i-1][j] <= 1 + heightmap[i][j]):
				graph[(i, j)].append((i-1, j))
			if (i+1 < rows) and (heightmap[i+1][j] <= 1 + heightmap[i][j]):
				graph[(i, j)].append((i+1, j))
			if (j-1 >= 0) and (heightmap[i][j-1] <= 1 + heightmap[i][j]):
				graph[(i, j)].append((i, j-1))
			if (j+1 < cols) and (heightmap[i][j+1] <= 1 + heightmap[i][j]):
				graph[(i, j)].append((i, j+1))

	path = bfs(graph, start, end)
	print("Part 1:", len(path) - 1)

	cheat = []
	for i in range(len(heightmap)):
		start = (i, 0)
		path = bfs(graph, start, end)
		cheat.append(len(path) - 1)
	print("Part 2:", min(cheat))

if __name__ == "__main__":
	main()
