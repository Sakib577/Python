# Unidriected Tree
un_tree = {
        'A': ['B', 'E'],
        'B': ['C', 'D', 'A'],
        'C': ['F', 'B'],
        'D': ['B'],
        'E': ['A'],
        'F': ['C']
    }

from collections import deque

def bidirectional_search(tree, start, goal):
    if start == goal:
        return None, None
    
    start_visited = []
    end_visited = []

    start_queue = deque([start])
    end_queue = deque([goal])

    while start_queue or end_queue:
        if start_queue:
            start_node= start_queue.popleft()
            if start_node not in start_visited:
                start_visited.append(start_node)

                for neighbor in tree[start_node]:
                    if neighbor not in start_visited:
                        start_queue.append(neighbor)

        if end_queue:
            end_node = end_queue.popleft()
            if end_node not in end_visited:
                end_visited.append(end_node)

                for neighbor in tree[end_node]:
                    if neighbor not in end_visited:
                        end_queue.append(neighbor)

        if start_node in end_visited or end_node in start_visited:
            return start_visited, end_visited
        
print(bidirectional_search(un_tree, 'A', 'F'))