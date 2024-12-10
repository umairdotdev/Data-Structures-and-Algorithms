
import unittest
from src.bst import BST

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_add_and_contains(self):
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(15)
        self.assertTrue(self.bst.contains(10))
        self.assertTrue(self.bst.contains(5))
        self.assertTrue(self.bst.contains(15))
        self.assertFalse(self.bst.contains(20))

    def test_find_min_and_max(self):
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(15)
        self.assertEqual(self.bst.find_min(), 5)
        self.assertEqual(self.bst.find_max(), 15)

    def test_remove(self):
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(15)
        self.bst.remove(10)
        self.assertFalse(self.bst.contains(10))
        self.assertTrue(self.bst.contains(5))
        self.assertTrue(self.bst.contains(15))

    def test_is_empty_and_make_empty(self):
        self.assertTrue(self.bst.is_empty())
        self.bst.add(10)
        self.assertFalse(self.bst.is_empty())
        self.bst.make_empty()
        self.assertTrue(self.bst.is_empty())

if __name__ == '__main__':
    unittest.main()
