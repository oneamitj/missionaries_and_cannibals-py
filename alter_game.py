# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''

@Author Amit Joshi

'''

class bcolors:
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLACK = '\033[0m'

class cannibal:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def isStart(self):
		return self.start

	def isEnd(self):
		return self.end

	def goStart(self):
		if self.end == 1:
			self.start = 1
			self.end = 0
		else:
			return "AT START"

	def goEnd(self):
		if self.start == 1:
			self.start = 0
			self.end = 1
		else:
			return "AT END"

	def position(self):
		if self.start == 1:
			return "start"
		elif self.end == 1:
			return "end"


class machinery:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def isStart(self):
		return self.start

	def isEnd(self):
		return self.end

	def goStart(self):
		if self.end == 1:
			self.start = 1
			self.end = 0
		else:
			return "AT START"

	def goEnd(self):
		if self.start == 1:
			self.start = 0
			self.end = 1
		else:
			return "AT END"

	def position(self):
		if self.start == 1:
			return "start"
		elif self.end == 1:
			return "end"

class boat:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def isStart(self):
		return self.start

	def isEnd(self):
		return self.end

	def goStart(self):
		if self.end == 1:
			self.start = 1
			self.end = 0
		else:
			return "AT START"

	def goEnd(self):
		if self.start == 1:
			self.start = 0
			self.end = 1
		else:
			return "AT END"

	def position(self):
		if self.start == 1:
			return "start"
		elif self.end == 1:
			return "end"
		

def count(can, mac):
	counter = [0,0,0,0]
	for i in range(len(can)):
		if can[i].position() == 'start':
			counter[1] += 1
		elif can[i].position() == 'end':
			counter[3] += 1

	for i in range(len(mac)):
		if mac[i].position() == 'start':
			counter[0] += 1
		elif mac[i].position() == 'end':
			counter[2] += 1
	return counter

def prt(can, mac):
	print "mac_1", mac[0].position()
	print "mac_2", mac[1].position()
	print "mac_3", mac[2].position()

	print "can_1", can[0].position()
	print "can_2", can[1].position()
	print "can_3", can[2].position()


def check(can, mac):
	# prt(can, mac)
	counter = count(can, mac)
	print counter
	if ship.position() == "start": boat_position =  bcolors.BLUE + " ==river==" + bcolors.VIOLET + "((__boat__)) " + bcolors.BLACK
	elif ship.position() == "end": boat_position =  bcolors.VIOLET + " ((__boat__))" + bcolors.BLUE + "==river== " + bcolors.BLACK

	print bcolors.RED + ' Ç'*counter[3] + bcolors.GREEN + ' ᵯ'*counter[2] + bcolors.BLACK +  boat_position + bcolors.GREEN + ' ᵯ'*counter[0] + bcolors.RED + ' Ç'*counter[1] + bcolors.BLACK
	if counter[0]<counter[1] and counter[0]>0:
		print "GAME OVER!!!\n"
		exit(1)
		return 0
	elif counter[2]<counter[3] and counter[2]>0:
		print "GAME OVER!!!\n"
		exit(1)
		return 0
	elif counter[2] == 3 and counter[3] == 3:
		print "COMPLETE SUCCESS!!!\n"
		# exit(1)
		return 3
	else:
		# print "PASS!!!\n"
		return 1


def move(*data):
	pos = ship.position()
	for obj in data:
		if obj.position() != pos:
			print "invalid move"
			exit(1)
			return 0

	if pos == 'start':
		for obj in data:
			obj.goEnd()
		ship.goEnd()
		print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
	elif pos == 'end':
		for obj in data:
			obj.goStart()
		ship.goStart()
		print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
	check(can, mac)
	# print
	return 0


def initialize():
	[can[0].goStart(), can[1].goStart(), can[2].goStart()]
	[mac[0].goStart(), mac[1].goStart(), mac[2].goStart()]
	ship.goStart()
	play()

can = [cannibal(1,0), cannibal(1,0), cannibal(1,0)]
mac = [machinery(1,0), machinery(1,0), machinery(1,0)]
ship = boat(1,0)

def game():
	choice = raw_input("1. Let it play\n2. I want to play\n3. Quit\nChoice(1/2/3)::")
	print


	if choice == '1':
		check(can, mac)

		move(can[0],can[1])
		
		move(can[1])
		
		move(can[1],can[2])
		
		move(can[2])
		
		move(mac[0],mac[1])
		
		move(mac[1],can[1])
		
		move(mac[1], mac[2])
		
		move(can[0])
		
		move(can[0],can[1])
		
		move(can[1])

		move(can[1],can[2])

	elif choice == '2':
		initialize()
		play()

	elif choice == '3':
		return 0

	game()

def play():

	obj1 = raw_input("Select 1st {(c/m)(0/1/2)}::")
	obj2 = raw_input("Select 2nd::")
	
	check(can, mac)	
	
	if obj1 == '' and obj2 == '':
		print "INVALID SELECTION!!!\nEnter Again!!!\n"
		play()
	elif obj1 == '':
		if obj2[0] == 'c':
			move(can[int(obj2[1])])
		elif obj2[0] == 'm':
			move(mac[int(obj2[1])])
	elif obj2 == '':
		if obj1[0] == 'c':
			move(can[int(obj1[1])])
		elif obj1[0] == 'm':
			move(mac[int(obj1[1])])
	elif obj1[0] == 'c' and obj2[0] == 'c':
		move(can[int(obj1[1])], can[int(obj2[1])])

	elif obj1[0] == 'm' and obj2[0] == 'm':
		move(mac[int(obj1[1])], mac[int(obj2[1])])

	elif obj1[0] == 'm' and obj2[0] == 'c':
		move(mac[int(obj1[1])], can[int(obj2[1])])

	elif obj1[0] == 'c' and obj2[0] == 'm':
		move(can[int(obj1[1])], mac[int(obj2[1])])
	elif obj1 == None:
		print "NONE"


	play()
	
	initialize()

	print count(can, mac)

	return 0




game()
