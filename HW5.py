from collections import deque

def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    R, C = len(maze), len(maze[0])
    dirs = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }
    normal_dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    # หา S และ E
    start = end = None
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start = (r,c)
            elif maze[r][c] == 'E':
                end = (r,c)

    if not start or not end:
        return {"distance": -1, "path": []}

    # ฟังก์ชัน simulate conveyor move
    def follow_conveyor(r, c):
        path = [(r,c)]
        while maze[r][c] in dirs:
            dr, dc = dirs[maze[r][c]]
            nr, nc = r+dr, c+dc
            if not (0 <= nr < R and 0 <= nc < C):  # out of bounds
                return None
            if maze[nr][nc] == '#':  # hit wall
                return None
            r, c = nr, nc
            path.append((r,c))
        return (r,c,path)

    # BFS
    dq = deque()
    dq.append(start)
    dist = {start: 0}
    parent = {start: None}

    while dq:
        r, c = dq.popleft()
        if (r,c) == end:
            break

        for dr, dc in normal_dirs:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if maze[nr][nc] == '#':
                continue

            if maze[nr][nc] in dirs:  # conveyor
                res = follow_conveyor(nr,nc)
                if not res:
                    continue
                fr, fc, conveyor_path = res
                if (fr,fc) not in dist or dist[(fr,fc)] > dist[(r,c)] + 1:
                    dist[(fr,fc)] = dist[(r,c)] + 1
                    parent[(fr,fc)] = ((r,c), conveyor_path)
                    dq.append((fr,fc))
            else:  # normal move
                if (nr,nc) not in dist or dist[(nr,nc)] > dist[(r,c)] + 1:
                    dist[(nr,nc)] = dist[(r,c)] + 1
                    parent[(nr,nc)] = ((r,c), [(nr,nc)])
                    dq.append((nr,nc))

    if end not in dist:
        return {"distance": -1, "path": []}

    # reconstruct path
    path = []
    node = end
    while node != start:
        prev, seg = parent[node]
        path = seg + path
        node = prev
    path = [list(start)] + [list(p) for p in path]

    return {"distance": dist[end], "path": path}


if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze))
    # {'distance': 2, 'path': [[0,0],[0,1],[0,2],[0,3],[0,4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze))
    # {"distance": -1, "path": []}

    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    print(maze_solver_with_conveyors(maze))
    # {'distance': 7, 'path': [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,3],[2,3],[1,3],[0,3],[0,4]]}