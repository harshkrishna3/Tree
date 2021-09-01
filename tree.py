from queue import Queue
class Tree:
    '''Abstract base class representing a tree'''

    class Position:
        '''An abstraction representing location of single element'''

        def element(self):
            'Return the element stored at the position'
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, pos):
            'Return True if two postions represents same location'
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, pos):
            'Return True if two postions does not represents same location'
            return not (self == pos)

    def root(self):
        'Return root of the tree'
        raise NotImplementedError('must be implemented by subclass')

    def element(self, pos):
        'Return the element stored at position'
        raise NotImplementedError

    def parent_pos(self, pos):
        'Return parent of the tree'
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, pos):
        'Return number of children of the Position'
        raise NotImplementedError('must be implemented by subclass')

    def children(self, pos):
        'Return an iteration of children of the position'
        raise NotImplementedError('must be implemented by subclass')

    def change_parent(self, pos):
        'Changes the parent of the position'
        raise NotImplementedError('must be implemented by subclass')

    def is_leaf(self, pos):
        'Return True if the position is a leaf'
        return self.number_of_children(pos) == 0

    def __len__(self):
        'Return the number of elements in the tree'
        raise NotImplementedError('must be implemented by subclass')

    def bredth_first_transversal(self, pos = None):
        'Return a generator transversing the tree bredth first'
        leftovers = Queue()
        leftovers.put(pos)
        # print(list(leftovers))
        while not leftovers.empty():
            node = leftovers.get(block = False)
            # print(node)
            try:
                for child in self.children(node):
                    leftovers.put(child)
            except TypeError:
                node = self.root()
                for child in self.children(node):
                    leftovers.put(child)
            yield node
            # print('-'*15)

    def preorder_transversal(self, node = None):
        'Returns a generator transversing the tree in preorder'
        pass
