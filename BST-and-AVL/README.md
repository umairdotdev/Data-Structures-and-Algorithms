
# CS261 Data Structures Project

This project is an implementation of **Binary Search Tree (BST)** and **AVL Tree**.
Date: 27/2/2023

## Structure

```
CS261-Data-Structures-Project/
│
├── src/
│   ├── queue_and_stack.py  # Helper classes for queue and stack operations
│   ├── bst.py              # Binary Search Tree implementation
│   ├── avl.py              # AVL Tree implementation
│
├── tests/
│   ├── test_bst.py         # Tests for BST implementation
│   ├── test_avl.py         # Tests for AVL implementation
│
├── README.md               # Project overview and documentation
```

## Description

- **queue_and_stack.py**: Contains helper classes `Queue` and `Stack` for internal operations.
- **bst.py**: Implements the `BST` class with operations like add, remove, find, and traversal.
- **avl.py**: Extends `BST` to create an `AVL` class, ensuring the tree remains balanced after each operation.

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run tests:
    ```bash
    python -m unittest discover tests
    ```

## Contributing

Feel free to submit pull requests with improvements or additional test cases.
