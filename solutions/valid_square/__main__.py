from .solution import validSquare

print('Enter space-separated points, with coordinates separated by commas:'
      ' e.g. 0,0 1,1 1,0 0,1')

points = [[int(coord) for coord in vertex.split(',')]
          for vertex in input().strip().split(' ')]

valid = validSquare(*points)
print('Valid Square' if valid else 'Invalid Square')