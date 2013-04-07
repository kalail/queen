Queen Documentation
===================

Introduction
------------

This is the code that powers the Queen bot for team *Swarm* in Northwestern Univerity's Design Competition.

The Queen bot is part of the *swarm* system which is described below.


Architecture
------------

The Swarm system is designed to implement high level multi-node logic in a robot network where individual node behaviour can be described by a low-state-count state machine.

It is comprised of the following elements:

- **Drone**
	A low-memory, integrated-cpu bot. It implements a simple state machine and manages hardware resources.

- **Queen**
	Bot running on a fast-cpu with no practical memory restrictions. It is the only central authority and decides *Drone* state machine transitions.

- **Swarm**
	A network of 1 queen bot and any number drone bots over a singular communication bus.

Protocol
--------

The **Queen** process is started and immediately goes to sleep for 2 seconds.

The **Drones** are started. Each immediately connect to the **swarm** and wait for the *Heartbeat*.

The **Queen** wakes up and sends out the *Heartbeat*.

Any **Drone** that recieves the *Heartbeat* responds with a *Pulse* containing it's up-to-date *DroneState*.

The **Queen** processes all *Pulse* messages and creates a *ContestState*. It then sends all **Drones** individual *Commands*.

**Drones** perform routines based on recieved *Commands* and then listen for the *Heartbeat* when done.

The **Queen** and the drones then repeat this cycle starting with the queen sending the *Heartbeat* and updating the *ContestState* every iteration.



Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

