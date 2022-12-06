from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

PKT_BUFFER_DIM = 4
MSG_BUFFER_DIM = 14

def findMarker(string, bufferDim):
	marker = 0
	buffer = ["" for n in range(bufferDim)]
	for i in range(len(buffer)-1):
		buffer[i+1] = string[i]
	for i in range(len(buffer)-1, len(string)):
		buffer.pop(0)
		buffer.append(string[i])
		if len(buffer) == len(set(buffer)):
			marker = i+1
			return marker
	return marker

def main():
	with open(INPUT_FILE, mode="rt") as f:
		data = f.read()
    
	marker = findMarker(data, PKT_BUFFER_DIM)
	print("Part 1:", marker)

	marker = findMarker(data, MSG_BUFFER_DIM)
	print("Part 2:", marker)

if __name__ == "__main__":
	main()
