from collections import deque
R = int(input())
C = int(input())
patch = []
for _ in range(R):
    row = input()
    patch.append(list(row))
A = int(input())
B = int(input())

queue = deque() 
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False for _ in range(C)] for _ in range(R)]
queue.append((A, B))
visited[A][B] = True
total_value = 0
while queue:
    x, y =queue.popleft()
    if patch[x][y] == 'S':
        total_value += 1
    elif patch[x][y] == 'M':
        total_value += 5
    elif patch[x][y] == 'L':
        total_value += 10
    
    for x1, y1 in directions:
        x2, y2 = x + x1, y + y1
        if 0<=x2<R and 0<=y2<C:
            if visited[x2][y2]== False and patch[x2][y2] != "*":
                visited[x2][y2] = True
                queue.append((x2, y2))
print(total_value)
