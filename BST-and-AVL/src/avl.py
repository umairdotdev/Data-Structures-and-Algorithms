
from bst import BSTNode, BST

class AVLNode(BSTNode):
    """AVL Tree Node class."""
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.parent = None
        self.height = 0

class AVL(BST):
    """AVL Tree class."""
    def __init__(self, start_tree=None) -> None:
        super().__init__(start_tree)

    def add(self, value: object) -> None:
        """Insert a value into the AVL tree."""
        node = AVLNode(value)
        if not self._root:
            self._root = node
            return

        current = self._root
        while current:
            if value < current.value:
                if not current.left:
                    current.left = node
                    node.parent = current
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    node.parent = current
                    break
                current = current.right

        self._rebalance(node)

    def remove(self, value: object) -> bool:
        """Remove a value from the AVL tree."""
        node = self._find_node(value)
        if not node:
            return False

        if node.left and node.right:
            successor = self._find_min_node(node.right)
            node.value = successor.value
            node = successor

        self._remove_single_child(node)
        return True

    def _remove_single_child(self, node):
        """Remove a node with at most one child."""
        child = node.left if node.left else node.right
        if node.parent:
            if node.parent.left == node:
                node.parent.left = child
            else:
                node.parent.right = child
        else:
            self._root = child

        if child:
            child.parent = node.parent

        self._rebalance(node.parent)

    def _rebalance(self, node):
        """Rebalance the AVL tree starting from the given node."""
        while node:
            self._update_height(node)
            balance = self._balance_factor(node)
            if balance > 1:
                if self._balance_factor(node.right) < 0:
                    node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
            elif balance < -1:
                if self._balance_factor(node.left) > 0:
                    node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
            else:
                node = node.parent

    def _rotate_left(self, node):
        """Perform a left rotation."""
        new_root = node.right
        node.right = new_root.left
        if new_root.left:
            new_root.left.parent = node
        new_root.parent = node.parent
        if not node.parent:
            self._root = new_root
        elif node.parent.left == node:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_right(self, node):
        """Perform a right rotation."""
        new_root = node.left
        node.left = new_root.right
        if new_root.right:
            new_root.right.parent = node
        new_root.parent = node.parent
        if not node.parent:
            self._root = new_root
        elif node.parent.left == node:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.right = node
        node.parent = new_root
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _balance_factor(self, node):
        """Calculate the balance factor of a node."""
        return self._get_height(node.right) - self._get_height(node.left)

    def _get_height(self, node):
        """Get the height of a node."""
        return node.height if node else -1

    def _update_height(self, node):
        """Update the height of a node."""
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _find_node(self, value):
        """Find a node by its value."""
        current = self._root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def _find_min_node(self, node):
        """Helper function to find the node with the minimum value."""
        current = node
        while current and current.left:
            current = current.left
        return current
