import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic_values.csv'


def astar(start, end):
    # Begin your code (Part 4)
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

    with open(heuristicFile, mode='r', newline='', encoding='utf-8') as hfile:
        csv_reader = csv.reader(hfile)

        heuristic = {}
        head =[]

        head = next(csv_reader)[1:]
        head = list(map(int, head))
    
        for row in csv_reader:
            node = int(row[0])
            heuristics = list(map(float, row[1:]))
            heuristic[node] = heuristics
    
    def get_heuristic(current_node, end_node, head, heuristic_data):
        if end_node not in head:
            return float('inf')
        target_index = head.index(end_node)
        if current_node in heuristic_data:
            return heuristic_data[current_node][target_index]
        return float('inf')
    
    import heapq
    priority_queue = [(0, start)]
    dist = {start: 0}
    parent = {start: None}
    visited = set()
    num_visited = 0

    while priority_queue:
        total, current = heapq.heappop(priority_queue)
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

                    if neighbor not in visited:
                        new_dist = dist[current] + distance
                        heur = get_heuristic(neighbor, end, head, heuristic)
                        total = new_dist + heur

                        if neighbor not in dist or new_dist < dist[neighbor]:
                            dist[neighbor] = new_dist
                            parent[neighbor] = current
                            heapq.heappush(priority_queue, (total, neighbor))

    return [], float('inf'), num_visited
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {round(dist, 3)}')
    print(f'The number of visited nodes: {num_visited}')
