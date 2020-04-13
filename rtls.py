'''
	There is no implementation of methods for sending and receiving a signal,
since there is no hardware for implementing the calculation of the signal return time.
We just imitate work.
	Therefore, we believe that the transmitter knows its actual coordinates and sends
the distance from them to the desired receivers (no more than n remote). 
The distance to the receiver and the receiver itself are calculated in the transmitter class method.

In a real situation, the receivers themselves will calculate the distance to the transmitter based on the received signal.
'''


class Receiver:

	quantity = 0
	calculatedCoordinates = []
	answer = []
	listOfReceivers = []
	maxLenghtOfSignal = 0

	def __init__(self, graph, vertex):
		self.index = Receiver.quantity
		Receiver.quantity += 1
		self.graph = graph
		self.vertex = vertex
		self.lastCalculatedCoordinates = []
		self.lastTakenDistance = None
		Receiver.listOfReceivers.append(self)
	

	'''
	Function that calculate coordinates to a miner. Takes the distance rfom receiver to a miner as an argument.
	'''
	
	def calculateCoordinates(self, transmitterIndex, distance):

		self.lastCalculatedCoordinates = []

		self.lastTakenDistance = distance

		if distance != None:
			vertex = self.vertex
			for i in vertex.distanceToVertices:
				for x in self.graph.listOfVertices[i].connectedVerticesAndEdges:
					if (vertex.distanceToVertices[i] - self.graph.listOfVertices[x].connectedVerticesAndEdges[i].weight != vertex.distanceToVertices[x] and
						distance - self.vertex.distanceToVertices[i] >= 0 and
						vertex.distanceToVertices[i] + self.graph.listOfVertices[i].connectedVerticesAndEdges[x].weight > distance and
						vertex.distanceToVertices[x] + self.graph.listOfVertices[i].connectedVerticesAndEdges[x].weight - (distance - vertex.distanceToVertices[i]) >= distance):

						self.lastCalculatedCoordinates.append((self.graph.listOfVertices[i].connectedVerticesAndEdges[x].weight - (vertex.distanceToVertices[i] + self.graph.listOfVertices[i].connectedVerticesAndEdges[x].weight - distance), 
							self.graph.listOfVertices[i], 
							self.graph.listOfVertices[i].connectedVerticesAndEdges[x], 
							transmitterIndex))
						
						if self.graph.listOfVertices[i].connectedVerticesAndEdges[x].weight - (vertex.distanceToVertices[i] + self.graph.listOfVertices[i].connectedVerticesAndEdges[x].weight - distance) == 0:
							break

			self.deleteDuplicates(self.findDuplicates(self.lastCalculatedCoordinates), self.lastCalculatedCoordinates)

			for i in self.lastCalculatedCoordinates:
				Receiver.calculatedCoordinates.append(i)

	'''
	Delete similar and unreal coordinates.
	Such results may appear when there are two identical distances to the same point,
	as well as if there is a shorter path to the found point
	'''
	def findDuplicates(self, listOfCoordinates): 

		duplicates = []

		for coordinates in listOfCoordinates:
			if listOfCoordinates.index(coordinates) not in duplicates:
				newDistance = (coordinates[2].weight - coordinates[0])
				newVertex = self.graph.findSecondVertexInEdge(coordinates[1], coordinates[2])
				newCoordinates = (newDistance, newVertex, coordinates[2], coordinates[3])

				try:
					duplicates.append(listOfCoordinates.index(newCoordinates))
				except:
					pass

		return duplicates

	def deleteDuplicates(self, deadList, fromList):
		for i in deadList:
			fromList.pop(i)



class Transmitter:

	quantity = 0

	def __init__(self, coordinates, graph):
		self.graph = graph
		self.realCoordinates = coordinates
		self.index = Transmitter.quantity
		Transmitter.quantity += 1
		
	'''
	result -> ditance to receiver from transmitter. 
	In real life this distance is calculated on receivers. 
	(by calculating from the speed of the signal and its return time).
	'''

	def findDistanceToReceiver(self, receiver):
		
		
		distance = receiver.vertex.distanceToVertices[self.realCoordinates[1].index] + self.realCoordinates[0]
		
		if (receiver.vertex.distanceToVertices[self.graph.findSecondVertexInEdge(self.realCoordinates[1], self.realCoordinates[2]).index] +
			self.realCoordinates[2].weight - self.realCoordinates[0] < distance):

			distance = receiver.vertex.distanceToVertices[self.graph.findSecondVertexInEdge(self.realCoordinates[1], self.realCoordinates[2]).index] + self.realCoordinates[2].weight - self.realCoordinates[0]

		return distance

	def sendDistances(self):
		for i in Receiver.listOfReceivers:
			if self.findDistanceToReceiver(i) <= Receiver.maxLenghtOfSignal:
				i.calculateCoordinates(self.index, self.findDistanceToReceiver(i))
			else:
				i.calculateCoordinates(self.index, None)

'''
	The function of finding an approximate answer by removing impossible results and intersecting possible ones.
Impossible results:
The results received from all transmitters fall into the list of found answers, BUT they can contradict each other.
Example:
From receiver A, the path to point x is 100. From receiver B, it is 50. 
The point can be removed from A by 100, and from B less by 50 and vice versa. 
(For example, if the transmitters are at the vertices of one edge, the length is short 120. 
In this case, both results are deleted, so it contradicts each other.)
Thus, if there is a shorter path to the receiver from the point than the distance it has received, this point is deleted.

If the distance from the point to the receiver is greater than the length of its signal, 
this receiver does not participate in the dispute.

Paths to points are calculated based on previously calculated distances to the vertices of the graph (dijkstra algorithm).
'''

def answer(graph):

	Receiver.answer = Receiver.calculatedCoordinates

	# Unreal results deleting
	while True:
		deadList = []
		for receiver in Receiver.listOfReceivers:
			if receiver.lastTakenDistance:
				for coordinates in Receiver.answer:
					if coordinates not in deadList:
						firstWay = graph.listOfVertices[receiver.vertex.index].distanceToVertices[coordinates[1].index] + coordinates[0]
						secondWay = graph.listOfVertices[receiver.vertex.index].distanceToVertices[graph.findSecondVertexInEdge(coordinates[1], coordinates[2]).index] + coordinates[2].weight - coordinates[0]

						if firstWay > secondWay:
							firstWay, secondWay = secondWay, firstWay

						if firstWay != receiver.lastTakenDistance:
							deadList.append(coordinates)

		if deadList == []: break


		for i in deadList:
			Receiver.answer.pop(Receiver.answer.index(i))


	# Error Removal
	while True:
		deadList = []
		for i in Receiver.answer:
			if i not in deadList:
				for c in Receiver.answer:
					if c not in deadList and i != c:
						if i[2] == c[2]:
							if i[1] == c[1]:
								if -5 < i[0] - c[0] <= 5:
									deadList.append(c)
							else:
								if (i[2].weight - i[0] - c[0]) <= 5:
									deadList.append(c)

		if deadList == []: break

		for i in deadList:
			Receiver.answer.pop(Receiver.answer.index(i))

	answer = Receiver.answer
	Receiver.calculatedCoordinates = []
	Receiver.answer = []

	return answer




