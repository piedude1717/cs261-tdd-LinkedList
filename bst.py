# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# Abhimanyu. bais

import test_bst as bst


class BinarySearchTree:

    def __init__(self, key=None, left=None, right=None):
        self.data_tree = bst
        self.left = left
        self.right = right
        self.key = key
        self.parent = self.key

    def insert(self, child):

        if child.key <= self.key:
            if self.left is None:
                self.left = child
                child.parent = self

            else:
                self.left.insert(child)

        elif child.key > self.key:
            if self.right is None:
                self.right = child
                child.parent = self

            else:
                self.right.insert(child)

    def search(self, value):
        if self:
            if self.key == value:
                return self
            elif value < self.key:
                return None if self.left is None else self.left.search(value)
            elif value > self.key:
                return None if self.right is None else self.right.search(value)
            else:
                return self

    def delete(self, value):
        node = self.search(value)

        if node is None:
            # return self at bottom
            pass

        elif node == self:
            # if the value we want to delete is the root itself

            if self.left is None and self. right is None:
                # This is for a single level tree
                self = None

            elif self.right is not None:
                # This is for when the tree has a right child which will be the new root
                if self.left is not None:
                    self.right.left = self.left
                self = self.right

            elif self.left is not None and self.right is None:
                # This is for when the tree has a left child which will be the new root
                if self.right is not None:
                    self.left.right = self.right
                self = self.left

        elif node.key > node.parent.key:
            node.parent.right = None

        elif node.key <= node.parent.key:
            node.parent.left = None

        return self

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.left is not None

    def minimum(self):
        itr = self
        while itr.left:
            itr = itr.left
        return itr
