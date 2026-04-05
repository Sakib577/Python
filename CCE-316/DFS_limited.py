tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

def dfs_limited(tree, start,limit, visited = None):
    if visited==None:
        visited=[]
    if limit <= 0:
        return
    if start not in visited:
        visited.append(start)
        print(start, end=" ")

    for node in tree[start]:
        dfs_limited(tree, node,limit-1, visited)

dfs_limited(tree, 'A', 3)