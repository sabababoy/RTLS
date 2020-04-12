import graph
import rtls
import imitation
import threading
import time
import sys

sys.stdin = open('test.txt', 'r')

g = graph.Graph()

rtls.Receiver.maxLenghtOfSignal = 100

r = rtls.Receiver(g, g.listOfVertices[0])
r2 = rtls.Receiver(g, g.listOfVertices[3])
r3 = rtls.Receiver(g, g.listOfVertices[0])
tr = rtls.Transmitter((0, g.listOfVertices[0], g.listOfEdges[0]), g)

mainer = imitation.Miner(tr)

thr = threading.Thread(target=mainer.start_walking)
thr.start()

while True:
	time.sleep(2)

	d1 = tr.findDistanceToReceiver(r)
	d2 = tr.findDistanceToReceiver(r2)
	d3 = tr.findDistanceToReceiver(r3)

	r.calculateCoordinates(tr.index, d1)
	r2.calculateCoordinates(tr.index, d2)
	r3.calculateCoordinates(tr.index, d3)

	rtls.answer(g)
	for i in rtls.Receiver.answer:
		print('Найденная координата:\n')
		a, b, c, d = i
		print('distance -> {}'.format(a))
		print('vertex -> {}'.format(b.index))
		print('edge -> {}'.format(c.index))
		print('rID -> {}'.format(d))

	print('Настойщие коордтнаты:\n')
	a, b, c = tr.realCoordinates
	print('distance -> {}'.format(a))
	print('vertex -> {}'.format(b.index))
	print('edge -> {}'.format(c.index))


