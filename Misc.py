
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
            #regex_clip_example_href,
            #regex_clip_example_href_span,
            regex_clip_italic,
            #regex_clip_example,
            regex_clip_bold,
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
    find = ["Define.+?at Dictionary.com</title>"]
    clip = ["Define ", " at Dictionary.com</title>"]
    root = capture(html, find, clip, 1)
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

def fetch_nearbywords(dictionary):
    find = ["<div class=\"nearby-words-inner-box\".+?</ul>", "<li>.+?</li>"]
    clip = ["\n","\t","\r",
            "<div class=\"nearby-words-inner-box\" data-linkid='lno2pu' data-ordinal='1' data-item='1'>",
            "<li>.+?<a href=\"http://www.dictionary.com/browse/.+?\">", "[ ]*</li>",
            "</a>"]
    nearbyWords = capture(dictionary, find, clip)
    return nearbyWords

def exists_dictionary(dictionary):
    find = ["<section class=\"closest-result\">.+?</section>"]
    clip = []
    cap = capture(dictionary, find, clip, 1)
    return cap == []

def exists_thesaurus(thesaurus):
    find = ["<li id=\"words-gallery-no-results\">no thesaurus results</li>"]
    clip = []
    cap = capture(thesaurus, find, clip, 1)
    return cap == []

def make_word(dictionary, thesaurus):
    root = []
    definitions = []
    related_forms = []
    nearby_words = []
    synonyms = []
    if(exists_dictionary(dictionary)):
        root = fetch_root(dictionary)
        definitions = fetch_sections(dictionary)
        related_forms = fetch_related_forms(dictionary)
        nearby_words = fetch_nearbywords(dictionary)
    else:
        return None

    if(exists_thesaurus(thesaurus)):
        synonyms = fetch_synonyms(thesaurus)

    word = Word(root, definitions, related_forms, synonyms, nearby_words)


    return word

def fetch_word(word):
    word = word.replace("/", "--")
    word = word.replace(" ", "-")
    word = word.replace("&", "-and-")

    dictionary_url = "http://www.dictionary.com/browse/" + word + "/"
    print("Fetching: " + dictionary_url)
    dictionary = requests.get(dictionary_url).text

    #print("-----DICTIONARY-----")
    #print(dictionary)

    thesaurus_url = "http://www.thesaurus.com/browse/" + word + "/"
    thesaurus = requests.get(thesaurus_url).text

    #print("-----THESAURUS-----")
    #print(thesaurus)

    word = make_word(dictionary, thesaurus)

    return word
