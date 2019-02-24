#! /usr/bin/env python
# change permissions with chmod +x
#
#
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)



##############################################################
# UPPER ARM MOTION DATA
##############################################################


UpperArmMovements = [
	
	["HeadPitch",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[
	[-0.170316, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.199461, [3, -0.386667, 0], [3, 0.4, 0]], [-0.199461, [3, -0.4, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.4, 0]], [-0.204064, [3, -0.4, 0], [3, 0.4, 0]], [-0.199461, [3, -0.4, 0], [3, 0.4, 0]], [-0.204064, [3, -0.4, 0], [3, 0.4, 0]], [-0.199461, [3, -0.4, 0], [3, 0.2, 0]], [-0.204064, [3, -0.2, 0], [3, 0.2, 0]], [-0.199461, [3, -0.2, 0], [3, 0.2, 0]], [-0.204064, [3, -0.2, 0], [3, 0.2, 0]], [-0.199461, [3, -0.2, 0], [3, 0.4, 0]], [-0.204064, [3, -0.4, 0], [3, 0.4, 0]], [-0.199461, [3, -0.4, 0], [3, 0.4, 0]], [-0.204064, [3, -0.4, 0], [3, 0.4, 0]], [-0.199461, [3, -0.4, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.6, 0]], [-0.204064, [3, -0.6, 0], [3, 0.6, 0]], [-0.199461, [3, -0.6, 0], [3, 0.4, 0]], [-0.199461, [3, -0.4, 0], [3, 0.4, 0]], [-0.170316, [3, -0.4, 0], [3, 0, 0]]]
	],

	["HeadYaw",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[-0.0138481, [3, -0.0133333, 0], [3, 0.386667, 0]], [0, [3, -0.386667, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.6, 0]], [0, [3, -0.6, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]], [-0.0138481, [3, -0.4, 0], [3, 0, 0]]]],

	["LElbowRoll",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[-1.44959, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.782298, [3, -0.386667, -0.186992], [3, 0.4, 0.19344]], [-0.308291, [3, -0.4, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.4, 0]], [-0.406468, [3, -0.4, 0], [3, 0.4, 0]], [-0.308291, [3, -0.4, 0], [3, 0.4, 0]], [-0.406468, [3, -0.4, 0], [3, 0.4, 0]], [-0.308291, [3, -0.4, 0], [3, 0.2, 0]], [-0.406468, [3, -0.2, 0], [3, 0.2, 0]], [-0.308291, [3, -0.2, 0], [3, 0.2, 0]], [-0.406468, [3, -0.2, 0], [3, 0.2, 0]], [-0.308291, [3, -0.2, 0], [3, 0.4, 0]], [-0.406468, [3, -0.4, 0], [3, 0.4, 0]], [-0.308291, [3, -0.4, 0], [3, 0.4, 0]], [-0.406468, [3, -0.4, 0], [3, 0.4, 0]], [-0.308291, [3, -0.4, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.6, 0]], [-0.406468, [3, -0.6, 0], [3, 0.6, 0]], [-0.308291, [3, -0.6, 0], [3, 0.4, 0]], [-0.782298, [3, -0.4, 0.190216], [3, 0.4, -0.190216]], [-1.44959, [3, -0.4, 0], [3, 0, 0]]]],

	["LElbowYaw",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[-1.22111, [3, -0.0133333, 0], [3, 0.386667, 0]], [-1.23645, [3, -0.386667, 0], [3, 0.4, 0]], [-0.366667, [3, -0.4, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.4, 0]], [-0.630516, [3, -0.4, 0], [3, 0.4, 0]], [-0.366667, [3, -0.4, 0], [3, 0.4, 0]], [-0.630516, [3, -0.4, 0], [3, 0.4, 0]], [-0.366667, [3, -0.4, 0], [3, 0.2, 0]], [-0.630516, [3, -0.2, 0], [3, 0.2, 0]], [-0.366667, [3, -0.2, 0], [3, 0.2, 0]], [-0.630516, [3, -0.2, 0], [3, 0.2, 0]], [-0.366667, [3, -0.2, 0], [3, 0.4, 0]], [-0.630516, [3, -0.4, 0], [3, 0.4, 0]], [-0.366667, [3, -0.4, 0], [3, 0.4, 0]], [-0.630516, [3, -0.4, 0], [3, 0.4, 0]], [-0.366667, [3, -0.4, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.6, 0]], [-0.630516, [3, -0.6, 0], [3, 0.6, 0]], [-0.366667, [3, -0.6, 0], [3, 0.4, 0]], [-1.23645, [3, -0.4, 0], [3, 0.4, 0]], [-1.21957, [3, -0.4, 0], [3, 0, 0]]]],

	["LHand",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[0.0196, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.3532, [3, -0.386667, -0.104728], [3, 0.4, 0.108339]], [0.6588, [3, -0.4, -0.06016], [3, 0.6, 0.09024]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.4, 0]], [0.8044, [3, -0.4, 0], [3, 0.4, 0]], [0.6588, [3, -0.4, 0], [3, 0.4, 0]], [0.8044, [3, -0.4, 0], [3, 0.4, 0]], [0.6588, [3, -0.4, 0], [3, 0.2, 0]], [0.8044, [3, -0.2, 0], [3, 0.2, 0]], [0.6588, [3, -0.2, 0], [3, 0.2, 0]], [0.8044, [3, -0.2, 0], [3, 0.2, 0]], [0.6588, [3, -0.2, 0], [3, 0.4, 0]], [0.8044, [3, -0.4, 0], [3, 0.4, 0]], [0.6588, [3, -0.4, 0], [3, 0.4, 0]], [0.8044, [3, -0.4, 0], [3, 0.4, 0]], [0.6588, [3, -0.4, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0], [3, 0.6, 0]], [0.8044, [3, -0.6, 0], [3, 0.6, 0]], [0.6588, [3, -0.6, 0.09024], [3, 0.4, -0.06016]], [0.3532, [3, -0.4, 0.105733], [3, 0.4, -0.105733]], [0.0244, [3, -0.4, 0], [3, 0, 0]]]],


	["LShoulderPitch",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[1.35448, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.783916, [3, -0.386667, 0.326231], [3, 0.4, -0.33748]], [-1.1214, [3, -0.4, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.4, 0]], [-1.09839, [3, -0.4, 0], [3, 0.4, 0]], [-1.1214, [3, -0.4, 0], [3, 0.4, 0]], [-1.09839, [3, -0.4, 0], [3, 0.4, 0]], [-1.1214, [3, -0.4, 0], [3, 0.2, 0]], [-1.09839, [3, -0.2, 0], [3, 0.2, 0]], [-1.1214, [3, -0.2, 0], [3, 0.2, 0]], [-1.09839, [3, -0.2, 0], [3, 0.2, 0]], [-1.1214, [3, -0.2, 0], [3, 0.4, 0]], [-1.09839, [3, -0.4, 0], [3, 0.4, 0]], [-1.1214, [3, -0.4, 0], [3, 0.4, 0]], [-1.09839, [3, -0.4, 0], [3, 0.4, 0]], [-1.1214, [3, -0.4, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.6, 0]], [-1.09839, [3, -0.6, 0], [3, 0.6, 0]], [-1.1214, [3, -0.6, 0], [3, 0.4, 0]], [-0.783916, [3, -0.4, -0.33748], [3, 0.4, 0.33748]], [1.36215, [3, -0.4, 0], [3, 0, 0]]]],

	["LShoulderRoll",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[0.130348, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.184038, [3, -0.386667, 0], [3, 0.4, 0]], [-0.29457, [3, -0.4, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.4, 0]], [0.800706, [3, -0.4, 0], [3, 0.4, 0]], [-0.29457, [3, -0.4, 0], [3, 0.4, 0]], [0.800706, [3, -0.4, 0], [3, 0.4, 0]], [-0.29457, [3, -0.4, 0], [3, 0.2, 0]], [0.800706, [3, -0.2, 0], [3, 0.2, 0]], [-0.29457, [3, -0.2, 0], [3, 0.2, 0]], [0.800706, [3, -0.2, 0], [3, 0.2, 0]], [-0.29457, [3, -0.2, 0], [3, 0.4, 0]], [0.800706, [3, -0.4, 0], [3, 0.4, 0]], [-0.29457, [3, -0.4, 0], [3, 0.4, 0]], [0.800706, [3, -0.4, 0], [3, 0.4, 0]], [-0.29457, [3, -0.4, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.6, 0]], [0.800706, [3, -0.6, 0], [3, 0.6, 0]], [-0.29457, [3, -0.6, 0], [3, 0.4, 0]], [0.184038, [3, -0.4, 0], [3, 0.4, 0]], [0.139552, [3, -0.4, 0], [3, 0, 0]]]],

	["LWristYaw",	
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[0.0367741, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.00455999, [3, -0.386667, 0], [3, 0.4, 0]], [0.260738, [3, -0.4, -0.0533832], [3, 0.6, 0.0800748]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.4, 0]], [0.404934, [3, -0.4, 0], [3, 0.4, 0]], [0.260738, [3, -0.4, 0], [3, 0.4, 0]], [0.404934, [3, -0.4, 0], [3, 0.4, 0]], [0.260738, [3, -0.4, 0], [3, 0.2, 0]], [0.404934, [3, -0.2, 0], [3, 0.2, 0]], [0.260738, [3, -0.2, 0], [3, 0.2, 0]], [0.404934, [3, -0.2, 0], [3, 0.2, 0]], [0.260738, [3, -0.2, 0], [3, 0.4, 0]], [0.404934, [3, -0.4, 0], [3, 0.4, 0]], [0.260738, [3, -0.4, 0], [3, 0.4, 0]], [0.404934, [3, -0.4, 0], [3, 0.4, 0]], [0.260738, [3, -0.4, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0], [3, 0.6, 0]], [0.404934, [3, -0.6, 0], [3, 0.6, 0]], [0.260738, [3, -0.6, 0.0800748], [3, 0.4, -0.0533832]], [0.00455999, [3, -0.4, 0], [3, 0.4, 0]], [0.033706, [3, -0.4, 0], [3, 0, 0]]]],


	["RElbowRoll",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[1.44047, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.771643, [3, -0.386667, 0.193778], [3, 0.4, -0.20046]], [0.257754, [3, -0.4, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.4, 0]], [0.331386, [3, -0.4, 0], [3, 0.4, 0]], [0.257754, [3, -0.4, 0], [3, 0.4, 0]], [0.331386, [3, -0.4, 0], [3, 0.4, 0]], [0.257754, [3, -0.4, 0], [3, 0.2, 0]], [0.331386, [3, -0.2, 0], [3, 0.2, 0]], [0.257754, [3, -0.2, 0], [3, 0.2, 0]], [0.331386, [3, -0.2, 0], [3, 0.2, 0]], [0.257754, [3, -0.2, 0], [3, 0.4, 0]], [0.331386, [3, -0.4, 0], [3, 0.4, 0]], [0.257754, [3, -0.4, 0], [3, 0.4, 0]], [0.331386, [3, -0.4, 0], [3, 0.4, 0]], [0.257754, [3, -0.4, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.6, 0]], [0.331386, [3, -0.6, 0], [3, 0.6, 0]], [0.257754, [3, -0.6, 0], [3, 0.4, 0]], [0.771643, [3, -0.4, -0.198397], [3, 0.4, 0.198397]], [1.44814, [3, -0.4, 0], [3, 0, 0]]]],

	["RElbowYaw",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[1.22256, [3, -0.0133333, 0], [3, 0.386667, 0]], [1.27318, [3, -0.386667, 0], [3, 0.4, 0]], [1.00626, [3, -0.4, 0.0640189], [3, 0.6, -0.0960284]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.4, 0]], [0.793036, [3, -0.4, 0], [3, 0.4, 0]], [1.00626, [3, -0.4, 0], [3, 0.4, 0]], [0.793036, [3, -0.4, 0], [3, 0.4, 0]], [1.00626, [3, -0.4, 0], [3, 0.2, 0]], [0.793036, [3, -0.2, 0], [3, 0.2, 0]], [1.00626, [3, -0.2, 0], [3, 0.2, 0]], [0.793036, [3, -0.2, 0], [3, 0.2, 0]], [1.00626, [3, -0.2, 0], [3, 0.4, 0]], [0.793036, [3, -0.4, 0], [3, 0.4, 0]], [1.00626, [3, -0.4, 0], [3, 0.4, 0]], [0.793036, [3, -0.4, 0], [3, 0.4, 0]], [1.00626, [3, -0.4, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, 0], [3, 0.6, 0]], [0.793036, [3, -0.6, 0], [3, 0.6, 0]], [1.00626, [3, -0.6, -0.0960284], [3, 0.4, 0.0640189]], [1.27318, [3, -0.4, 0], [3, 0.4, 0]], [1.22409, [3, -0.4, 0], [3, 0, 0]]]],

	["RHand",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[0.0228, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.312, [3, -0.386667, -0.106628], [3, 0.4, 0.110305]], [0.6736, [3, -0.4, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.2, 0]], [0.6736, [3, -0.2, 0], [3, 0.2, 0]], [0.6736, [3, -0.2, 0], [3, 0.2, 0]], [0.6736, [3, -0.2, 0], [3, 0.2, 0]], [0.6736, [3, -0.2, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.4, 0]], [0.6736, [3, -0.4, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.6, 0]], [0.6736, [3, -0.6, 0], [3, 0.4, 0]], [0.312, [3, -0.4, 0.107733], [3, 0.4, -0.107733]], [0.0272, [3, -0.4, 0], [3, 0, 0]]]],

	["RShoulderPitch",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[1.35763, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.754686, [3, -0.386667, 0.240225], [3, 0.4, -0.248509]], [-1.00319, [3, -0.4, 0.0153403], [3, 0.6, -0.0230104]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.4, 0]], [-1.0262, [3, -0.4, 0], [3, 0.4, 0]], [-1.00319, [3, -0.4, 0], [3, 0.4, 0]], [-1.0262, [3, -0.4, 0], [3, 0.4, 0]], [-1.00319, [3, -0.4, 0], [3, 0.2, 0]], [-1.0262, [3, -0.2, 0], [3, 0.2, 0]], [-1.00319, [3, -0.2, 0], [3, 0.2, 0]], [-1.0262, [3, -0.2, 0], [3, 0.2, 0]], [-1.00319, [3, -0.2, 0], [3, 0.4, 0]], [-1.0262, [3, -0.4, 0], [3, 0.4, 0]], [-1.00319, [3, -0.4, 0], [3, 0.4, 0]], [-1.0262, [3, -0.4, 0], [3, 0.4, 0]], [-1.00319, [3, -0.4, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, 0], [3, 0.6, 0]], [-1.0262, [3, -0.6, 0], [3, 0.6, 0]], [-1.00319, [3, -0.6, -0.0230104], [3, 0.4, 0.0153403]], [-0.754686, [3, -0.4, -0.248509], [3, 0.4, 0.248509]], [1.35763, [3, -0.4, 0], [3, 0, 0]]]],

	["RShoulderRoll",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[-0.14117, [3, -0.0133333, 0], [3, 0.386667, 0]], [-0.289967, [3, -0.386667, 0.0902287], [3, 0.4, -0.0933401]], [-0.691876, [3, -0.4, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.4, 0]], [0.309826, [3, -0.4, 0], [3, 0.4, 0]], [-0.691876, [3, -0.4, 0], [3, 0.4, 0]], [0.309826, [3, -0.4, 0], [3, 0.4, 0]], [-0.691876, [3, -0.4, 0], [3, 0.2, 0]], [0.309826, [3, -0.2, 0], [3, 0.2, 0]], [-0.691876, [3, -0.2, 0], [3, 0.2, 0]], [0.309826, [3, -0.2, 0], [3, 0.2, 0]], [-0.691876, [3, -0.2, 0], [3, 0.4, 0]], [0.309826, [3, -0.4, 0], [3, 0.4, 0]], [-0.691876, [3, -0.4, 0], [3, 0.4, 0]], [0.309826, [3, -0.4, 0], [3, 0.4, 0]], [-0.691876, [3, -0.4, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.6, 0]], [0.309826, [3, -0.6, 0], [3, 0.6, 0]], [-0.691876, [3, -0.6, 0], [3, 0.4, 0]], [-0.289967, [3, -0.4, -0.0928071], [3, 0.4, 0.0928071]], [-0.135034, [3, -0.4, 0], [3, 0, 0]]]],

	["RWristYaw",
	[0.04, 1.2, 2.4, 4.2, 6, 7.8, 9.6, 10.8, 12, 13.2, 14.4, 15, 15.6, 16.2, 16.8, 18, 19.2, 20.4, 21.6, 23.4, 25.2, 27, 28.8, 30, 31.2],
	[[0.059784, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.0705221, [3, -0.386667, 0], [3, 0.4, 0]], [-0.428028, [3, -0.4, 0.0904037], [3, 0.6, -0.135606]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.4, 0]], [-0.607505, [3, -0.4, 0], [3, 0.4, 0]], [-0.428028, [3, -0.4, 0], [3, 0.4, 0]], [-0.607505, [3, -0.4, 0], [3, 0.4, 0]], [-0.428028, [3, -0.4, 0], [3, 0.2, 0]], [-0.607505, [3, -0.2, 0], [3, 0.2, 0]], [-0.428028, [3, -0.2, 0], [3, 0.2, 0]], [-0.607505, [3, -0.2, 0], [3, 0.2, 0]], [-0.428028, [3, -0.2, 0], [3, 0.4, 0]], [-0.607505, [3, -0.4, 0], [3, 0.4, 0]], [-0.428028, [3, -0.4, 0], [3, 0.4, 0]], [-0.607505, [3, -0.4, 0], [3, 0.4, 0]], [-0.428028, [3, -0.4, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, 0], [3, 0.6, 0]], [-0.607505, [3, -0.6, 0], [3, 0.6, 0]], [-0.428028, [3, -0.6, -0.135606], [3, 0.4, 0.0904037]], [0.0705221, [3, -0.4, 0], [3, 0.4, 0]], [0.059784, [3, -0.4, 0], [3, 0, 0]]]]

]




##############################################################
# MOTION DATA LISTS
##############################################################


ArmMovementList = [UpperArmMovements]

##############################################################




import argparse
from naoqi import ALProxy
from pprint import pprint

def main(robotIP, PORT=9559):
    	""" Simple code to test above motion data. """
    	# Choregraphe simplified export in Python.
    	motion  = ALProxy("ALMotion", robotIP, PORT)
    	posture = ALProxy("ALRobotPosture", robotIP, PORT)
	ttsProxy = ALProxy("ALTextToSpeech", robotIP, PORT)
	asp = ALProxy('ALAnimatedSpeech', robotIP, PORT)
    
	#conf={'bodyLanguageMode':'contextual'}
	#asp.say('Hello, I am Nao', conf)

    	asp.say("Hiya, My name is super NAO")
    	asp.say("You are going to imitate the following upper arm movements")
    	asp.say("Are you ready?")
    	asp.say("Let's start")

	

	testList = ArmMovementList
	bezier = True
	
 	motion.wakeUp()
   	 # posture.goToPosture("StandInit", 0.8)


    	for i in range(len(testList)):
        	names = list()
        	times = list()
        	keys = list()
	
	for n, t, k in testList[i]:
        	names.append(n)
            	times.append(t)
            	keys.append(k)
	
	if bezier:
        	motion.angleInterpolationBezier(names, times, keys)
	else:
		motion.angleInterpolation(names, keys, times, True)


    	# Go to rest position
    	motion.rest()

	ttsProxy.say("Wow ")
    	ttsProxy.say('That was cool!')
    	ttsProxy.say("Thank you very much")




if __name__ == "__main__":
	parser = argparse.ArgumentParser()
    	parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    	#parser.add_argument("--ip", type=str, default="169.254.228.148", help="Robot ip address")
    	parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    	args = parser.parse_args()
    	main(args.ip, args.port)

