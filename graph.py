from math import sqrt

class Vertex:

	quantity = 0
	
	def __init__(self):

		self.connectedVerticesAndEdges = {} # {Connected Vertex: Edge}
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



if __name__ == '__main__':
	print('It\'s just a module. Use it in your project to make graph.')
