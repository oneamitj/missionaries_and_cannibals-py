# !/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue

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


class objects:
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
        

def count():
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

def prt():
    print "mac_1", mac[0].position()
    print "mac_2", mac[1].position()
    print "mac_3", mac[2].position()

    print "can_1", can[0].position()
    print "can_2", can[1].position()
    print "can_3", can[2].position()


def check(*data):
    # prt()
    counter = count()
    obj = ['', '']
    for i in range(len(data)):
        obj[i] = data[i]

    if ship.position() == "start": boat_position =  bcolors.BLUE + " ==river==" + bcolors.VIOLET + "((__boat__)) " + bcolors.BLACK
    elif ship.position() == "end": boat_position =  bcolors.VIOLET + " ((__boat__))" + bcolors.BLUE + "==river== " + bcolors.BLACK

    print bcolors.RED + ' Ç'*counter[3] + bcolors.GREEN + ' ᵯ'*counter[2] + bcolors.BLACK +  boat_position + bcolors.GREEN + ' ᵯ'*counter[0] + bcolors.RED + ' Ç'*counter[1] + bcolors.BLACK
    if counter[0]<counter[1] and counter[0]>0:
        print bcolors.RED+"#################### GAME OVER!!! ##########################"+bcolors.BLACK
        print "-------------- BACKTRACK TO PREVIOUS STATE -----------------"
        return "BT"

    elif counter[2]<counter[3] and counter[2]>0:
        print "GAME OVER!!!\n"
        print "BACKTRACK"
        return "BT"

    elif counter[2] == 3 and counter[3] == 3:
        print "COMPLETE SUCCESS!!!\n"
        print "Algorithm Used:: DFS Search and Recursive Backtracking"
        print "Final solution states and moves are::\n"
        while(not q_success.empty()):
            print q_success.get()
        print counter, "SOLVED"
        exit(1)
        return 3
    else:
        # print "PASS!!!\n"
        return 1

    return 0


def move(*data):
    pos = ship.position()
    for obj in data:
        if obj.position() != pos:
            print "invalid select"
            # exit(1)
            play()
            return 0

    if pos == 'start':
        for obj in data:
            obj.goEnd()
        ship.goEnd()
    elif pos == 'end':
        for obj in data:
            obj.goStart()
        ship.goStart()

    return check(*data)

def state_move(state):
    counter = count()

    if ship.position() == 'start':
        if counter[0] >= state[0] and counter[1] >= state[1]:
            q_state.put(state)
            print state
        else:
            # print 'x'+ str(state)
            pass

    elif ship.position() == 'end':
        if counter[2] >= state[0] and counter[3] >= state[1]:
            q_state.put(state)
            print state
        else:
            # print 'x'+ str(state)
            pass
    return 0

def initialize():
    [can[0].goStart(), can[1].goStart(), can[2].goStart()]
    [mac[0].goStart(), mac[1].goStart(), mac[2].goStart()]
    ship.goStart()
    for c in can:
        q_can_start.put(c)

    for m in mac:
        q_mac_start.put(m)

    play()
    return 0

ship = objects(1,0)
can = [objects(1,0), objects(1,0), objects(1,0)]
mac = [objects(1,0), objects(1,0), objects(1,0)]
q_state = Queue.LifoQueue()
q_can_start = Queue.Queue()
q_mac_start = Queue.Queue()
q_can_end = Queue.Queue()
q_mac_end = Queue.Queue()
q_success = Queue.Queue()




def check_state(*st):
    s = [[0,1], [1,0], [0, 2], [1,1], [2,0]]

    for state in s:
        if st[0] == state:
            continue
        else:
            state_move(state)

    print

def play():
    check()
    check_state([0, 0])
    x = 0
    level = 0

    
    while(not q_state.empty()):
    	if level<0:
            level=0
        counter = count()
        state = q_state.get()
        print "\n**************************LEVEL:", level, "**********************************"
        obj = ['','']
        print state
        cnt = 0

        if ship.position() == 'start':
            for i in range(int(state[0])):
                obj[cnt] = q_mac_start.get()
                q_mac_end.put(obj[cnt])
                cnt = cnt + 1

            for i in range(int(state[1])):
                obj[cnt] = q_can_start.get()
                q_can_end.put(obj[cnt])        
                cnt = cnt + 1

        if ship.position() == 'end':
            for i in range(int(state[0])):
                obj[cnt] = q_mac_end.get()
                q_mac_start.put(obj[cnt])
                cnt = cnt + 1

            for i in range(int(state[1])):
                obj[cnt] = q_can_end.get()        
                q_can_start.put(obj[cnt])
                cnt = cnt + 1

        if obj[1] == '':
            chk = move(obj[0])
        else:
            chk = move(obj[0], obj[1])

        # print chk, state

        if chk == "BT":
            cnt = 0
            if ship.position() == 'start':
                for i in range(int(state[0])):
                    obj[cnt] = q_mac_start.get()
                    q_mac_end.put(obj[cnt])
                    cnt = cnt + 1

                for i in range(int(state[1])):
                    obj[cnt] = q_can_start.get()
                    q_can_end.put(obj[cnt])        
                    cnt = cnt + 1

            if ship.position() == 'end':
                for i in range(int(state[0])):
                    obj[cnt] = q_mac_end.get()
                    q_mac_start.put(obj[cnt])
                    cnt = cnt + 1

                for i in range(int(state[1])):
                    obj[cnt] = q_can_end.get()        
                    q_can_start.put(obj[cnt])
                    cnt = cnt + 1                
            
            if obj[1] == '':
                chk = move(obj[0])
            else:
                chk = move(obj[0], obj[1])

            level = level -1
        else:
            side = ""
            if x%2 == 0:
                side = "from START to END "
            else: side = "from END to START "
                
            q_success.put("current state: " + str(counter) + "\tmove: " + side + str(state[0]) + " machinery " + str(state[1]) + " cannibal")
            x = x+1
            check_state(state)

            level = level + 1
            
    return 0

initialize()
