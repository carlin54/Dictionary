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
        self.root = None

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
        self.root.colour = Colour.BLACK


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
        print("rotate_left(" + str(z.value) + ")")
        left = z.right.left
        z.parent = z.right
        z.parent.left = z
        z.right = left

    def _rotate_right(self, z):
        self._update_parent(z.left, z, z.parent)
        print("rotate_right(" + str(z.value) + ")")
        right = z.left.right
        z.parent = z.left
        z.parent.right = z
        z.left = right


    def _rebalance(self, node):
        print("balancing (" + str(node.value) + ")")

        parent = node.parent

        # 0. Z = root
        if not parent:  # => is Root
            node.colour = Colour.BLACK
            print("case: 0")
            return

        grandparent = parent.parent

        if grandparent is None:   # => Parent is Root
            self._rebalance(node.parent)
            return


        uncle = None if grandparent is None else \
            (grandparent.right if parent.value < grandparent.value \
             else grandparent.left)

        # 1. Z.uncle = red
        if uncle is not None and uncle.colour == Colour.RED:
            print("case: 1")
            parent.colour = Colour.BLACK
            uncle.colour = Colour.BLACK
            grandparent.colour = Colour.RED
            self._rebalance(grandparent) # this can be optimized into a while loop


        # 2. Z.uncle = black(triangle)
        #
        #       [B]                 [B]
        #      /  \                /  \
        #   [B]   [R] <-Rotate-> [R]  [B]
        #        /                 \
        #      [R]                 [R]

        # 3. Z.uncle = black(line)
        #
        #       [B]    <-Rotate->   [B]
        #      /  \                /  \
        #   [B]   [R]            [B]  [R]
        #  /  \                      /  \
        #[R]  [B]                 [B]   [R]

        elif uncle is None or uncle.colour == Colour.BLACK:
            if node.value > parent.value:               # R
                if parent.value > grandparent.value:    # RR (case 3)
                    print("case: 3 RR")
                    grandparent.colour = Colour.RED
                    parent.colour = Colour.BLACK
                    self._rotate_left(grandparent)
                else:                                   # RL (case 2)
                    print("case: 2 LL")
                    self._rotate_left(node)
            else:                                       # L
                if parent.value > grandparent.value:    # LR (case 2)
                    print("case: 2 LR")
                    self._rotate_right(node)
                else:                                   # LL (case 3)
                    print("case: 3 LL")
                    grandparent.colour = Colour.RED
                    parent.colour = Colour.BLACK
                    self._rotate_right(grandparent)

    def _update_parent(self, new_child, old_child, parent):
        new_child.parent = parent
        if parent:
            if old_child.value > parent.value:
                parent.right = new_child
            else:
                parent.left = new_child
        else:
            self.root = new_child

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




main()
