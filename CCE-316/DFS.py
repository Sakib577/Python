tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

def dfs(tree, start, visited = None):
    if visited is None:
        visited=[]
    if start not in visited:
        visited.append(start)
        print(start, end=" ")

    for node in tree[start]:
        dfs(tree, node, visited)

dfs(tree, 'A')