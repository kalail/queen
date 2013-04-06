Queen Documentation
===================

Introduction
------------

This is the code that powers the Queen bot for team *Swarm* in Northwestern Univerity's Design Competition.

The Queen bot is part of the *swarm* system which is described below.


Architecture
------------

The Swarm system is designed to easily implement high level multi-node logic in robot networks where individual node behaviour can be described by a low-state-count state machine.

It is comprised of the following elements:

- **Drone**
	A psuedo-dumb bot. It implements a simple state machine managing appropriate hardware resources.

- **Queen**
	Smart bot that decides *Drone* state machine transitions and can run arbritrary code.

- **Swarm**
	A network of at most 1 queen bot and infinite drone bots over a singular communication bus. 

Protocol
--------

The **Queen** periodically sends out the *ready packet* when it is free.

**Drones** send the *basic packet* when they recieve the *ready packet*.

The **Queen** recieves the first response and converses with the **Drone** using *command* and *info packets*.

Once the conversation is finished, the **Queen** will broadcast the *ready packet*.

A **Drone** will not respond to consecutive *ready packets*.


Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

