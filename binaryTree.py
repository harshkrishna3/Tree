from tree import Tree
class BinaryTree(Tree):
    def left_child(self, pos):
        '''Return the left child of the position

        Return None if there is no left child of the position'''
        raise NotImplementedError('must be implemented by subclass')

    def right_child(self, pos):
        '''Return the right child of the position

        Return None if there is no right child of the position'''
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, pos):
        '''Return the siblings of the position

        Return None if the position does not have a sibling'''
        parent = self.parent(pos)
        left = self.left(parent)
        right = self.right(parent)
        if pos == left:
            return right
        else:
            return left
