from heapq import *
print("Enter n and m: " , end='')
n, m = map(int, input().split(" "))

print("Enter map:")
maze = []
for i in range(n):
    maze.append(list(map(int, input().split(" "))))

print("Enter start position: " ,end='')
start = tuple(reversed(list(map(int, input().split(" ")))))
print("Enter end position: " ,end='')
end = tuple(reversed(list(map(int, input().split(" ")))))


def heuristic(point):
    return abs(point[0] - end[0]) + abs(point[1] - end[1])


priority_queue = [(heuristic(start), start)]
distance = {start: 0}
mark = []
parent = {}

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# enum for moves
name = {(1, 0): "down", (0, 1): "right", (-1, 0): "up", (0, -1): "left"}

while priority_queue:
    (cst, v) = heappop(priority_queue)
    if v in mark:#if state already exists
        continue
    mark.append(v)
    x, y = v
    g = cst - heuristic(v)
    # g = 9 - 9 = 0
    for it in range(len(moves)): # it = 0,1,2,3
        nx = x + moves[it][0]
        ny = y + moves[it][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or ((maze[x][y] & (2 ** it)) != 0):
            continue
        if it == 0: newit = 2
        elif it == 1: newit = 3
        elif it == 2: newit = 0
        else: newit = 1

        if (maze[nx][ny] & (2 ** newit)) != 0:
            continue

        np = (nx, ny)
        if np in distance and distance[np] <= g + 1:
            continue
        distance[np] = g + 1
        parent[np] = v
        heappush(priority_queue, (distance[np] + heuristic(np), np))

print(distance[end])

it = end
path = []
while it != start:
    np = parent[it]
    dx = it[0] - np[0]
    dy = it[1] - np[1]
    path.append(name[(dx, dy)])
    it = np

print(" ".join(reversed(path)))
