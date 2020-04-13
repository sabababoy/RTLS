import graph
import rtls
import imitation
import threading
import time
import sys

_in = sys.stdin
_out = sys.stdout
sys.stdin = open('test.txt', 'r')

if sys.stdin != _in:
	sys.stdout = open('trash.txt', 'w+')

g = graph.Graph()

if sys.stdin != _in:
	sys.stdout = _out

rtls.Receiver.maxLenghtOfSignal = 200

r = rtls.Receiver(g, g.listOfVertices[0])
r2 = rtls.Receiver(g, g.listOfVertices[2])
r3 = rtls.Receiver(g, g.listOfVertices[9])
tr = rtls.Transmitter((0, g.listOfVertices[0], g.listOfEdges[0]), g)

mainer = imitation.Miner(tr)

thr = threading.Thread(target=mainer.start_walking)
thr.start()

while True:
	time.sleep(2)

	tr.sendDistances()

	answer = rtls.answer(g)
	for i in answer:
		print('@@@ Find:')
		a, b, c, d = i
		print('distance -> {}'.format(a))
		print('vertex -> {}'.format(b.index))
		print('edge -> {}'.format(c.index))
		print('rID -> {}\n'.format(d))

	print('@@@ Real Coordinates:')
	a, b, c = tr.realCoordinates
	print('distance -> {}'.format(a))
	print('vertex -> {}'.format(b.index))
	print('edge -> {}'.format(c.index))
	print('--------or---------')
	print('distance -> {}'.format(c.weight - a))
	print('vertex -> {}'.format(g.findSecondVertexInEdge(b, c).index))
	print('edge -> {}\n\n\n'.format(c.index))


