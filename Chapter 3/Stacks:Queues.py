
class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def peak(self):
		if self.head == None:
			return None
		return self.head.value

	def push(self, value):
		node = Node(value)
		node.next = self.head
		self.head = node

	def pop(self):
		if self.head == None:
			return None
		res = self.head 
		self.head = self.head.next
		return res

	def asArray(self):
		arr = []
		tmp = self.head
		while tmp != None:
			arr.append(tmp.value)
			tmp = tmp.next
		return arr
# 3.1
class NStack:

	def __init__(self, numStacks):
		self.arr = [None]*numStacks
		self.ind = [x for x in range(numStacks)]

	def push(self, value, stack):
		if stack > len(self.arr):
			raise Exception("There aren't that many stacks")

		stack -= 1

		if self.arr[self.ind[stack]] == None:
			self.arr[self.ind[stack]] = value
		else:
			self.arr.insert(self.ind[stack] + 1, value)
			for i in range(stack, len(self.ind)):
				self.ind[i] += 1

	def pop(self, stack):
		if stack > len(self.arr):
			raise Exception("There aren't that many stacks")

		stack -= 1

		val = self.arr[self.ind[stack]]

		if self.ind[stack] == stack:
			self.arr[self.ind[stack]] = None

		else:
			del self.arr[self.ind[stack]]
			for i in range(stack, len(self.ind)):
				self.ind[i] -= 1

		return val

# 3.2

class minStack:

	def __init__(self):
		self.stck = LinkedList()

	def peak(self):
		return self.stck.peak()

	def push(self, value):
		if self.stck.peak == value:
			return
		self.stck.push(value)

	def pop(self):
		return self.stck.pop()

class Stack:

	def __init__(self):
		self.lst = LinkedList()
		self.minStck = minStack()
		self.size = 0

	def push(self, value):
		self.lst.push(value)
		if self.minStck.peak() == None or value < self.minStck.peak():
			self.minStck.push(value)
		else:
			self.minStck.push(self.minStck.peak())
		self.size += 1

	def pop(self):
		self.minStck.pop()
		item = self.lst.pop()
		if item != None:
			self.size -= 1
		return item

	def min(self):
		return self.minStck.peak()
# 3.3
class SetOfStacks:

	def __init__(self, size):
		self.stacks = []
		self.size = size

	def push(self, value):
		if len(self.stacks) == 0 or len(self.stacks[-1]) == self.size:
			self.stacks.append([])
		self.stacks[-1].append(value)

	def pop(self):
		if len(self.stacks) == 0:
			return None

		value = self.stacks[-1][-1]

		del self.stacks[-1][-1]

		if len(self.stacks[-1]) == 0:
			del self.stacks[-1]

		return value
# 3.4
class TowersOfHanoi:

	def __init__(self, stack):
		self.rods = [stack, Stack(), Stack()]
		self.n    = stack.size

	def solve():
		if self.rods[2].size == self.n:
			return self.rods
		for i in range(3):
			pass
# 3.5
class MyQueue:

	def __init__(self):
		self.inStack = Stack()
		self.outStack = Stack()

	def enqueue(self, value):
		self.inStack.push(value)

	def dequeue(self):
		if self.outStack.size == 0:
			while self.inStack.size != 0:
				val = self.inStack.pop()
				self.outStack.push(val.value)
		node = self.outStack.pop()
		if node == None:
			return node
		return node.value

# 3.6
def sortStack(stack):
	# tower of hanoi it ?
class Tests:

	def execute(self):
		self.testNStack()
		self.testMinStack()
		self.testSetofStacks()
		self.testMyQueue()
	# 3.1
	def testNStack(self):
		stck = NStack(3)

		stck.push(1,1)
		stck.push(2,1)

		stck.push(3,2)
		stck.push(4,2)

		stck.push(5,3)
		stck.push(6,3)

		assert(stck.pop(1) == 2)
		assert(stck.pop(2) == 4)
		assert(stck.pop(3) == 6)
		assert(stck.pop(1) == 1)
		assert(stck.pop(1) == None)
		assert(stck.pop(3) == 5)
		assert(stck.pop(2) == 3)
		assert(stck.pop(2) == None)
		assert(stck.pop(3) == None)

		print("Passed NStack Test")

	# 3.2
	def testMinStack(self):
		stck = Stack()
		vals = [8,10,6,7,4,3]
		mins = [None, 8,8,6,6,4,3]
		for i in range(len(vals)):
			assert(stck.min() == mins[i])
			stck.push(vals[i])
		for i in range(0,len(vals),-1):
			assert(stck.min() == mins[i])
			stck.pop()

		print("Passed O(1) Min, Push, Pop, Stack")

	# 3.3
	def testSetofStacks(self):
		stck = SetOfStacks(2)
		stck.push(1)
		stck.push(2)
		stck.push(3)
		stck.push(4)
		assert(stck.pop() == 4)
		assert(stck.pop() == 3)
		assert(stck.pop() == 2)
		assert(stck.pop() == 1)
		assert(stck.pop() == None)

		print("Passed Set of Stacks Test")
	# 3.5
	def testMyQueue(self):
		queue = MyQueue()
		queue.enqueue(1)
		assert(queue.dequeue() == 1)
		queue.enqueue(2)
		queue.enqueue(3)
		assert(queue.dequeue() == 2)
		assert(queue.dequeue() == 3)
		assert(queue.dequeue() == None)
		queue.enqueue(4)
		assert(queue.dequeue() == 4)
		assert(queue.dequeue() == None)

		print("Passed MyQueue Test")

t = Tests().execute()