import csv
edgeFile = 'edges.csv'

def bfs(start, end):
    # Begin your code (Part 1)
    with open(edgeFile, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        edge = {}
        for row in csv_reader:
            s, neighbor, distance = row
            s = int(s) 
            neighbor = int(neighbor) 
            distance = float(distance)
            if s not in edge:
                edge[s] = []
            edge[s].append((neighbor, distance))
    
    from collections import deque

    queue = deque([(start, [start], 0)])
    visited = set()
    num_visited = 0

    while queue:
        current, path, dist = queue.popleft()

        if current == end:
                return path, dist, num_visited

        if current not in visited:
            
            num_visited += 1
            visited.add(current)

            if current in edge:
                for neighbor, distance in edge[current]:
                    if neighbor not in visited: 
                        queue.append((neighbor, path + [neighbor], dist + distance))

    return [], float('inf'), num_visited

    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {round(dist, 3)}')
    print(f'The number of visited nodes: {num_visited}')
