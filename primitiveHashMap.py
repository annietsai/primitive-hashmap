# hashMap.py
# Author: Annie Tsai
# ----------
# A fixed-size hash map using only primitive types that associate string
# keys with arbitrary data object references.


class PrimitiveHashMap(object):

	def __init__(self, size):
		"""
		Initialize an empty node for the trie stored in data to extend from.
		The number of elements in the HashMap cannot exceed the given size.
		"""
		self.size = size
		self.num_elem = 0
		self.data = Node('')

	def set(self, key, value):
		"""
		Set a key to map to a value in our HashMap. Returns True if successful;
		else, returns False.
		"""
		if self.num_elem >= self.size:
			return False

		hashCode = hash(key)
		strHashCode = str(hashCode)
		currNode = self.data
		duplicate = True

		for num in strHashCode:
			if num == '-':
				child = currNode.getChild(num)
				if child is None:
					currNode.changeChild(num, Node(num, currNode))
					currNode.updateChildren('add')
					duplicate = False
					child = currNode.getChild(num)
			else:
				child = currNode.getChild(int(num))
				if child is None:
					currNode.changeChild(int(num), Node(int(num), currNode))
					currNode.updateChildren('add')
					duplicate = False
					child = currNode.getChild(int(num))
			currNode = child

		if currNode.last != None:
			if duplicate:
				if currNode.last.getValue() == value:
					return False
				else:
					currNode.last = Node(value, currNode, None, True)
					return True

		currNode.last = Node(value, currNode, None, True)
		self.num_elem += 1

		return True

	def get(self, key):
		"""
		Retrieves the object value that is mapped to by the inputted key.
		Returns the value if successful; else, returns None.
		"""
		if self.num_elem == 0:
			return None

		hashCode = hash(key)
		strHashCode = str(hashCode)
		currNode = self.data

		for num in strHashCode:
			if num == '-':
				child = currNode.getChild(num)
			else:
				child = currNode.getChild(int(num))

			if child is None:
				return None
			currNode = child

		if currNode.last is None:
			return None

		return currNode.last.getValue()

	def delete(self, key):
		"""
		Deletes the key and its value from the HashMap if it exists. Returns
		the value if successful; else, returns None.
		"""
		if self.num_elem == 0:
			return None

		hashCode = hash(key)
		strHashCode = str(hashCode)
		currNode = self.data

		for num in strHashCode:
			if num == '-':
				child = currNode.getChild(num)
			else:
				child = currNode.getChild(int(num))

			if child is None:
				return None
			currNode = child

		if currNode is None or currNode.last is None:
			return None

		retValue = currNode.last.getValue()
		listHashCode = list(strHashCode)

		while currNode.getNumChildren() <= 1 and len(listHashCode) > 0:
			currNode = currNode.getParent()
			lastHashElem = listHashCode.pop()

			if lastHashElem == '-':
				child = currNode.getChild(lastHashElem)
			else:
				child = currNode.getChild(int(lastHashElem))
			child = None

		currNode.updateChildren('sub')
		self.num_elem -= 1

		return retValue

	def load(self):
		"""
		Returns the load factor, which should always be less than or equal
		to 1.
		"""
		return float(self.num_elem) / float(self.size)

class Node(object):

	def __init__(self, val, parent=None, last=None, isLeaf=False):
		self.val = val
		self.parent = parent
		self.posNeg = None
		self.child0 = None
		self.child1 = None
		self.child2 = None
		self.child3 = None
		self.child4 = None
		self.child5 = None
		self.child6 = None
		self.child7 = None
		self.child8 = None
		self.child9 = None
		self.last = last
		self.isLeaf = isLeaf
		self.num_children = 0

	def getParent(self):
		return self.parent

	def getChild(self, n):
		if n == '-':
			return self.posNeg
		if n == 0:
			return self.child0
		if n == 1:
			return self.child1
		if n == 2:
			return self.child2
		if n == 3:
			return self.child3
		if n == 4:
			return self.child4
		if n == 5:
			return self.child5
		if n == 6:
			return self.child6
		if n == 7:
			return self.child7
		if n == 8:
			return self.child8
		if n == 9:
			return self.child9

	def changeChild(self, n, value):
		if n == '-':
			self.posNeg = value
		elif n == 0:
			self.child0 = value
		elif n == 1:
			self.child1 = value
		elif n == 2:
			self.child2 = value
		elif n == 3:
			self.child3 = value
		elif n == 4:
			self.child4 = value
		elif n == 5:
			self.child5 = value
		elif n == 6:
			self.child6 = value
		elif n == 7:
			self.child7 = value
		elif n == 8:
			self.child8 = value
		elif n == 9:
			self.child9 = value

	def getValue(self):
		return self.val

	def updateChildren(self, op):
		if op == 'add':
			self.num_children += 1
		elif op == 'sub':
			self.num_children -= 1

	def getNumChildren(self):
		return self.num_children

