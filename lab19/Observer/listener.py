from abc import ABC, abstractmethod


class Listener(ABC):
    @property
    @abstractmethod
    def update(self, line):
        pass


class MaxLengthListener(Listener):
    def __init__(self):
        self.max_length = 0
        self.line = None

    def update(self, line):
        line_len = len(line)
        if line_len > self.max_length:
            print(f"Found new longest line: {line_len} chars.")
            self.max_length = line_len
            self.line = line


class MaxWordLengthListener(Listener):
    def __init__(self):
        self.longest_word = ""
        self.source_line = None

    def update(self, line):
        longest_word = max(line.split(), key=len)

        if len(longest_word) > len(self.longest_word):
            print(f"Found new longest word: {longest_word}, {len(longest_word)} chars.")
            self.longest_word = longest_word
            self.source_line = line


class WordCounterListener(Listener):
    def __init__(self):
        self.word_count = 0

    def update(self, line: str):
        self.word_count += len(line.split())
