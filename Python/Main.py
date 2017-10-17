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
    Idioms = 10

class Word:
    root = ''
    definitions = []

class Definition:
    partOfSpeech = 0
    meaning = []

class FindObject:
    find = []
    clip = []
    def __init__(self, find, clip):
        self.find = find;
        self.clip = clip;

## Definitions ##
def createDefinitionFindObject(regex_section_object):
    regex_find_each_definition = r"<div class=\"def-set\">.+?</div>"

    regex_clip_new_line = r"\n"
    regex_clip_carriage_return = r"\r"
    regex_clip_l1 = r"<div.*number\">"
    regex_clip_l2 = r"</span>.+?\">[ ]*"
    regex_clip_l3 = r"[ ]*</div>"
    regex_clip_href_a = r"<a class=\"dbox-xref dbox-roman\" href=\"http://www.dictionary.com/browse/[a-zA-Z]*\">"
    regex_clip_a = r"</a>"
    ## rregex_clip_example_href = r"[ ]*<div class=\"def-block def-inline-example\"><span class=\"dbox-example\">"
    ## rregex_clip_example_href_span = r"</span>"
    ## regex_clip_italic = r"<span class=\"dbox-italic\">"
    ## rregex_clip_example = r"<span class=\"dbox-example\">"
    ## regex_clip_bold = r"<span class=\"dbox-bold\">"
    ## regex_clip_li = r"<li>"

    find = [regex_section_object,
            regex_find_each_definition]

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

    return FindObject(find,[])

def capture(text, findObject, n=0):
    input = [text]
    for i in range(0, len(findObject.find)):
        output = []
        for j in range(0, len(input)):
            output.extend(re.findall(findObject.find[i], input[j], re.DOTALL))
        input = output
        if len(input) == 0:
            break;

    if len(input) == 0:
        return []

    for i in range(0, len(findObject.clip)):
        for j in range(0, len(input)):
           input[j] = re.sub(findObject.clip[i], '', input[j])

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



def form_meaning(definition):

    # The Sublist [Definition, +? Example]
    numberObject = FindObject(['<span class="def-number">[0-9].'], ['<span class="def-number">','[.]'])
    number = capture(definition, numberObject, 1)
    number = int(number[0])


    # The Sublist [Definition, +? Example]
    subListObject = FindObject(['<ol class="def-sub-list">.*</ol>','<li>.+?</li>'],[])
    subList = capture(definition, subListObject)
    if(len(subList) != 0):
        print("SUBLIST------")
        print(subList)

    #re.match('<ol class="def-sub-list">.*</ol>')
    #re.match('<li>.+?</li>')
    #re.match('<span class="dbox-example">.+?</div>')    #Capture Examples

    # Also
    #re.match("Also,.+?</div>")

    #re.match('Also,.+?</div>')

    return definition

def form_definition(definitions):
    meaning = []
    for i in range(0, len(definitions)):
        meaning.extend(form_meaning(definitions[i]))


def form_word(root, definitions):
    print("-----Noun Parts-----")
    regex_find_noun_section = "<span class=\"dbox-pg\">noun</span>.+?</header>.+?</section>"
    findObjectNoun = createDefinitionFindObject(regex_find_noun_section)
    noun_section = capture(definitions, findObjectNoun)
    x = form_definition(noun_section)

    x = [PartOfSpeech.Noun, capture(definitions, findObjectNoun)]
    print(noun_section)

    print("-----Verbs (used without object) Parts-----")
    regex_find_verb_UWOO_section = "<span class=\"dbox-pg\">verb.+?.used without object.</span>.+?</section>"
    findObjectVerb_UWOO = createDefinitionFindObject(regex_find_verb_UWOO_section)
    verb_UWOO = capture(definitions, findObjectVerb_UWOO)
    print(verb_UWOO)

    print("-----Verbs (used with object) Parts-----")
    regex_find_verb_UWO_section = "<span class=\"dbox-pg\">verb .used without object.</span>.+?</section>"
    findObjectVerb_UWO = createDefinitionFindObject(regex_find_verb_UWO_section)
    verb_UWO = capture(definitions, findObjectVerb_UWO);
    print(verb_UWO)

    ## Adjective ##

    ## Adverb ##

    ## Pronoun ##

    ## Conjunction ##

    ## Determiner ##

    ## Exclamation ##
	
	## Idioms ##

##CUT ([FIND], [CLIP, REPLACE])
def lookup_word(word):
    print("Looking up:" + word);
    request_url = "http://www.dictionary.com/browse/" + word + "/";
    print("From:" + request_url + "\n");
    html = requests.get(request_url).text;


    print("-----Title-----");
    title_pattern = "Define [a-zA-Z]* at Dictionary.com</title>";
    title_find = [title_pattern];
    title_clip = ["Define ", " at Dictionary.com</title>"];
    findObjectTitle = FindObject(title_find, title_clip);
    title = capture(html, findObjectTitle)[0]
    print(title)

    print("-----Forming Word-----");
    regex_find_definitions = r"<div class=\"deep-link-synonyms\">.+?<div class=\"tail-wrapper\">.+?<div class=\"tail-box tail-type-origin pm-btn-spot\" data-pm-btn-target=\".tail-content\" >"
    findObjectDefinition = FindObject([regex_find_definitions],[])
    definitions = capture(html, findObjectDefinition, 1)
    print(definitions)
    word = form_word(title, definitions[0])

    print("-----Accociated Words-----")
    find_href = "href=\"http://www.dictionary.com/browse/[a-zA-Z]*"
    clip_href = "href=\"http://www.dictionary.com/browse/"
    findObjectAccociatedWords = FindObject([find_href], [clip_href]);
    accociatedWords = set(capture(html, findObjectAccociatedWords));
    print(accociatedWords)


lookup_word("board")