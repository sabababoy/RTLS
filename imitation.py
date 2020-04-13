import threading
import time
import random

class Miner():

	def __init__(self, transmitter):
		self.transmitter = transmitter
		self.walking = True
		self.coordinates = [0,0,0]

	def start_walking(self):
		self.coordinates[0] = self.transmitter.realCoordinates[0]
		self.coordinates[1] = self.transmitter.realCoordinates[1]
		self.coordinates[2] = self.transmitter.realCoordinates[2]
		while self.walking:
			time.sleep(1)
			self.coordinates[0] += 1
			if self.coordinates[0] >= self.coordinates[2].weight:
				self.coordinates[0] = self.coordinates[0] - self.coordinates[2].weight
				self.coordinates[1] = self.transmitter.graph.findSecondVertexInEdge(self.coordinates[1], self.coordinates[2])
				number = random.randint(0,len(self.coordinates[1].connectedVerticesAndEdges) - 1)

				i = 0
				newWay = None

				for key in self.coordinates[1].connectedVerticesAndEdges:
					if i == number:
						newWay = key
						break
					
					i += 1
				
				self.coordinates[2] = self.coordinates[1].connectedVerticesAndEdges[newWay]
				

			self.transmitter.realCoordinates = (self.coordinates[0], self.coordinates[1], self.coordinates[2])

	def stop_walking(self):
		self.walking = False
