from binaryTree import BinaryTree
class ListBinaryTree(BinaryTree):
    def __init__(self):
        self.elements = []
        self.parent = []
        self.left = []
        self.right = []

    def root(self):
        if len(self.elements) == 0:
            return None
        else:
            return 0

    def element(self, idx):
        return self.elements[idx]

    def parent_pos(self, idx):
        return self.parent[idx]

    def num_children(self, idx):
        num = 0
        if self.left(idx) is not None:
            num += 1
        if self.left(idx) is not None:
            num += 1
        return num

    def children(self, idx):
        l_child = self.left_child(idx)
        r_child = self.right_child(idx)
        if l_child:
            yield l_child
        if r_child:
            yield r_child

    def is_leaf(self, idx):
        return self.num_children(idx) == 0

    def __len__(self):
        return len(self.elements)

    def left_child(self, idx):
        return self.left[idx]

    def right_child(self, idx):
        return self.right[idx]

    def addNode(self, element, parent_idx, left_idx = None, right_idx = None, is_right_child = False):
        self.elements.append(element)
        self.parent.append(parent_idx)
        self.left.append(left_idx)
        self.right.append(right_idx)
        idx = len(self.elements) -1
        try:
            l_child = self.left_child(parent_idx)
            if not l_child:
                if not is_right_child:
                    self.change_left(parent_idx, idx)
                    return idx
            r_child = self.right_child(parent_idx)
            if not r_child:
                self.change_right(parent_idx, idx)
                return idx
            raise KeyError('Parent already has 2 children')
        except TypeError:
            pass

    def change_left(self, idx, left_idx):
        self.left[idx] = left_idx

    def change_right(self, idx, right_idx):
        self.right[idx] = right_idx

    def change_parent(self, idx, parent_idx):
        self.parent[idx] = parent_idx
