position, fret, distance between pairs of nodes or antinodes:


as position and fret increases, the frequency also increases and the distance between two successive peaks decreases per unit of time.

for 10 seconds of total runtime, 2 strings can have (24, 24) possible fret positions and for each state, the wavelengths (l1, l2) given fret positions (p1, p2) have two nodes (n1, n2) and two antinodes (a1, a2).

the largest wavelength will have large distances covered between each peaks in the cycle containing two phases opposing their countertop.





consider two waves that have exact same properties expect for the phases:

call them (user, agent)

write a program called medium which facilitates the communication of two objects via their shared tracks.

each object has two tracks and one is shared with a common medium.

medium also has two tracks where one is used to collect the new messages and the other is used to copy the collected messages.

both objects use their choosen pole to connect with the other via the pole that medium uses and the other pole is used to copy the information from medium side to their class memory for further computation.

so the medium could use a sine and cosine wave of equal frequency and use +pi/2 and -pi/2 for binding with the phases of the object systems.

all objects will use a fixed interval denoting one unit of communication and repeat that entire wavelength for arbitrary long communucation periods.

use bytes for messages and have all the objects automatically manage reception and transmission of data without requiring manual intervention.

additional note:
1. use system clock to match the wavelengths for cyclic processes


for example:

consider two possible messages (x, y) that uses some blank state pairs (i, j) of a receiver to transfer the messages.

some transmission medium will use its computation variables (phi, x) and information variables (y, theta) to map (i, phi) to (x, j) or (theta, j) to (i, y) while retaining an instance of the messages itself.

the receiver uses some process that will distinguish between x and y dependending on the computation associated with (phi, theta) and (i, j) where i : phi -> x and j : theta -> y.


the medium creates two equal length buffers called "left" and "right". with a constant radius vector angled as -pi / 2 from the normal axis, a scanning samples the right pole of the sender terminal and continues through to the +pi / 2 away from the normal axis where the changes are copied at the left pole of the receiver terminal and continues clockwise. for the lower half if the circle, the medium completes the switching related configurations such that the next revolution would place the receiver at senders pole and sender at receivers pole.

the object systems have terminals that can operate with both read and write modes. upon connecting to the medium, a buffer gets initialized which has twice the length of the static wavelength, half of which is used for writing changes and the half contains transmissible bytes.