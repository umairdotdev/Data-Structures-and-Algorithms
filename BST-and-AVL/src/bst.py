
from queue_and_stack import Queue, Stack

class BSTNode:
    """Binary Search Tree Node class"""
    def __init__(self, value: object) -> None:
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree class"""
    def __init__(self, start_tree=None) -> None:
        self._root = None
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def add(self, value: object) -> None:
        """Add a new value to the BST."""
        node = BSTNode(value)
        if self._root is None:
            self._root = node
            return

        parent = None
        current = self._root
        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if value < parent.value:
            parent.left = node
        else:
            parent.right = node

    def remove(self, value: object) -> bool:
        """Remove a value from the BST."""
        def remove_node(node, value):
            if not node:
                return None, False

            if value < node.value:
                node.left, removed = remove_node(node.left, value)
            elif value > node.value:
                node.right, removed = remove_node(node.right, value)
            else:
                if not node.left:
                    return node.right, True
                elif not node.right:
                    return node.left, True

                # Node with two children: Get the inorder successor (smallest in the right subtree)
                min_larger_node = self._find_min_node(node.right)
                node.value = min_larger_node.value
                node.right, _ = remove_node(node.right, min_larger_node.value)
                return node, True

            return node, removed

        self._root, removed = remove_node(self._root, value)
        return removed

    def contains(self, value: object) -> bool:
        """Check if the tree contains a value."""
        current = self._root
        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self) -> Queue:
        """Perform an inorder traversal and return a queue of values."""
        result = Queue()

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.enqueue(node.value)
            inorder(node.right)

        inorder(self._root)
        return result

    def find_min(self) -> object:
        """Find the minimum value in the BST."""
        min_node = self._find_min_node(self._root)
        return min_node.value if min_node else None

    def find_max(self) -> object:
        """Find the maximum value in the BST."""
        max_node = self._find_max_node(self._root)
        return max_node.value if max_node else None

    def is_empty(self) -> bool:
        """Check if the BST is empty."""
        return self._root is None

    def make_empty(self) -> None:
        """Remove all nodes from the BST."""
        self._root = None

    def _find_min_node(self, node):
        """Helper function to find the node with the minimum value."""
        current = node
        while current and current.left:
            current = current.left
        return current

    def _find_max_node(self, node):
        """Helper function to find the node with the maximum value."""
        current = node
        while current and current.right:
            current = current.right
        return current
