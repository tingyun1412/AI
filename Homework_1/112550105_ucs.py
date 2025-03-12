import csv
edgeFile = 'edges.csv'


def ucs(start, end):
    # Begin your code (Part 3)
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
    
    import heapq
    priority_queue = [(0, start)]
    dist = {start: 0}
    parent = {start: None}
    visited = set()
    num_visited = 0

    while priority_queue:
        cur_dist, current = heapq.heappop(priority_queue)
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1],  dist[end] ,num_visited

        num_visited += 1

        if current not in visited:
                
            visited.add(current)

            if current in edge:
                for neighbor, distance in edge[current]:
                    new_dist = cur_dist + distance

                    if neighbor not in visited  and (neighbor not in dist or new_dist < dist[neighbor]):
                        dist[neighbor] = new_dist
                        parent[neighbor] = current
                        heapq.heappush(priority_queue, (new_dist, neighbor))

    return [], float('inf'), num_visited
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {round(dist, 3)}')
    print(f'The number of visited nodes: {num_visited}')
