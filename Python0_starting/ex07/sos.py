import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def text_to_morse(text):
    return ' '.join(NESTED_MORSE[char.upper()] for char in text)


def main():
    """
    Main function that converts a given text to Morse code and prints it.
    The function expects exactly one command-line argument which should be
    a string containing only alphanumeric characters and spaces. If the
    input does not meet these criteria, an assertion error is raised with
    an appropriate message.
    Raises:
        AssertionError: If the number of command-line arguments
        is not exactly one.
        AssertionError: If the input string contains characters
        ther than alphanumeric characters and spaces.
    """
    try:
        assert len(sys.argv) == 2, "AssertionError: \
            the program takes exactly 1 arguments"
        assert all(c.isalnum() or c == " " for c in sys.argv[1]), \
            "AssertionError: the program supports only \
            alphanumeric characters and spaces"

        text = sys.argv[1]
        morse_text = text_to_morse(text)
        print(morse_text)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
