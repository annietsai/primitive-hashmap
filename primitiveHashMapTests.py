import unittest
from primitiveHashMap import PrimitiveHashMap

class PrimitiveHashMapTests(unittest.TestCase):

	def testSet(self):
		x = PrimitiveHashMap(4)
		self.assertEqual(x.size, 4)
		self.assertEqual(x.data.num_children, 0)
		self.assertEqual(x.num_elem, 0)

		bool1 = x.set('numbers', 1234567890)
		self.assertEqual(bool1, True)
		self.assertEqual(x.data.num_children, 1)
		self.assertEqual(x.num_elem, 1)

		boolErr = x.set(2, 'this is not a string key')
		self.assertEqual(boolErr, False)
		self.assertEqual(x.num_elem, 1)

		bool2 = x.set('letters', 'abcdefg')
		self.assertEqual(bool2, True)
		self.assertEqual(x.num_elem, 2)

		bool3 = x.set('numbers', 1234567890)
		self.assertEqual(bool3, False)
		self.assertEqual(x.num_elem, 2)

		bool4 = x.set('tuple', (2, 3))
		self.assertEqual(bool4, True)
		self.assertEqual(x.num_elem, 3)

		bool5 = x.set('dict', {'hi': 2})
		self.assertEqual(bool5, True)
		self.assertEqual(x.num_elem, 4)

		bool6 = x.set('list', [0])
		self.assertEqual(bool6, False)
		self.assertEqual(x.num_elem, 4)

	def testGet(self):
		x = PrimitiveHashMap(3)

		x.set('string', 'thisisastring')
		string = x.get('string')
		self.assertEqual(string, 'thisisastring')
		self.assertEqual(x.num_elem, 1)

		x.set('boolean', True)
		boolean = x.get('boolean')
		self.assertEqual(boolean, True)
		self.assertEqual(x.num_elem, 2)

		error1 = x.get('error')
		self.assertEqual(error1, None)

		error2 = x.get({0: 4})
		self.assertEqual(error2, None)

		x.set('boolean', False)
		new_bool = x.get('boolean')
		self.assertEqual(new_bool, False)
		self.assertEqual(x.num_elem, 2)

		x.set('dictionary', {'hello': 'goodbye', 'cya': 'later'})
		dictionary = x.get('dictionary')
		self.assertEqual(dictionary, {'hello': 'goodbye', 'cya': 'later'})
		self.assertEqual(x.num_elem, 3)

		x.set('sentence', 'this is a sentence')
		sentence = x.get('sentence')
		self.assertEqual(sentence, None)
		self.assertEqual(x.num_elem, 3)

	def testDelete(self):
		x = PrimitiveHashMap(4)

		x.set('this is a sentence', 'hello how are you?')
		self.assertEqual(x.get('this is a sentence'), 'hello how are you?')

		x.set('delete this one', ['delete', 'me'])
		self.assertEqual(x.get('delete this one'), ['delete', 'me'])
		self.assertEqual(x.num_elem, 2)

		deleted = x.delete('delete this one')
		self.assertEqual(deleted, ['delete', 'me'])
		self.assertEqual(x.num_elem, 1)

		error1 = x.delete('nonexistent')
		self.assertEqual(error1, None)
		self.assertEqual(x.num_elem, 1)

		error2 = x.delete(['this', 'is', 'incorrect'])
		self.assertEqual(error2, None)
		self.assertEqual(x.num_elem, 1)

		x.set('listen', {'walk': 1, 'the': 2, 'moon': 3})
		x.set('play', {'shut': 0, 'up': 1, 'and': 2, 'dance': 3})
		x.set('repeat', {'with': 4, 'me': 5})
		self.assertEqual(x.num_elem, 4)

		sad = x.set('sad', [1, 2, 3])
		self.assertEqual(sad, False)
		self.assertEqual(x.get('sad'), None)
		self.assertEqual(x.num_elem, 4)

		listen = x.delete('listen')
		self.assertEqual(listen, {'walk': 1, 'the': 2, 'moon': 3})
		self.assertEqual(x.num_elem, 3)

		play = x.delete('play')
		self.assertEqual(play, {'shut': 0, 'up': 1, 'and': 2, 'dance': 3})
		self.assertEqual(x.num_elem, 2)

		repeat = x.delete('repeat')
		self.assertEqual(repeat, {'with': 4, 'me': 5})
		self.assertEqual(x.num_elem, 1)

		sentence = x.delete('this is a sentence')
		self.assertEqual(sentence, 'hello how are you?')
		self.assertEqual(x.num_elem, 0)

	def testLoad(self):
		x = PrimitiveHashMap(5)

		x.set('test1', ['t', 'e', 's', 't', '1'])
		self.assertEqual(x.load(), 1.0 / 5.0)

		x.set('test2', 'testing #2')
		self.assertEqual(x.load(), 2.0 / 5.0)

		x.set('test3', 10293)
		self.assertEqual(x.load(), 3.0 / 5.0)

		x.set('test4', (1, 2))
		self.assertEqual(x.load(), 4.0 / 5.0)

		x.set('test5', {'test': 5})
		self.assertEqual(x.load(), 5.0 / 5.0)

		boolErr = x.set('test6', 'ERROR')
		self.assertEqual(boolErr, False)
		self.assertEqual(x.num_elem, 5)
		self.assertEqual(x.load(), 5.0 / 5.0)

		x.delete('test5')
		self.assertEqual(x.load(), 4.0 / 5.0)

		x.delete('test4')
		self.assertEqual(x.load(), 3.0 / 5.0)

		x.delete('test3')
		self.assertEqual(x.load(), 2.0 / 5.0)

		x.delete('test2')
		self.assertEqual(x.load(), 1.0 / 5.0)

		x.delete('test1')
		self.assertEqual(x.load(), 0.0 / 5.0)

if __name__ == '__main__':
	unittest.main(exit=False)
