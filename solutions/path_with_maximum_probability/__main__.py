from solutions.utils.io import get_list
from .solution import maxProbability
from ..utils import io

print('Enter number of nodes:', end=' ')
n = io.get(int)

print('Enter edges (e.g. 0,1 0,2 1,2):', end=' ')
edges = [[int(node) for node in edge.split(',')]
         for edge in io.get_list(str)]

print('Enter space-separated success probabilities:', end=' ')
succProbs = io.get_list(float)

print('Enter start and end nodes, space-separated:', end=' ')
start, end = io.get_list(int)

print('Max probability:', maxProbability(n, edges, succProbs, start, end))