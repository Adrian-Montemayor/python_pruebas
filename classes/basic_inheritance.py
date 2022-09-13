class TextInput:
    def __init__(self):
        self.characters = []

    def add(self, character):
        self.characters.append(character)

    def get_value(self):
        return "".join(self.characters)

class NumericInput(TextInput):
    def __init__(self):
        super().__init__()

    def add(self, character):
        if character.isnumeric():
            self.characters.append(character)
    
    @staticmethod
    def negative():
        return -1

input = NumericInput()
input.add("1")
input.add("o")
input.add("0")
print(input.get_value())