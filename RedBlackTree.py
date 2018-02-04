from enum import Enum

class Colour(Enum):
    RED = True
    BLACK = False

class Direction(Enum):
    RIGHT = True
    LEFT = False

class RedBlackNode:
    def __init__(self, value, colour=Colour.BLACK, parent=None, left=None, right=None):
        self.value = value
        self.colour = colour
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        same_colour = self.colour == other.colour
        same_value = self.value == other.value

        return same_colour and same_value





class RedBlackTree:

    def __init__(self):
        #Always black
        self.nil = RedBlackNode(None, None, None, None, None)
        self.root = self.nil

    def add(self, value):

        # Setting Root
        if self.root is None:
            self.root = RedBlackNode(value, Colour.BLACK, None, None, None)
            return

        # Find where to insert the new node
        parent, add_direction = self._find_parent(value)

        # Insert the new node
        add_node = RedBlackNode(value, Colour.RED, parent, None, None)

        if add_direction is Direction.RIGHT:
            parent.right = add_node
        else:
            parent.left = add_node

        # Clean-up
        self._rebalance(add_node)


    def find_node(self, value):
        if self.root is None:
            return None
        find = self.root
        parent = None
        while find is not self.nil:
            parent = find
            if value > find.value:
                find = find.right
            elif value < find.value:
                find = find.left
            else:
                return find

        return None

    def _rotate_left(self, z):
        self._update_parent(z.right, z, z.parent)
        left = z.right.left
        z.parent = z.right
        z.parent.left = z
        z.right = left

    def _rotate_right(self, z):
        self._update_parent(z.left, z, z.parent)
        right = z.left.right
        z.parent = z.left
        z.parent.right = z
        z.left = right


    def _rebalance(self, node):
        print("balancing")

        # 0. Z = root
        parent = node.parent
        if not parent:  # => is Root
            node.colour = Colour.BLACK
            return

        grandparent = parent.parent

        if grandparent == None:   # => Parent is Root
            return

        uncle = grandparent.right if parent.value < grandparent.value else grandparent.left

        # 1. Z.uncle = red
        if uncle.colour == Colour.RED:
            parent.colour = Colour.BLACK
            uncle.colour = Colour.BLACK
            grandparent = Colour.RED

        # LL (left, right)

        # RL (left, right)

        # LR (left, right)

        # RR (left, right)


        # 2. Z.uncle = black(triangle)
        if uncle.colour == Colour.BLACK:
            if node.value > parent.value:
                self._rotate_left(parent)
            else:
                self._rotate_right(parent)

        # 3. Z.uncle = black(line)
        if uncle.colour == Colour.BLACK


    def _update_parent(self, new_child, old_child, parent):
        new_child.parent = parent
        if parent:
            if old_child.value > parent.value:
                parent.right = new_child
            else:
                parent.left = new_child
        else:
            self.root = new_child

    def _rotate_right(self, child, parent, grandparent):
        great_grandparent = grandparent.parent
        self._update_parent(parent, grandparent, great_grandparent)
        right = parent.right
        parent.right = grandparent
        grandparent.parent = parent
        grandparent.left = right

    def _rotate_left(self, child, parent, grandparent):
        great_grandparent = grandparent.parent
        self._update_parent(parent, grandparent, great_grandparent)
        left = parent.left
        parent.left = grandparent
        grandparent.parent = parent
        grandparent.right = left

    def _find_parent(self, value):
        next = self.root
        parent = None
        last_direction = None

        while next:
            parent = next
            if value > next.value:      #
                next = next.right
                last_direction = Direction.RIGHT
            elif value < next.value:    #
                next = next.left
                last_direction = Direction.LEFT
            else:                       # Is in the tree
                return None

        return parent, last_direction



def main():
    print("testing tree")
    array = [1,2,3,4,5,6,7,9,10]
    rbtree = RedBlackTree()
    for i in range(0, len(array)):
        print("Adding: " + str(array[i]))
        rbtree.add(array[i])

main()