import requests
import re
from enum import Enum
class Colour(Enum):
    RED = True
    BLACK = False

class RedBlackNode:
    def __init__(self, key):
        self.key = key
        self.colour = Colour.RED
        self.left = []
        self.right = []
        self.p = []


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

    def search(self, key, x=[]):
        """Iterative implementation to find a specific node in a tree."""
        print('search')

        if(x == self.nil):
            x = self.root

        while(x == self.nil or x.key != key):
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
        if(z.p != []):
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

def main():
    dictionary = RedBlackTree()
    seed = "board"
    pool = [seed]
    #while(len(pool) > 0):
    str = pool[0]
    word = fetch_word(str)
    print(word)
        #dictionary.insert_key(word)
        #for i in range(0, len(word.synonyms)):
        #    add_word = word.synonyms[i].word
         #   print(word.synonyms)
        #    search_node = dictionary.search(add_word)
        #    if(search_node.key != add_word):    ## => add_word was not found
         #       pool.extend(add_word)






##word = input("Word -> ");
##https://pythex.org/

class PartOfSpeech(Enum):
    NOUN = 0
    VERB_USED_WITHOUT_OBJECT = 1
    VERB_USED_WITH_OBJECT = 2
    ADJECTIVE = 3
    ADVERB = 4
    PRONOUN = 5
    PREPOSITIONAL = 6
    CONJUNCTION = 7
    DETERMINER = 8
    EXCLAMATION = 9

def pos_to_string(pos):
    return {
        PartOfSpeech.NOUN                       : "Noun",
        PartOfSpeech.VERB_USED_WITHOUT_OBJECT   : "Verb (used without object)",
        PartOfSpeech.VERB_USED_WITH_OBJECT      : "Verb (used with object)",
        PartOfSpeech.ADJECTIVE                  : "Adjective",
        PartOfSpeech.ADVERB                     : "Adverb",
        PartOfSpeech.PRONOUN                    : "Pronoun",
        PartOfSpeech.PREPOSITIONAL              : "Prepositional",
        PartOfSpeech.CONJUNCTION                : "Conjunction",
        PartOfSpeech.DETERMINER                 : "Determiner",
        PartOfSpeech.EXCLAMATION                : "Exclamation"
    }[pos]

class Description:
    context = []
    example = []

    def __init__(self, context, example):
        self.context = context
        self.example = example

class Definition:
    number = 1                        # :: Integer || Char
    mainDescription = []            # :: Description
    additionalDescriptions = []     # :: [Description]

    def __str__(self):
        string = ""
        string += str(self.number) + ". "

        if(self.mainDescription != []):
            if(self.mainDescription.context != []):
                string += self.mainDescription.context + "\n"
            if(self.mainDescription.example != []):
                string += "\"" + self.mainDescription.example + "\"\n"

        if(self.additionalDescriptions != []):
            for i in range(0, len(self.additionalDescriptions)):
                description = self.additionalDescriptions[i]
                if(description.context != []):
                    letter = chr(97 + i)
                    string += "\t" + letter + ". " + description.context + "\n"

                if(description.example != []):
                    string += "\t\t\"" + description.example + "\"\n"
        return string

    def __init__(self, number=0, main_description=[], additional_descriptions=[]):
        self.number = number
        self.mainDescription = main_description
        self.additionalDescriptions = additional_descriptions

    def setMainDescription(self, mainDescription):
        self.mainDescription = mainDescription

    def setAdditionalDescription(self, additionalDescriptions):
        self.additionalDescriptions = additionalDescriptions

class Section:
    partOfSpeech = []           # :: Part of Speech
    definitions = []            # :: [Definition]

    def __init__(self, pos, definitions):
        self.partOfSpeech = pos
        self.definitions = definitions

    def __str__(self):
        out = '[' + pos_to_string(self.partOfSpeech) + ']' + '\n'
        for i in range(0, len(self.definitions)):
            definition = self.definitions[i]
            print(str(definition))
            out += str(definition)
        return out

    def setPartOfSpeech(self, pos):
        self.partOfSpeech = pos

    def setDefinitions(self, definitions):
        self.definitions = definitions

class Word:
    word = ''                   # :: String
    sectionDefinition = []      # :: [Section]
    relatedForms = []           # :: [String]
    synonyms = []               # :: Synonyms

    def __repr__(self):
        out = "[Word]\n" + self.word + "\n"

        out += "[Definition]\n"
        for i in range(0, len(self.sectionDefinition)):
            out += str(self.sectionDefinition[i])

        out += "[Related Forms]\n"
        row_width = 3
        counter = 0
        for i in range(0, len(self.relatedForms)):
            out += str(self.relatedForms[i]) + ",\t"
            counter += 1
            if(counter >= row_width):
                out += '\n'
                counter = 0

        out += "\n"
        out += "[Synonyms]\n"
        row_width = 3
        counter = 0
        for i in range(0, len(self.synonyms)):
            out += str(self.synonyms[i]) + ",\t"
            counter += 1
            if(counter >= row_width):
                out += '\n'
                counter = 0
        return out

    def __init__(self, word, sectionDefinition, relatedForms, synonyms):
        self.word = word
        self.relatedForms = relatedForms
        self.synonyms = synonyms
        self.sectionDefinition = sectionDefinition

    def __eq__(self, other):
        return self.word == other.word

    def __gt__(self, other):
        s_len = len(self.word)
        o_len = len(other.word)
        min_len = min(s_len, o_len)
        for i in range(0, min_len):
            cs = ord(self.word[i])
            co = ord(other.word[i])
            if(cs > co):
                return True
            elif(cs < co):
                return False

        return s_len > o_len

    def __lt__(self, other):
        s_len = len(self.word)
        o_len = len(other.word)
        min_len = min(s_len, o_len)
        for i in range(0, min_len):
            cs = ord(self.word[i])
            co = ord(other.word[i])
            if (cs < co):
                return True
            elif (cs > co):
                return False

        return s_len < o_len

    def addSection(self, partofspeech, section):
        if(section != []):
            section = Section(partofspeech, section)
            self.sectionDefinition.append(section)

class Meaning:
    number = 0
    definition = []
    example = []

    def _init__(self, definition, example):
        self.definition = definition
        self.example = example

def min(a, b):
    if(a < b):
        return a
    else :
        return b

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

def cut(regex, text):
    return []

def find_definition(regex_section):
    regex_find_each_definition = r"<div class=\"def-set\">.+?</div>.[\n ]*</div>"
    find = [regex_section,
            regex_find_each_definition]
    return find

def clip_definition():
    regex_clip_new_line = r"\n"
    regex_clip_carriage_return = r"\r"
    regex_clip_l1 = r"<div.*number\">"
    regex_clip_l2 = r"[ ]*</span>.+?<div class=\"def-content\">[ ]*"
    regex_clip_l3 = r"[ ]*</div>"
    regex_clip_href_a = r"<a class=\"dbox-xref dbox-roman\" href=\"http://www.dictionary.com/browse/[a-zA-Z-]*\">"
    regex_clip_a = r"</a>"
    regex_clip_example_href = r"[ ]*<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">"
    regex_clip_example_href_span = r"</span>"
    regex_clip_italic = r"<span class=\"dbox-italic\">"
    regex_clip_example = r"<span class=\"dbox-example\">"
    regex_clip_bold = r"<span class=\"dbox-bold\">"
    regex_clip_bold_xref = r"<a class=\"dbox-xref dbox-bold\" href=\"http://www.dictionary.com/browse/[A-Za-z-]*\">"
    regex_clip_li = r"<li>"
    regex_clip_lislash = r"</li>"

    clip = [regex_clip_new_line,
            regex_clip_carriage_return,
            regex_clip_l1,
            regex_clip_l2,
            regex_clip_l3,
            regex_clip_href_a,
            regex_clip_example_href,
            regex_clip_example_href_span,
            regex_clip_italic,
            regex_clip_example,
            regex_clip_bold,
            regex_clip_li,
            regex_clip_lislash,
            regex_clip_bold_xref,
            regex_clip_a
    ]

    return clip

def fetch_number(definition):
    find = ['[0-9]*.']
    clip = ['[.]']
    number = capture(definition, find, clip, 1)
    number = int(number)
    return number


def fetch_main_description(dirty_definition):
    find = []
    clip = ['[0-9]+[.]', '<span class=\"dbox-italic\">', '<li>.+?</ol>',
            ':[ ]*<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">.+?</span>',
            '<span class=\"dbox-bold\">', '</span>', '[ ]*<ol class="def-sub-list">[ ]*', '</a>',
            '<a class=\"dbox-xref dbox-roman\" href=\"http://www.dictionary.com/browse/circuit-board\">']
    context = capture(dirty_definition, find, clip, 1)
    find = ['<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">.+?</span>']
    clip = ['<li>.+?</ol>', '</span>', '<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">']
    example = capture(dirty_definition, find, clip, 1)


    return Description(context, example)

def make_sublist(descriptions):
    sub_list = []
    find_context = ['<li>.*</li>']
    clip_context = ['<li>[ ]*','[ ]*</li>','[ ]*<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">.+?</span>','</span>']
    find_example = ['<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">.+?</span>']
    clip_example = ['<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">','</span>']
    for description in descriptions:
        context = capture(description, find_context, clip_context, 1)
        example = capture(description, find_example, clip_example, 1)
        description = Description(context, example)
        sub_list.append(description)
    return sub_list

def fetch_additional_descriptions(definition):
    find = ['<li>.+?</li>']
    clip = []
    dirty_sublist = capture(definition, find, clip)
    if(len(dirty_sublist) != 0):
        return make_sublist(dirty_sublist)
    else:
        return []

def make_definition(dirty_definition):        # :: String
    number = fetch_number(dirty_definition)
    main_description = fetch_main_description(dirty_definition)
    addition_description = fetch_additional_descriptions(dirty_definition)
    definition = Definition(number, main_description, addition_description)
    return definition

def make_definitions(dirty_definitions):    # :: [String]
    definitions = []                        # :: [Definition]
    for dirty_definition in dirty_definitions:
        definitions.append(make_definition(dirty_definition))
    return definitions

def fetch_root(html):
    find = ["Define [a-zA-Z-]* at Dictionary.com</title>"]
    clip = ["Define ", " at Dictionary.com</title>"]
    root = capture(html, find, clip)[0]
    return root

def fetch_accociated_words(html):
    find = "href=\"http://www.dictionary.com/browse/[a-zA-Z]*"
    clip = "href=\"http://www.dictionary.com/browse/"
    accociated_words = set(capture(html, find, clip))

def fetch_section(section_definitions, pos, find):
    find = find_definition(find)
    clip = clip_definition()
    pos_definition = capture(section_definitions, find, clip)

    if(pos_definition != []):
        definitions = make_definitions(pos_definition)
        return Section(pos, definitions)
    else:
        return Section(pos, [])

def add_section(section, sections):
    if(section != []):
        sections.extend(section)

def fetch_sections(html):
    find = [
        "<div class=\"deep-link-synonyms\">.+?<div class=\"tail-wrapper\">.+?<div class=\"tail-box tail-type-origin pm-btn-spot\" data-pm-btn-target=\".tail-content\" >"]
    clip = []
    definition_section = capture(html, find, clip, 1)

    sections = []

    find = "<span class=\"dbox-pg\">noun</span>.+?</header>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)

    if(section.definitions != []):
        sections.append(section)

    find = "<span class=\"dbox-pg\">verb .used without object.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.VERB_USED_WITHOUT_OBJECT, find)
    if(section.definitions != []):
        sections.append(section)

    find = "<span class=\"dbox-pg\">verb .used with object.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.VERB_USED_WITH_OBJECT, find)
    if(section.definitions != []):
        sections.append(section)

    ## Adjective ##
    find = "<span class=\"dbox-pg\">adjective.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.ADJECTIVE, find)
    if(section.definitions != []):
        sections.append(section)

    ## Adverb ##
    find = "<span class=\"dbox-pg\">adverb.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.ADVERB, find)
    if(section.definitions != []):
        sections.append(section)

    ## Pronoun ##
    find = "<span class=\"dbox-pg\">pronoun.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.PRONOUN, find)
    if(section.definitions != []):
        sections.append(section)

    ## Conjunction ##
    find = "<span class=\"dbox-pg\">conjunction</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.CONJUNCTION, find)
    if(section.definitions != []):
        sections.append(section)

    ## Determiner ##
    find = "<span class=\"dbox-pg\">determiner.</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.DETERMINER, find)
    if(section.definitions != []):
        sections.append(section)

    ## Exclamation ##
    print('SECTION\n')
    print(sections)
    return sections

def fetch_related_forms(html):
    find = ["Related forms[ ]*<button class=\"button-source\"[ ]*type=\"button\">Expand</button>.+?<div class=\"tail-header[ ]*\"[ ]*>",
            "<span class=\"dbox-bold\" data-syllable=\"[A-Za-z·]*, \">[A-Za-z]*, </span>"]

    clip = ["\r", "\n", "<span class=\"dbox-bold\" data-syllable=\".+?\">",
            ",", " [ ]*</span>"]

    related_forms = capture(html, find, clip)
    return related_forms

def fetch_synonyms(thesaurus):
    find = ['<div class=\"relevancy-block\">.+?<div id="filter-[0-9]*">','<ul>.+?</ul>']
    clip = ["\r","\n","<ul>.*<span class=\"text\">","</span>.*"]
    synonyms = capture(thesaurus, find, clip)
    return synonyms

def make_word(dictionary, thesaurus):
    root = fetch_root(dictionary)
    definitions = fetch_sections(dictionary)
    related_forms = fetch_related_forms(dictionary)
    synonyms = fetch_synonyms(thesaurus)

    word = Word(root, definitions, related_forms, synonyms)

    print(word)
    return word

def fetch_word(word):

    dictionary_url = "http://www.dictionary.com/browse/" + word + "/"
    dictionary = requests.get(dictionary_url).text
    thesaurus_url = "http://www.thesaurus.com/browse/" + word + "/"
    thesaurus = requests.get(thesaurus_url).text

    word = make_word(dictionary, thesaurus)

    return word

main()
