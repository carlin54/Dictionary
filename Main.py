import requests
import re
import time

from enum import Enum

class Colour(Enum):
    RED = True
    BLACK = False

class RedBlackNode:
    def __init__(self, key):
        self.key = key
        self.colour = Colour.BLACK
        self.left = []
        self.right = []
        self.p = []

    def __ne__(self, other):
        return self.key != other.key

class RedBlackTree:
    # Refer to Introduction to Algorithms, P 273,
    # Thomas H. Cormen, Charles E. Leiserson
    # Ronald L. Rivest, Clifford Stein

    # Also
    # Red Black Tree (Python Recipe)
    # http://code.activestate.com/recipes/576817-red-black-tree/
    # John Reid

    """
    Red-black tree properties
        1. Every node is either red or black.
        2. The root is black.
        3. Every leaf (NIL) is black.
        4. If a node is red, then both its children are black.
        5. For each node, all paths from the node descendant leaves
           contain the same number of black nodes.

    """
    def __init__(self):
        """constructor."""
        self.nil = RedBlackNode(key=[])
        self.root = self.nil

    def search(self, key, x=None):
        """Iterative implementation to find the closest node match in the tree."""
        if(x == None):
            x = self.root

        while(x != self.nil and x.key != key):
            if(key > x.key):
                x = x.right
            else:
                x = x.left

        return x

    def minimum(self, x=[]):
        """Iterative implementation to find the minimum value in the tree."""
        print('minimum')
        if(x == self.nil):
            x = self.root

        while(x.left != self.nil):
            x = x.left

        return x

    def maximum(self, x=[]):
        """Iterative implementation to find the maximum value in the tree."""
        print('maximum')

        if (x == self.nil):
            x = self.root

        while (x.left != self.nil):
            x = x.right

        return x

    def successor(self, x):
        """This function returns the next greatest number in the tree."""
        if(x.right != self.nil):
            return self.minimum(x.right)

        y = x.parent

        while(y != self.nil and x == y.right):
            x = y
            y = y.parent

        return y

    def insert_key(self, key):
        """Inserts a node with only a key."""
        print('insert key')
        rbnode = RedBlackNode(key)
        self.insert_node(rbnode)

    def insert_node(self, z):
        """Inserts a node into the tree."""
        print('insert node')
        y = self.nil
        x = self.root
        while(x != self.nil):
            y = x
            if(z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.parent = y

        if(y == self.nil):  # The tree was empty
            self.root = z
            return
        elif(z.key < y.key):
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.colour = Colour.RED
        self.insert_fixup(z)

    def insert_fixup(self, z):
        print('insert_fixup')
        """
        After insertion potential violation of properties are property 2 and 4.
            2. The root is black.
            4. If a node is red, then both its children are black.
        This is due to z being coloured red
            where z is the newly inserted node
        
        Figure 13.4
        (b) Case 1: z's uncle y is red, z's parent p is black, z is red
            -> Set my parent to black
            -> Set my uncle to black
            -> Set my grandparent to red
            (.) Repair the structure, and set up for the next iteration
        (c) Case 2: z's uncle y is black and z is the right child
            -> If z is the right child
                -> set z to p
                -> rotate left on z
            (.) Make it turn it into case 3
                   
        (d) Case 3: z's uncle y is black and z is the left child
            -> Set z's parent to black
            -> Set z's uncle to red
            -> rotate right on z's uncle
            (.) Makes z's parent blackm so that if z's parent is the root at 
            the start of the next iteration it is black
            
        """
        while(z.p.colour == Colour.RED):                # Terminate when z's parent is black
            if(z.p == z.p.p.left):                          # If my parent is on the left side of my grandparent
                y = z.p.p.right                                 # Set y to be z's uncle
                if(y.colour == Colour.RED):                     # If my uncle is red
                    z.p.colour = Colour.BLACK                       # Set z's parent colour to black.       # Case 1
                    y.colour = Colour.BLACK                         # Set z's uncle colour to black.        # Case 1
                    z.p.p.colour = Colour.RED                       # Set z's grand parent colour to red.   # Case 1
                    z = z.p.p                                       # Set z to z's grandparent.             # Case 1
                                                                    # This is done for to fix it for the next iteration.
                else:
                    if(z == z.p.right):                     # If z is on the right side of my parent.
                        z = z.p                                 # Set z to be z's parent.                  # Case 2
                        self.left_rotate(z)                     # Rotate left on z.                        # Case 2
                    z.p.colour = Colour.BLACK               # Set z's parent to black.                     # Case 3
                    z.p.p.colour = Colour.RED               # Set z's grandparent to colour to red.        # Case 3
                    self.rotate_right(z.p.p)                # Rotate right on z's grandparent.             # Case 3

            else:                                       # If my parent is on the right side of my grandparent.
                y = z.p.p.left                              # Set y to be z's uncle.
                if(y.colour == Colour.RED):                 # If my uncle is red.
                    z.p.colour = Colour.BLACK                   # Set z's parent colour to black.          # Case 1
                    y.colour = Colour.BLACK                     # Set z's uncle colour to black.           # Case 1
                    z.p.p.colour = Colour.RED                   # Set z's grandparent colour to red.       # Case 1
                    z = z.p.p                                   # Set z to z's grandparent.                # Case 1
                                                                # This is done for to fix it for the next iteration.
                else:
                    if(z == z.p.left):                      # If z is on the left side of my parent
                        z = z.p                                 # Set y to be z's uncle.                   # Case 2
                        self.right_rotate(z)                    # Rotate right on z.                       # Case 2
                    z.p.colour = Colour.BLACK               # Set z's parent to black.                     # Case 3
                    z.p.p.colour = Colour.RED               # Set z's grandparent to colour to red.        # Case 3
                    self.left_rotate(z.p.p)                 # Rotate left on z's grandparent.              # Case 3

        self.root.colour = Colour.BLACK

    def delete_key(self, z):
        print('delete key')

    def delete_node(self, z):
        print('delete node')

    def delete_fixup(self, x):
        print("delete fix up")

    def left_rotate(self, x):
        print('left_rotate')
        """Left rotation on the tree."""
        y = x.right                     # Set Y
        x.right = y.left                # Turn y's left subtree into x's right subtree.

        if(y.left != self.nil):         # If y has a left child.
            y.left.p = x                # Set y's left child to be the child of x.
        y.p = x.p                       # Link x's parent to y.

        if(x.p == self.nil):            # If x is root, y is now root.
            self.root = y
        elif(x == x.p.left):            # Finding the right side for y in x's parent.
            x.p.left = y
        else:
            x.p.right = y
        y.left = x                      # Put x on y's left.
        x.p = y

    def right_rotate(self, y):
        print('right_rotate')
        """Right rotation on the tree"""
        x = y.left                      # Set y.
        x.right = y.left                # Turn x's right subtree into y's left subtree.

        if(x.right != self.nil):        # If x has a right child.
            x.right.p = y               # Set x's right child to be a child of y.

        y.p = x.p                       # Link y's parent to x.

        if(y.p == self.nil):            # If y was the root, x is now the root.
            self.root = x
        elif(y == y.p.left):            # Finding the right side for x in y's parent.
            y.p.left = x
        else:
            y.p.right = x

        x.right = y                     # Put y on x's right.
        y.p = x

    def check_invariants(self):
        print('check_invariants')

def isInList(str, list):
    for i in range(len(list)):
        if str == list[i]:
            return True
    return False

def capture(text, find, clip, n=0):
    """
    Capture:
        text : String
        find : StringREGEX   - what to find in the text
        clip : StringREGEX   - what to remove from the found text
        n    : Int           - return setting
                                0 is all results,
                                1 is the first and only result not in a list,
                                1+ is the
    """
    input = []
    if(isinstance(text, str)):
        input = [text]
    else:
        input = text

    for i in range(0, len(find)):
        output = []
        for j in range(0, len(input)):
            output.extend(re.findall(find[i], input[j], re.DOTALL))
        input = output
        if len(input) == 0:
            break;

    if len(input) == 0:
        return []

    for i in range(0, len(clip)):
        for j in range(0, len(input)):
           input[j] = re.sub(clip[i], '', input[j])

    if n == 0:
        return input
    elif n == 1:
        return input[0]
    else:
        return input[0:max(n,len(input))]

def fetch_word_links_from_page(html):
    regex_word_definition = "[A-Za-z0-9\(\) &-/ʽ;]*"
    find = "<a href=\"/dictionary/" + regex_word_definition + "\">" + regex_word_definition + "</a>"
    clip = ["<a href=\"/dictionary/", "</a>"]
    captures = capture(html, find, clip)
    print(captures)

def main():
    print("hello, world!")
    seed = "word"
    alpherbet = ["abcdefghijklmnopqrstuvwxyz0"]
    pool = [seed]
    word = "<a href=\"/dictionary/[A-Za-z0-9\(\) &-/ʽ;]*\">[A-Za-z0-9\(\) &-/ʽ;]*</a>"

    for i in range(0, len(alpherbet)):
        link = "https://www.merriam-webster.com/browse/dictionary/" + 'a'
        ##Fetch Pages
        ##page 1 of 74
        ##<span class="counters">page 1 of 74</span>
        for i in range(1, 10):
            req = link + "/" + str(i)

            print(req)
            r = requests.get(req)
            html = r.text
            regex_word_definition = "[A-Za-z0-9\(\) &-/ʽ;]*"

            find = ["<a href=\"/dictionary/[A-Za-z0-9\(\) &-/ʽ;]*\">[A-Za-z0-9\(\) &-/ʽ;]*</a>"]
            clip = ["<a href=\"/dictionary/", "</a>"]
            captures = capture(html, find, [])
            print(captures)




##word = input("Word -> ");
##https://pythex.org/

main()
