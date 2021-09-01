from binaryTree import BinaryTree
class LinkedBinaryTree(BinaryTree):
    #this file is incomplete
    class _Node:
        __slots__ = 'parent', 'left', 'right', 'element', 'depth'
        def __init__(self, element, parent = None, left = None, right = None):
            self.element = element
            self.left = left
            self.right = right
            self.parent = parent
            try:
                self.depth = parent.depth + 1
            except AttributeError:
                self.depth = 0

    class Position(BinaryTree.Position):
        def __init__(self, node):
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, pos):
            return (type(self) == type(pos)) and (self.node is pos.node)

    def _make_position(self, node):
        return self.Position(node)

    def __init__(self):
        self._size = 0

    def parent(self, pos):
        return pos.node.parent

    def num_children(self, pos):
        num = 0
        if self.left(pos):
            num += 1
        if self.right(pos):
            num += 1
        return num

    def children(self, pos):
        yield self.left()
        yield self.right()

    def left(self, pos):
        return pos.node.left

    def right(self, pos):
        return pos.node.right

    def depth(self, pos):
        return pos.node.depth

    def __len__(self):
        return self._size

    def addNode(self, element, parent = None, left = None, right = None):
        return self._make_position(self._Node(element, parent, left, right))

    def change_parent(self, pos, new_parent):
        pos.node.parent = self._make_position(new_parent)

    def change_left(self, pos, new_left):
        pos.node.left = self.make_position(new_left)
