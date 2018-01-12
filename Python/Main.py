import requests
import re
from enum import Enum

class rbnode:
    def __init__(self, key):
        self.key = key
        self.isRed = False
        self.left = None
        self.right = None
        self.p = None

class rbtree:
    def __init__(self):
        self.root = self.nil

    def search(self, key, x=None):
        print('search')

    def minimum(self, key, x=None):
        print('minimum')

    def maximum(self, key, x=None):
        print('maximum')

    def insert_key(self, key):
        print('insert key')

    def insert_node(self, z):
        print('insert node')

    def insert_fixup(self, z):
        print('insert_fixup')

    def left_rotate(self, x):
        print('left_rotate')

    def right_rotate(self, y):
        print('right_rotate')

    def check_invariants(self):
        print('check_invariants')
        
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

class Description:
    context = ''
    example = ''

    def __init__(self, context, example):
        self.context = context
        self.example = example

class Definition:
    number = 1                      # :: Integer || Char
    mainDescription = []            # :: Description
    additionalDescriptions = []     # :: [Description]

    def __init__(self, number=0, main_description=[], additional_descriptions=[]):
        self.number = number
        self.mainDescription = main_description
        self.additionalDescriptions = additional_descriptions

    def setMainDescription(self, mainDescription):
        self.mainDescription = mainDescription

    def setAdditionalDescription(self, additionalDescriptions):
        self.additionalDescriptions = additionalDescriptions

class Section:
    partOfSpeech = ''           # :: Part of Speech
    definitions = []            # :: [Definition]

    def __init__(self, pos, definitions):
        self.partOfSpeech = pos
        self.definitions = definitions

    def setPartOfSpeech(self, pos):
        self.partOfSpeech = pos

    def setDefinitions(self, definitions):
        self.definitions = definitions

class Sections:
    sections = []
    def __init__(self, sections=[]):
        self.sections = sections

    def addSection(self, section):
        if(section.definitions != []):
            self.sections.append(section)

class Word:
    word = ''                   # :: String
    sectionDefinition = []      # :: [Definition]
    difficultyIndex = 0         # :: Integer
    nearbyWords =   []          # :: [String]
    relatedForms = []           # :: [String]
    canBeConfused = []          # :: [String]
    origin = ''                 # :: String
    synonyms = []               # :: Synonyms

    def __init__(self, word):
        self.word = word
        self.sectionDefinition = []

    def addSection(self, partofspeech, section):
        if(section != []):
            section = Section(partofspeech, section)
            self.sectionDefinition.append(section)

class Meaning:
    number = 0
    definition = None
    example = None

    def _init__(self, definition, example):
        self.definition = definition
        self.example = example

def capture(text, find, clip, n=0):
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
    regex_clip_href_a = r"<a class=\"dbox-xref dbox-roman\" href=\"http://www.dictionary.com/browse/[a-zA-Z]*\">"
    regex_clip_a = r"</a>"
    regex_clip_example_href = r"[ ]*<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">"
    regex_clip_example_href_span = r"</span>"
    regex_clip_italic = r"<span class=\"dbox-italic\">"
    regex_clip_example = r"<span class=\"dbox-example\">"
    regex_clip_bold = r"<span class=\"dbox-bold\">"
    regex_clip_li = r"<li>"

    clip = [regex_clip_new_line,
            regex_clip_carriage_return,
            regex_clip_l1,
            regex_clip_l2,
            regex_clip_l3,
            regex_clip_href_a,
            #regex_clip_example_href,
            #regex_clip_example_href_span,
            regex_clip_italic
            ## regex_clip_example
            ## regex_clip_bold,
            ## regex_clip_li
            ## regex_clip_a
    ]

    return clip

def fetch_number(definition):
    find = ['[0-9].']
    clip = ['[.]']
    number = capture(definition, find, clip, 1)
    number = int(number[0])
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
        context = capture(description, find_context, clip_context)
        example = capture(description, find_example, clip_example)
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

def fetch_root(html):
    print("-----Title-----")
    find = ["Define [a-zA-Z-]* at Dictionary.com</title>"]
    clip = ["Define ", " at Dictionary.com</title>"]
    root = capture(html, find, clip)[0]
    return root

def fetch_accociated_words(html):
    print("-----Accociated Words-----")
    find = "href=\"http://www.dictionary.com/browse/[a-zA-Z]*"
    clip = "href=\"http://www.dictionary.com/browse/"
    accociated_words = set(capture(html, find, clip))

def fetch_section(section_definitions, pos, find):
    find = find_definition(find)
    clip = clip_definition()
    pos_definition = capture(section_definitions, find, clip)
    print(pos_definition)
    if(pos_definition != []):
        definitions = make_definition(pos_definition)
        return Section(pos, definitions)
    else:
        return Section(pos, [])

def fetch_sections(html):
    print("-----Forming Word-----")
    find = [
        "<div class=\"deep-link-synonyms\">.+?<div class=\"tail-wrapper\">.+?<div class=\"tail-box tail-type-origin pm-btn-spot\" data-pm-btn-target=\".tail-content\" >"]
    clip = []
    definition_section = capture(html, find, clip, 1)

    sections = Sections()

    print("-----Noun Parts-----")
    find = "<span class=\"dbox-pg\">noun</span>.+?</header>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)
    print(section.definitions)

    print("-----Verbs (used without object) Parts-----")
    find = "<span class=\"dbox-pg\">verb .used without object.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)
    print(section.definitions)

    print("-----Verbs (used with object) Parts-----")
    find = "<span class=\"dbox-pg\">verb .used with object.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)
    print(section.definitions)

    ## Adjective ##
    print("-----Adjective-----")
    find = "<span class=\"dbox-pg\">adjective.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)

    ## Adverb ##
    print("-----Adverb-----")
    find = "<span class=\"dbox-pg\">adverb.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)
    print(section.definitions)

    ## Pronoun ##
    print("-----Pronoun-----")
    find = "<span class=\"dbox-pg\">pronoun.+?</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)

    ## Conjunction ##
    print("-----Conjunction-----")
    find = "<span class=\"dbox-pg\">conjunction</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)
    print(section.definitions)

    ## Determiner ##
    print("-----Determiner-----")
    find = "<span class=\"dbox-pg\">verb.+?.used without object.</span>.+?</section>"
    section = fetch_section(definition_section, PartOfSpeech.NOUN, find)
    sections.addSection(section)
    print(section.definitions)

    ## Exclamation ##
    return sections

def fetch_difficultyIndex(html):
    print("-----Difficulty Index-----")

def fetch_nearby_words(html):
    print("-----Nearby Words-----")

def fetch_related_forms(html):
    print("-----Related Forms-----")

def fetch_can_be_confused(html):
    print("-----Can Be Confused-----")

def fetch_origin(html):
    print("-----Origin-----")

def make_word(html):

    word = ''                   # :: String
    sections = []               # :: [Section]
    difficultyIndex = 0         # :: Integer
    nearbyWords =   []          # :: [String]
    relatedForms = []           # :: [String]
    canBeConfused = []          # :: [String]
    origin = ''                 # :: String
    synonyms = []               # :: [String]

    root = fetch_root(html)
    print(root)

    definitions = fetch_sections(html)
    print(definitions)

    difficulty_index = fetch_difficultyIndex(html)
    print(difficulty_index)

    nearby_words = fetch_nearby_words(html)
    print(nearby_words)

    related_forms = fetch_related_forms(html)
    print(related_forms)

    can_be_confused = fetch_can_be_confused(html)
    print(can_be_confused)

    origin = fetch_origin(html)
    print(origin)

    find = []
    clip = []

def lookup_word(word):
    print("Looking up:" + word);
    request_url = "http://www.dictionary.com/browse/" + word + "/";
    print("From:" + request_url + "\n");
    html = requests.get(request_url).text;

    word = make_word(html);

lookup_word("silver-tongued")

