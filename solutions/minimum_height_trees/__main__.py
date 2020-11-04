from .solution import findMinHeightTrees

print('Enter number of nodes:', end=' ')
n = int(input().strip())

print('Enter space-separated edges (e.g. 1,2 1,0):', end=' ')
edges = [[int(node) for node in edge.split(',')] for edge in input().strip().split(' ')]

roots = findMinHeightTrees(n, edges)
print(f'Min height tree(s) are rooted at: {roots}')