import requests
import re

##word = input("Word -> ");
##https://pythex.org/

class PartOfSpeech:
    Noun = 0
    Verb = 1
    Adjective = 2
    Adverb = 3
    Pronoun = 4
    Preposition = 5
    Conjunction = 6
    Determiner = 7
    Exclamation = 9

class Description:
    context = ''
    example = ''

class Definition:
    number = 1                      # :: Integer
    mainDescription = []            # :: Description
    additionalDescriptions = []     # :: [Description]

    def __init__(self, number=0, mainDescription=[], additionalDescriptions=[]):
        self.number = number
        self.mainDescription = mainDescription
        self.additionalDescriptions = additionalDescriptions

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


class Word:
    word = ''                 # :: String
    sectionDefinition = []    # :: [Definition]

    def __init__(self, word):
        self.word = word
        self.sectionDefinition = []

    def addSection(self, partofspeech, section):
        if(section != []):
            section = Section(partofspeech, section)
            self.sectionDefinition.append(section)


## Definitions ##
def find_definition(regex_section):
    regex_find_each_definition = r"<div class=\"def-set\">.+?</div>.[\n ]*</div>"
    find = [regex_section,
            regex_find_each_definition]
    return find

def clip_definition():
    regex_clip_new_line = r"\n"
    regex_clip_carriage_return = r"\r"
    regex_clip_l1 = r"<div.*number\">"
    regex_clip_l2 = r"</span>.+?\">[ ]*"
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
            ## rregex_clip_example_href,
            ## rregex_clip_example_href_span,
            ## regex_clip_italic,
            ## rregex_clip_example
            ## regex_clip_bold,
            ## regex_clip_li
            regex_clip_a
    ]

    return clip

def capture(text, find, clip, n=0):
    input = [text]
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

class Meaning:
    number = 0
    definition = None
    example = None

    def _init__(self, defintion, example):
        self.definition = defintion
        self.example = example

def cut(regex, text):
    return []

def fetchNumber(definition):
    find = ['[0-9].']
    clip = ['[.]']
    number = capture(definition, find, clip, 1)
    number = int(number[0])
    return number

def makeSublist(descriptions):
    print("makeSublist()")

def fetchAdditionalDescriptions(definition):
    print("----Fetching Sublist-----")

    # The Sublist [Definition, +? Example]



    # The Sublist [Definition, +? Example]
    print(definition)
    find = ['<ol class="def-sub-list">.+?</ol>','<li>.+?</li>']
    clip = []
    subList = capture(definition, find, clip)
    if(len(subList) != 0):
        return []
    else:
        return makeSublist(subList)


def fetchMainDescription(definition):
    print("fetchMainDescription(definition)")
    find = []
    clip = ['[0-9]+[.]', '<span class=\"dbox-italic\">', '<li>.+?</ol>', '</span>', ':.+?',
            '<div class="def-block def-inline-example"><span class="dbox-example">.+?</span>']
    context = capture(definition, find, clip, 1)
    find = ['<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">.+?</span>']
    clip = ['<li>.+?</ol>', '</span>', ':.+?<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">']
    example = capture(definition, find, clip, 1)
    print(context)
    print(example)

def makeDefinition(description):        # :: String
    print("makeDefinition()")
    print(description)

    number = fetchNumber(description)
    mainDescription = fetchMainDescription(description)
    #additionDescription = fetchAdditionalDescriptions(description)

    return []




    #re.match('<ol class="def-sub-list">.*</ol>')
    #re.match('<li>.+?</li>')
    #re.match('<span class="dbox-example">.+?</div>')    #Capture Examples

    # Also
    #re.match("Also,.+?</div>")

    #re.match('Also,.+?</div>')

    return definition

def makeDefinitions(dirtyDefinitions): # :: [String]
    definitions = []              # :: [Definition]
    for dirtyDefinition in dirtyDefinitions:
        definitions.extend(makeDefinition(dirtyDefinition))

def makeWord(root, definitions):
    word = Word(root)

    print("-----Noun Parts-----")
    find = find_definition("<span class=\"dbox-pg\">noun</span>.+?</header>.+?</section>")
    clip = clip_definition();
    dirtyDefinitions = capture(definitions, find, clip)
    definitions = makeDefinitions(dirtyDefinitions)
    word.addSection(PartOfSpeech.Noun, definitions)
    print(definitions)

    print("-----Verbs (used without object) Parts-----")
    find = find_definition("<span class=\"dbox-pg\">verb.+?.used without object.</span>.+?</section>")
    clip = clip_definition()


    print("-----Verbs (used with object) Parts-----")
    find = find_definition("<span class=\"dbox-pg\">verb .used without object.</span>.+?</section>")
    clip = clip_definition()


    ## Adjective ##
    print("-----Adjective-----")
    find = find_definition("<span class=\"dbox-pg\">adjective</span>.+?</section>")
    clip = clip_definition()


    ## Adverb ##
    print("-----Adverb-----")
    find = find_definition("<span class=\"dbox-pg\">adverb</span>.+?</section>")
    clip = clip_definition()


    ## Pronoun ##
    print("-----Pronoun-----")
    find = find_definition("<span class=\"dbox-pg\">pronoun</span>.+?</section>")
    clip = clip_definition()


    ## Conjunction ##

    ## Determiner ##

    ## Exclamation ##


def lookup_word(word):
    print("Looking up:" + word);
    request_url = "http://www.dictionary.com/browse/" + word + "/";
    print("From:" + request_url + "\n");
    html = requests.get(request_url).text;


    print("-----Title-----");
    pattern = "Define [a-zA-Z]* at Dictionary.com</title>";
    find = [pattern];
    clip = ["Define ", " at Dictionary.com</title>"];
    title = capture(html, find, clip)[0]
    print(title)

    print("-----Forming Word-----");
    find = ["<div class=\"deep-link-synonyms\">.+?<div class=\"tail-wrapper\">.+?<div class=\"tail-box tail-type-origin pm-btn-spot\" data-pm-btn-target=\".tail-content\" >"]
    clip = []
    definitions = capture(html, find, clip, 1)
    print(definitions)
    word = makeWord(title, definitions[0])

    print("-----Accociated Words-----")
    find = "href=\"http://www.dictionary.com/browse/[a-zA-Z]*"
    clip = "href=\"http://www.dictionary.com/browse/"
    accociatedWords = set(capture(html, find, clip));
    print(accociatedWords)

    print("-----Related Forms-----")

lookup_word("board")

