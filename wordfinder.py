"""Word Finder: finds random words from a dictionary."""
import random

# This unintentionally removes the last letter of the final word
def read_and_append(path, dict):
    file = open(path, 'r')
    for line in file:
        if not line.startswith('#') and line.strip():
            line_dict = [*line]
            line_dict[-1] = ''
            line_dict[-1] = ''
            line_to_append = ''.join(line_dict)
            dict.append(line_to_append)
    file.close()

class WordFinder:

    def __init__(self, path):
        self.collection = []
        read_and_append(path, self.collection)
        print(f"{len(self.collection)} words read")

    def random(self):
        item = random.choice(self.collection)
        return item


class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)