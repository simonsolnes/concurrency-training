#!/usr/bin/env python3
import threading
import time
import random

def randtime(multiplier = 1):
	time.sleep(random.uniform(0, 0.1 * multiplier))

print('Finished eating!')
