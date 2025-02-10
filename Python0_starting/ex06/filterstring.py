import sys
from ft_filter import ft_filter


def filter_string(text, wordLen):
    """
    Filters words in a string based on their length.

        Parameters:
        text (str): The input string containing words.
        wordLen (int): The minimum length of words to
        be included in the output.

        Returns:
        list: A list of words from the input string that
        are longer than wordLen.
    """
    return list(ft_filter(lambda word: len(word) > wordLen, text.split()))


def main():
    """
    Parses command-line arguments and filters
    the input string based on word length.
    """
    try:
        assert len(sys.argv) == 3, "AssertionError: \
            the program need exactly two arguments"
        assert isinstance(sys.argv[1], str), "AssertionError: \
            the first argument is not a string"
        assert sys.argv[2].isdigit(), "AssertionError: \
            the second argument is not an interger"
        assert all(c.isalpha() or c == " " for c in sys.argv[1]), \
            "AssertionError: \
                the first arg should have only alpha char or space"

        text = sys.argv[1]
        wordLen = int(sys.argv[2])

        print(filter_string(text, wordLen))

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
