from math import sqrt

class Vertex:

	quantity = 0
	
	def __init__(self):

		self.distanceToVertices = {} # {Vertex index: distance}
		self.connectedVerticesAndEdges = {} # {Connected vertex index: Edge index}
		self.index = Vertex.quantity
		Vertex.quantity += 1


class Edge:

	quantity = 0
	
	def __init__(self, vertexOne, vertexTwo, weight):

		self.index = Edge.quantity
		self.vertexOne = vertexOne
		self.vertexTwo = vertexTwo
		self.weight = weight
		Edge.quantity += 1
		

class Graph:

	def __init__(self):
		
		self.listOfVertices = []

		quantityOfVertices = int(input('How many vertices in the graph? '))

		print('---- Please, number the vertices (tops) of the graph! ----')
		print('Input vertices connections and distances:\n In the end just press Enter.')
		
		for i in range(quantityOfVertices):
			vertex = Vertex()
			self.listOfVertices.append(vertex)
		
		for i in range(quantityOfVertices):
			while True:
				connection = input('Vertex {} connected with: '.format(i + 1))
				if connection:
					connection = int(connection) - 1
					if (connection not in self.listOfVertices[i].connectedVerticesAndEdges) and (connection != i):
						distance = int(input('Distance: '))						
						edge = Edge(self.listOfVertices[i], connection, distance)
						self.listOfVertices[i].connectedVerticesAndEdges[connection] = edge
						self.listOfVertices[connection].connectedVerticesAndEdges[i] = edge
				else:
					break

		self.calculatingDistances()

	def calculatingDistances(self): # Dijkstra's algorythm for all vertices. To rember distances from all vertices to all vertices

		for vertex in self.listOfVertices:
			self.dijkstra(vertex)

	def dijkstra(self, vertex):

		start = vertex.index
		visited = []
		weight = [1000000000] * Vertex.quantity
		weight[start] = 0

		for i in range(Vertex.quantity):

			for v in self.listOfVertices[start].connectedVerticesAndEdges:
				if v not in visited:
					weight[self.listOfVertices[v].index] = weight[start] + self.listOfVertices[start].connectedVerticesAndEdges[v].weight
					vertex.distanceToVertices[self.listOfVertices[v].index] = weight[start] + self.listOfVertices[start].connectedVerticesAndEdges[v].weight

			visited.append(start)
			m = 1000000000

			for i in range(Vertex.quantity):
				if (i not in visited) and (weight[i] < m):
					start = i
					m = weight[i]
			







if __name__ == '__main__':
	print('It\'s just a module. Use it in your project to make graph.')