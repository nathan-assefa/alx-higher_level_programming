#!/usr/bin/python3

"""text_indentation function prints text with two new lines
after certain characters(:.?). This fucntioin mainly porforms two
operations, nemely removing the white space after those characters,
and spliting the text accordingly. The parameter text is the one
going to be parsed
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip() for line in text.split(delim)])

    print("{}".format(text), end="")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
