
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
                string += "\t\"" + self.mainDescription.example + "\"\n"

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
