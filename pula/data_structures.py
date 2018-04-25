class Stack:
	def __init__ (self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)
	def side_view(self):
		trace = []
		for i in range(len(self.items)):
			trace.append(self.items[i])
		print (list(reversed(trace)))


class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def side_view(self):
		trace = []
		for i in range(len(self.items)):
			trace.append(self.items[i])
		print (list(reversed(trace)))

		
class PriorityQueue:
	def __init__(self):
		self.items = []
		self.priorities = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item, priority):
		self.items.insert(0,item)
		self.priorities.insert(0,priority)
	def dequeue(self):
		position = self.priorities.index(max(self.priorities))
		self.priorities.pop(position)
		return self.items.pop(position)
	def size(self):
		return len(self.items)
	def side_view(self):
		item_trace = []
		priority_trace = []
		for i in range(len(self.items)):
			item_trace.append(self.items[i])
			priority_trace.append(self.priorities[i])
		print (list(reversed(item_trace)))
		print(list(reversed(priority_trace)))