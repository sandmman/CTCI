class TreeNode:

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

# Binary Search Tree
class Tree:

	def __init__(self):
		self.head = None
		self.pre  = []
		self.post = []
		self.inor = []

	def __recursiveAdd(self,head,value):
		if value < head.value:
			if head.left == None:
				head.left = TreeNode(value)
				return
			self.__recursiveAdd(head.left,value)
		else:
			if head.right == None:
				head.right = TreeNode(value)
				return
			self.__recursiveAdd(head.right,value)

	def add(self,value):
		if self.head == None:
			self.head = TreeNode(value)

		else:
			self.__recursiveAdd(self.head,value)

	# Traversals
	def preOrder(self, head):
		if head == None:
			return 
		else:
			self.pre.append(head.value)
			self.preOrder(head.left)
			self.preOrder(head.right)

	def postOrder(self, head):
		if head.left != None:
			self.postOrder(head.left)
		if head.right != None:
			self.postOrder(head.right)
		self.post.append(head.value)

	def inOrder(self, head):
		if head.left != None:
			self.inOrder(head.left)
		self.inor.append(head.value)
		if head.right != None:
			self.inOrder(head.right)

	# 4.1
	def isBalanced(self):
		res = self._isBalanced(self.head,0)
		return res[0]


	def _isBalanced(self,head,level):
		if head == None:
			return (True, level)

		(balL, levelL) = self._isBalanced(head.left, level + 1)
		(balR, levelR) = self._isBalanced(head.right, level + 1)


		if balL or balR or levelL - levelR > 1:
			return (False, -1)
		return (True, level)

	def printAll(self):
		print("PreOrder")
		self.preOrder(self.head)
		print("PostOrder")
		self.postOrder(self.head)
		print("InOrder")
		self.inOrder(self.head)


class Tests():

	def __init__(self):
		self.tree = Tree()
		self.tree.add("F")
		self.tree.add("B")
		self.tree.add("G")
		self.tree.add("A")
		self.tree.add("D")
		self.tree.add("C")
		self.tree.add("E")
		self.tree.add("I")
		self.tree.add("H")

	def execute(self):
		self.testPreOrder()
		self.testPostOrder()
		self.testInOrder()
		self.testIsBalanced()

	def testPreOrder(self):
		self.tree.preOrder(self.tree.head)
		assert(self.tree.pre == ["F","B","A","D","C","E","G","I","H"])
		print("Passed Pre Order")

	def testPostOrder(self):
		self.tree.postOrder(self.tree.head)
		assert(self.tree.post == ["A","C","E","D","B","H","I","G","F"])
		print("Passed Post Order")

	def testInOrder(self):
		self.tree.inOrder(self.tree.head)
		assert(self.tree.inor == ["A","B","C","D","E","F","G","H","I"])
		print("Passed In Order")

	def testIsBalanced(self):
		assert(self.tree.isBalanced() == True)

		print("Passed is Balanced")

t = Tests()
t.execute()