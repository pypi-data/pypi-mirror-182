from typing import Union

__all__ = ["int_to_word", "word_to_int"]


def int_to_word(number: int, /) -> str:
    """Returns the word version of an integer

    Parameters
    ----------
    number: `int`
        the number to be turned into its word version

    Notes
    ----------
        If number is 10 or above, it will return its number form

    Returns
    ----------
    str
        the word version

    Examples
    ----------
    >>> int_to_word(5)
    ... five

    >>> int_to_word(10)
    ... 10
    """

    return {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }.get(number, str(number))


def word_to_int(word: str, /) -> Union[int, str]:
    """Returns the number version of a word

    Parameters
    ----------
    word: `str`
        the str to be turned into its number version

    Notes
    ----------
        If the word is either 10 or above or could not be turned into a valid number will return the word given

    Returns
    ----------
    typing.Union[int, str]
        the int version, or the str version if it could not be turned into a int version

    Examples
    ----------
    >>> word_to_int('five')
    ... 5

    >>> int_to_word('test'')
    ... 'test'
    """

    return {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }.get(word, word)
