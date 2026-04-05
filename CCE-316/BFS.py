tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

from collections import deque

def bfs(tree, start):
    visited = []
    q=deque([start])

    while q:
        node=q.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for neighbor in tree[node]:
                if neighbor not in visited:
                    q.append(neighbor)

bfs(tree, 'A')