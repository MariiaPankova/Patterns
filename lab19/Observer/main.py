from listener import *
from publisher import *


if __name__ == '__main__':
    wc_listener = WordCounterListener()
    line_length_listener = MaxLengthListener()
    word_length_listener = MaxWordLengthListener()
    listeners = [
        line_length_listener,
        word_length_listener,
        wc_listener,
    ]
    publisher = Publisher("resources\input01.txt")

    for listener_obj in listeners:
        publisher.subscribe(listener_obj)

    while publisher.update():
        pass
    print()
    print(f"Total words: {wc_listener.word_count}")
    print(
        f"Longest line: {line_length_listener.line}, {line_length_listener.max_length} chars."
    )
    print(
        f"Longest word: {word_length_listener.longest_word}, {len(word_length_listener.longest_word)}."
    )
    print(f"Source line: {word_length_listener.source_line}")