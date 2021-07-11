import math

'''
Manhattan.
'''
def manhattan(dx, dy):
      return dx + dy

'''
Euclidea.
'''
def euclidea(dx, dy):
    return math.sqrt(dx * dx + dy * dy)

'''
Octil.
'''
def octil(dx, dy):
    F = 1414
    return F * dx + (dy-dx)*1000 if (dx < dy) else F * dy + (dx-dy)*1000
