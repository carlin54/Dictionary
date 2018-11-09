
class Word:
    word = ''                   # :: String
    sectionDefinition = []      # :: [Section]
    relatedForms = []           # :: [String]
    synonyms = []               # :: Synonyms
    nearbyWords = []            # :: [String]

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

        out += "\n"
        out += "[Nearby Words]\n"
        for i in range(0, len(self.nearbyWords)):
            out += str(self.nearbyWords[i]) + ",\t"
            counter += 1
            if(counter >= row_width):
                out += '\n'
                counter = 0
        return out

    def __init__(self, word, section_definition, related_forms, synonyms, nearby_words):
        self.word = word
        self.relatedForms = related_forms
        self.synonyms = synonyms
        self.sectionDefinition = section_definition
        self.nearbyWords = nearby_words

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, str):
            return self.word == other
        elif isinstance(other, Word):
            return self.word == other.word
        return False

    def __gt__(self, other):
        if isinstance(other, str):
            return self.word == other
        elif isinstance(other, Word):
            return self.word == other.word

    def __lt__(self, other):
        if isinstance(other, str):
            return self.word == other
        elif isinstance(other, Word):
            return self.word == other.word

    # def __gt__(self, other):
    #     s_len = len(self.word)
    #     o_len = len(other.word)
    #     min_len = min(s_len, o_len)
    #     for i in range(0, min_len):
    #         cs = ord(self.word[i])
    #         co = ord(other.word[i])
    #         if(cs > co):
    #             return True
    #         elif(cs < co):
    #             return False
    #
    #     return s_len > o_len
    #
    # def __lt__(self, other):
    #     s_len = len(self.word)
    #     o_len = len(other.word)
    #     min_len = min(s_len, o_len)
    #     for i in range(0, min_len):
    #         cs = ord(self.word[i])
    #         co = ord(other.word[i])
    #         if (cs < co):
    #             return True
    #         elif (cs > co):
    #             return False
    #
    #     return s_len < o_len

    def addSection(self, partofspeech, section):
        if(section != []):
            section = Section(partofspeech, section)
            self.sectionDefinition.append(section)
