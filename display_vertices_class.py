import matplotlib.pyplot as plt
import random


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


vertices = []

# create 10 vertices
for _ in range(10):
    new_vertex = Vertex(random.uniform(0, 1), random.uniform(0, 1))
    vertices.append(new_vertex)

for vertex in vertices:
    plt.plot(vertex.x, vertex.y, 'ro')
plt.show()
