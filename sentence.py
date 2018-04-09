import re
import reprlib

word = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = word.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentences({})'.format(reprlib.repr(self.text))
