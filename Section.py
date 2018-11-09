
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
            out += str(definition)
        return out

    def setPartOfSpeech(self, pos):
        self.partOfSpeech = pos

    def setDefinitions(self, definitions):
        self.definitions = definitions
