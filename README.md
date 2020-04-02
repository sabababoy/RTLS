# RTLS
Search for miners in mines using the RTLS system
RTLS (Real-time Locating Systems) are used to automatically identify and track the location of objects or people in real time, usually within a building or other contained area.
The essence of the project is the search for miners in mines using the RTLS system.

Task:

Given a map of mining consisting of corridors. The place where the corridor begins is the vertex of the graph. Some of them have transmitters that send a signal to a receiver located at the miner. The signal to the receiver does not come from all transmitters, due to the curvature of the corridors, rocks and distance. Based on the time it takes for the signal to go back and forth, it is possible to say how far the miner is from him. By combining data from different transmitters, you can find out the location of the miner. The answer may not be accurate, since during the calculation a person walks some distance, plus the signal error (The answer will be a coordinate interval).

Realization:

As mentioned above: the map is a graph, where the corridor is an edge, and the starting point of the corridor - vertex of the graph. From some peaks (in which the transmitter is installed) a signal will come out. Suppose the transmitter has a maximum signal length. Then the signals from the transmitters that are remote from it no more than 'n' will reach the miner (which walks along our graph) and from these transmitters we will randomly select those from which the signal has come. Why? Because despite the fact that the transmitter is close due to rock characteristics or transmitter error, the signal may not reach the receiver. The signal is not constant, it propagates once every few seconds. Based on several such measurements and their intersections, we can calculate the location of a person.

Where does the task come from?

I got it as a term paper at the university, from my teacher. He received an order from a real mine to implement this system for them. So this project can be used for real situations. It is necessary to configure it by hand and specialize to your needs.
