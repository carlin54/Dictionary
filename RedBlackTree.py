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
        self.nil = RedBlackNode(None, None, None, None, None)
        self.root = self.nil



    def add(self, value):
        if self.root is self.nil:                           # Setting Root
            self.root = RedBlackNode(value, Colour.BLACK, self.nil, self.nil, self.nil)
            return

        parent, add_direction = self._find_parent(value)

        add_node = RedBlackNode(value, Colour.RED, parent, self.nil, self.nil)

        if add_direction is Direction.RIGHT:
            parent.right = add_node
        else:
            parent.left = add_node

        self._rebalance(add_node)

    def _rebalance(self, node):
        print("balancing")
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

    def _find_parent(self, value):
        next = self.root
        parent = None
        last_direction = None

        while next is not self.nil:
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