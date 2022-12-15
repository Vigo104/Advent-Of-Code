# WARNING run time ~10 minutes
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = [[y.split("=") for y in x.split(":")] for x in f.read().splitlines()]

	sensors = [[0, 0] for _ in range(len(data))]
	beacons = [[0, 0] for _ in range(len(data))]
	for i, _ in enumerate(data):
		sensors[i] = [int(data[i][0][1].removesuffix(", y")), int(data[i][0][2])]
		beacons[i] = [int(data[i][1][1].removesuffix(", y")), int(data[i][1][2])]

	count = 0
	flag = False
	i = 2000000
	for j in range(-2000000, 5000000):
		for sensor, beacon in zip(sensors, beacons):
			distPoint = abs(sensor[0] - j) + abs(sensor[1] - i)
			distBeacon = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
			if (distPoint <= distBeacon) and ([j, i] not in sensors) and ([j, i] not in beacons):
				flag = True
		if flag:
			count += 1
		flag = False
	print("Part 1:", count)

	areas = []
	for sensor, beacon in zip(sensors, beacons):
		dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
		areas.append([sensor[0], sensor[1], dist])

	points = []
	for area in areas:
		dist = area[2]
		x = area[0]
		y = area[1] + dist + 1
		for _ in range(dist+1):
			if 0 <= x <= 4000000 and 0 <= y <= 4000000:
				points.append([x, y])
			x += 1
			y -= 1
		for _ in range(dist+1):
			if 0 <= x <= 4000000 and 0 <= y <= 4000000:
				points.append([x, y])
			x -= 1
			y -= 1
		for _ in range(dist+1):
			if 0 <= x <= 4000000 and 0 <= y <= 4000000:
				points.append([x, y])
			x -= 1
			y += 1
		for _ in range(dist+1):
			if 0 <= x <= 4000000 and 0 <= y <= 4000000:
				points.append([x, y])
			x += 1
			y += 1

	result = [0, 0]
	flag = True
	for point in points:
		for area in areas:
			distBeacon = area[2]
			distPoint = abs(area[0] - point[0]) + abs(area[1] - point[1])
			if distPoint <= distBeacon:
				flag = False
		if flag:
			result = point
		flag = True

	print("Part 2:", result[0] * 4000000 + result[1])

if __name__ == "__main__":
	main()
