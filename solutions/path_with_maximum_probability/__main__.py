from .solution import maxProbability

print('Enter number of nodes:', end=' ')
n = int(input().strip())

print('Enter edges (e.g. 0,1 0,2 1,2):', end=' ')
edges = [[int(node) for node in edge.split(',')]
         for edge in input().strip().split(' ')]

print('Enter space-separated success probabilities:', end=' ')
succProbs = [float(prob) for prob in input().strip().split(' ')]

print('Enter start and end nodes, space-separated:', end=' ')
start, end = [int(node) for node in input().strip().split(' ')]

print('Max probability:', maxProbability(n, edges, succProbs, start, end))