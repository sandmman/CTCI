class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Tree():

	def __init__(self):
		self.root = None
		self.pre  = []
		self.post = []
		self.inor = []

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

	def nextNode(self, node):
		
	def build(self, array):
		pass

	def insert(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			tmp = self.root
			while (tmp.right != None and value > tmp.value) or (tmp.left != None and value < tmp.value):
				if value > tmp.value:
					tmp = tmp.right
				else:
					tmp = tmp.left
			if value > tmp.value:
				tmp.right = Node(value)
			else:
				tmp.left = Node(value)

	def add(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			self._add(self.root, value)

	def _add(self, root, value):
		if value > root.value:
			if root.right == None:
				root.right = Node(value)
			else:
				self._add(root.right, value)
		else:
			if root.left == None:
				root.left = Node(value)
			else:
				self._add(root.left, value)

	def isBinarySearchTree(self):
		return self._isBinarySearchTree(self.root)

	def _isBinarySearchTree(self, root):
		if root == None:
			return True

		if root.left != None and root.value < root.left.value:
			return False
		if root.right != None and root.value > root.right.value:
			return False

		left = self._isBinarySearchTree(root.left)
		right = self._isBinarySearchTree(root.right)

		return left and right

	def isBalanced(self):
		if self._isBalanced(self.root) == -1:
			return False
		return True

	def _isBalanced(self, root, depth=0):
		if root == None:
			return depth

		left = self._isBalanced(root.left, depth + 1)
		right = self._isBalanced(root.right, depth + 1)

		if left == -1 or right == -1 or left - right > 1:
			return -1

		return max(left, right)

	def printTree(self):
		print(self._printTree(self.root))

	def _printTree(self, root):
		if root == None:
			return ""
		if root.left == None and root.right == None:
			return str(root.value)
		else:
			left = self._printTree(root.left)
			right = self._printTree(root.right)

			string = str(root.value)
			return "Node: "  + string + " Left: [" + left + "] Right: [" + right  + "]"

	def get_levels(self):
		self.arr = []
		self._get_levels(self.root)
		return self.arr

	def _get_levels(self, root, level=0):
		if root == None:
			return
		if len(self.arr) - 1 != level:
			self.arr.append([])

		self.arr[level].append(root.value)

		self._get_levels(root.left,level + 1)
		self._get_levels(root.right,level + 1)

class Tests:

	def __init__(self):
		self.tree = Tree()
		self.tree.add(5)
		self.tree.add(4)
		self.tree.add(6)
		self.tree.add(2)
		self.tree.add(1)

		self.lTree = Tree()
		self.lTree.add("F")
		self.lTree.add("B")
		self.lTree.add("G")
		self.lTree.add("A")
		self.lTree.add("D")
		self.lTree.add("C")
		self.lTree.add("E")
		self.lTree.add("I")
		self.lTree.add("H")

	def execute(self):
		self.testPrintTree()
		self.testIsBalanced()
		self.testGetLevels()
		self.testIsBinarySearchTree()
		self.testPreOrder()
		self.testPostOrder()
		self.testInOrder()
		self.testIsBalanced()

	def testPreOrder(self):
		self.lTree.preOrder(self.lTree.root)
		assert(self.lTree.pre == ["F","B","A","D","C","E","G","I","H"])
		print("Passed Pre Order")

	def testPostOrder(self):
		self.lTree.postOrder(self.lTree.root)
		assert(self.lTree.post == ["A","C","E","D","B","H","I","G","F"])
		print("Passed Post Order")

	def testInOrder(self):
		self.lTree.inOrder(self.lTree.root)
		assert(self.lTree.inor == ["A","B","C","D","E","F","G","H","I"])
		print("Passed In Order")

	def testPrintTree(self):
		self.tree.printTree()

		print("Passed print All Test")

	def testIsBalanced(self):
		tree = Tree()
		assert tree.isBalanced() == True, "None"
		tree.add(5)
		assert tree.isBalanced() == True, "5"
		tree.add(4)
		assert tree.isBalanced() == True, "4"
		tree.add(6)
		assert tree.isBalanced() == True, "3"
		tree.add(2)
		assert tree.isBalanced() == True, "2"
		tree.add(1)
		assert self.tree.isBalanced() == False, "1"

		print("Passed isBalanced Test")

	def testBuildTree(self):
		tree = Tree()
		tree.build([1,2,3,4,5,6])
		tree.printTree()

		print("Passed Build Tree Test")

	def testGetLevels(self):
		assert self.tree.get_levels() == [[5], [4, 6], [2], [1], []]

		print("Passed Get Levels Test")

	def testIsBinarySearchTree(self):
		assert self.tree.isBinarySearchTree() == True

		tree = Tree()
		tree.root = Node(2)
		tree.root.left = Node(1)
		tree.root.right = Node(18)
		tree.root.right.right = Node(120)
		assert tree.isBinarySearchTree() == True
		tree.root.left.left = Node(-1)
		tree.root.left.left.right = Node(-10)
		assert tree.isBinarySearchTree() == False

		print("Passed is bst Test")

	def testNextNode(self):
		x = ["F","B","A","D","C","E","G","I","H"])
		for i in range(len(x) - 1):
			assert self.lTree.nextNode(x[i]) == x[i + 1], x[i], x[i + 1]
t = Tests()
t.execute()
