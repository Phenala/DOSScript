DOS Attack Python Script
---------------------------------

This repository contains a DoS attack script made in python. In order to run
the script, launch the py script and a prompt will appear for the ip address.

	Enter ip address: 192.168.45.42

When entered a prompt will appear for the port.

	Enter port: 17524

The script will then run an attack on the specified ip address, and display the
status of the attack while doing so.


Design

The script continuously creates threads each of which send connect requests to
the server via the socket module in python. Eventually the server cannot create
any more threads to handle the incoming requests and crashes. Unfortunately,
since Wamp and Xampp servers have precautions in place against such attacks,
it is not quite as effective. However, it is successful when tested with mobile
data transfer servers such as Xender.