#!/usr/bin/env python3
import threading
import time
import random

def randtime(multiplier = 1):
	time.sleep(random.uniform(0, 0.1 * multiplier))

nchairs = 5

CUTTING = 1
SLEEPING = 2
NOTHING = 3
DONE = 4

class Customer(threading.Thread):
	def __init__(self, wr, barber, id):
		threading.Thread.__init__(self)
		self.wr = wr
		self.barber = barber
		self.id = id
	def run(self):
		print("customer %d takes a waiting chair" % self.id)
		if len(self.wr) >= nchairs:
			print("there is no more room left, customer %d leaves" % self.id)
			return
			
		self.wr.append(self)
		if self.barber.status == SLEEPING:
			print("customer %d sees that barber is sleeping, and wakes him" % self.id)
			self.barber.wake()
	def dismiss(self):
		print("customer %d has a new style, and leaves the shop" % self.id)

class Barber(threading.Thread):
	def __init__(self, wr):
		threading.Thread.__init__(self)
		self.wr = wr
	
	def run(self):
		print("barber has started, and going to sleep")
		self.sleep()
		while self.status != DONE:
			print("barber checks waiting room")
			if len(self.wr) > 0:
				print("\t[", end='')
				[print(str(elem.id) + ', ', end='') if i < len(self.wr) - 1 else print(str(elem.id), end='') for i, elem in enumerate(self.wr)]
				print("]")
				print("\twhich is populated")
				customer = self.wr.pop(0)
				print("\tcustomer %d is chosen to be cut" % customer.id)
				self.cut(customer)
			else:
				self.sleep()
			print("loop")
				
	def cut(self, customer):
		print("barber starts cutting customer %d" % customer.id)
		self.status = CUTTING
		randtime()
		self.status = NOTHING
		print("barber dismisses customer %d" % customer.id)
		customer.dismiss()
		
	def sleep(self):
		print("barber going to sleep")
		self.status = SLEEPING
		while self.status == SLEEPING:
			pass
		print("barber waking up")
	
	def wake(self):
		self.status = NOTHING
	
	def finish(self):
		print("barber is asked to finish")
		self.status = DONE

class Checker(threading.Thread):
	def __init__(self, wr, barber, errors):
		threading.Thread.__init__(self)
		self.wr = wr
		self.barber = barber
		self.errors = errors
		self.check = True
		
	def run(self):
		while self.check:
			if self.wr and self.barber.status == SLEEPING:
				print("!!!!!!!!!!!!!!!!!!!! barber is sleeping when customers are waiting")
				self.errors["sleep"] += 1
			if len(self.wr) > 10:
				print("!!!!!!!!!!!!!!!!!!!! list error")
				self.errors["wr"] += 1
			randtime()

waiting_room = []

threads = []

barber = Barber(waiting_room)

barber.start()
errors = {
	"sleep": 0,
	"wr": 0
}

checker = Checker(waiting_room, barber, errors)
checker.start()

for i in range(1000):
	Customer(waiting_room, barber, i).start()
	randtime(2)

	
while waiting_room:
	pass
	
barber.finish()
barber.join()

print(errors)