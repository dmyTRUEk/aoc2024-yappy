from sys import argv as cli_args
m_, moves_ = "".join(open(cli_args[-1]).readlines()).strip().split("\n\n")
m = [[]]
for i, l in enumerate(m_.splitlines()):
	for j, c in enumerate(l):
		if c == "@":
			ry, rx = i, j
		m[-1].append(c)
	m.append([])
moves = [c for l in moves_.replace("\n", "").splitlines() for c in l]
def swap(x1, y1, x2, y2):
	m[y1][x1], m[y2][x2] = m[y2][x2], m[y1][x1]
dxys = { "^": (0,-1), "v": (0,1), "<": (-1,0), ">": (1,0) }
for move in moves:
	dx, dy = dxys[move]
	x, y, f = rx, ry, False
	while True:
		x += dx
		y += dy
		if m[y][x] == ".":
			f = True
			break
		if m[y][x] == "#":
			break
	if f and abs(rx-x) + abs(ry-y) == 1:
		swap(rx, ry, x, y)
	elif f:
		swap(rx+dx, ry+dy, x, y)
		swap(rx, ry, rx+dx, ry+dy)
	if f:
		rx += dx
		ry += dy
gs = sum(100*i+j if c == "O" else 0 for i, l in enumerate(m) for j, c in enumerate(l))
print(gs)
