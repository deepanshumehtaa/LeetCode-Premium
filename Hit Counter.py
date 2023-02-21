from collections import deque
import time



# flushing Queue ie. left part, before some index ..............................

queue = deque([1, 2, 3, 4, 5, 6])
purge_till_idx = 3

# poping the element till `purge_till_idx`
while len(queue) > purge_till_idx:
    queue.popleft()

print(queue)


## ...................................................................................

class HitCounter:

    duration = 100

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        self.hits.append(timestamp)
        
    # def get_hits_in_last_5_minutes(self):
    #     now_dt = time.now()
    #     while self.hits and now_dt - self.hits[0] >= HitCounter.duration:
    #         self.hits.popleft()
    #     print(f"Number of Hits: {len(self.hits)}")

    def my_get_hits_in_last_5_minutes(self, current_dt):

    	# flushing old data from the queue
   		while self.hits and current_dt - self.hits[0] >= HitCounter.duration:
   			self.hits.popleft()
   		
   		# what left in the queue is the result
   		print(f"Number of Hits: {len(self.hits)}")



hc = HitCounter()
for i in range(1, 200):
    hc.hit(i)

hc.my_get_hits_in_last_5_minutes(current_dt=220)



## Design Principle ..................................................................................


class HitCounterSingleton:
	_instance = None
	duration = 100

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.hits = deque()

		return cls._instance

	def hit(self, timestamp):
		self.hits.append(timestamp)
        
    # def get_hits_in_last_5_minutes(self):
    #     now_dt = time.now()
    #     while self.hits and now_dt - self.hits[0] >= HitCounter.duration:
    #         self.hits.popleft()
    #     print(f"Number of Hits: {len(self.hits)}")


	def my_get_hits_in_last_5_minutes(self, current_dt):

		# flushing old data from the queue
		while self.hits and current_dt - self.hits[0] >= HitCounter.duration:
			self.hits.popleft()
   		
   	# what left in the queue is the result
		print(f"Number of Hits: {len(self.hits)}")


hc1 = HitCounterSingleton()
for i in range(1, 200):
    hc1.hit(i)

hc1.my_get_hits_in_last_5_minutes(current_dt=220)

hc2 = HitCounterSingleton()
for i in range(1, 200):
    hc2.hit(i)


# The result is the summation of both the objects
hc2.my_get_hits_in_last_5_minutes(current_dt=220)

