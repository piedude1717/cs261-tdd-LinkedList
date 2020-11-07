# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# YOUR NAME

import test_bst as bst


class BinarySearchTree:

    def __init__(self, key=None, left=None, right=None):
        self.data_tree = bst
        self.left = left
        self.right = right
        self.key = key
        self.parent = self.key

    def insert(self, value):
        if value.key <= self.key:
            if self.left is not None:
                self.left = value
                value.parent = self
            else:
                self.left
                BinarySearchTree.insert(self, value)
        elif value.key >= self.key:
            self.right = value
            value.parent = self
        e:
            self = self.right
            BinarySearchTree.insert(self, value)

        else:
            self.key = value.key
            self.parent = value.parent

    def search(self, value):
        if self:
            if value < self.parent:
                return BinarySearchTree.search(self.left, value)
            if value > self.parent:
                return BinarySearchTree.search(self.right, value)
            else:
                return self

    def delete(self, value):
        self.search(value)
        self = ('hi')





        # def search(root, val):
        #     '''
        #     The Function will Search the Element is the given Tree And return Boolean value.
        #     | root = root of given tree.
        #     | val  = Value is Searching Element.
        #     '''
        #     if root:
        #         # if the value is smaller than the root ,then it will again recursive in the Left child Node.
        #         if val < root.val:
        #             return search(root.left, val)
        #         # if the value is greater than the root ,then it will again recursive in the right child Node.
        #         elif val > root.val:
        #             return search(root.right, val)
        #         # if the Both condition get False then it got value.
        #         else:
        #             return True
        #     # If the all recursion complied and didn't get them if will return False.
        #     else:
        #         return False
