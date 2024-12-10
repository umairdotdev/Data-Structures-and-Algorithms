
import unittest
from src.avl import AVL

class TestAVL(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()

    def test_add_and_balance(self):
        self.avl.add(10)
        self.avl.add(20)
        self.avl.add(30)  # Trigger a rotation
        self.assertTrue(self.avl.contains(10))
        self.assertTrue(self.avl.contains(20))
        self.assertTrue(self.avl.contains(30))

    def test_remove_and_balance(self):
        self.avl.add(10)
        self.avl.add(20)
        self.avl.add(5)
        self.avl.add(25)
        self.avl.add(15)
        self.avl.remove(20)  # Trigger rebalancing
        self.assertFalse(self.avl.contains(20))
        self.assertTrue(self.avl.contains(25))
        self.assertTrue(self.avl.contains(15))

    def test_find_min_and_max(self):
        self.avl.add(10)
        self.avl.add(5)
        self.avl.add(15)
        self.assertEqual(self.avl.find_min(), 5)
        self.assertEqual(self.avl.find_max(), 15)

    def test_is_empty_and_make_empty(self):
        self.assertTrue(self.avl.is_empty())
        self.avl.add(10)
        self.assertFalse(self.avl.is_empty())
        self.avl.make_empty()
        self.assertTrue(self.avl.is_empty())

if __name__ == '__main__':
    unittest.main()
