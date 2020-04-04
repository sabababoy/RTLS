""" 
	There is no implementation of methods for sending and receiving a signal,
since there is no hardware for implementing the calculation of the signal return time.
We just imitate work.
	Therefore, we believe that the transmitter knows its actual coordinates and sends
the distance from them to the desired receivers (no more than n remote). 
The distance to the receiver and the receiver itself are calculated in the transmitter class method.

In a real situation, the receivers themselves will calculate the distance to the transmitter based on the received signal.
"""

class Receiver:

	quantity = 0

	def __init__(self, graph, vertex):
		self.index = Receiver.quantity
		Receiver.quantity += 1
		self.graph = graph
		self.vertex = vertex
		self.lastCalculatedCoordinates = []
	
	def calculateCoordinates(self, transmitterIndex, distance, vertex = None, prVer = -1): # Function that calculate coordinates to a miner. Takes the distance to a miner as an argument
		#coordinates = (Distance from vertex, Vertex, Edge, TransmitterIndex)
		if vertex == None:
			vertex = self.vertex
		start = vertex.index
		
		for i in self.graph.listOfVertices[start].connectedVerticesAndEdges:
			if i != prVer and (self.graph.listOfVertices[start].connectedVerticesAndEdges[i].weight > distance):
				self.lastCalculatedCoordinates.append((distance, vertex, self.graph.listOfVertices[start].connectedVerticesAndEdges[i], transmitterIndex))
			elif i != prVer:
				self.calculateCoordinates(transmitterIndex, distance - self.graph.listOfVertices[start].connectedVerticesAndEdges[i].weight, self.graph.listOfVertices[i], start)


