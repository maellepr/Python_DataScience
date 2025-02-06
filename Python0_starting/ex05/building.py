import sys
import string


def countCharacters(str):
    """
    This function analyse the given string

    It counts the total length of the string
    its number of uppercase character
    its number of lowercase character
    its number of punctuation character (special char)
    its number of space char
    its number of digit char
    """
    total = len(str)
    upper = sum(1 for c in str if c.isupper())
    lower = sum(1 for c in str if c.islower())
    punctuations = sum(1 for c in str if c in string.punctuation)
    space = sum(1 for c in str if c.isspace())
    digits = sum(1 for c in str if c.isdigit())

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")


def main():
    """
    Analyzes the text input and print informations about its composition

    First it checks the number of argument
    If there's one argument -> that's the text which is going to be analyse
    If there's less than one argument -> ask for an input argument
    If there's more than one argument -> AssertionError
    """
    try:
        if len(sys.argv) == 2:
            str = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("AssertionError: \
                                 more than one argument is provided")
        elif len(sys.argv) < 2:
            try:
                str = input("What is the text to count?\n ")
            except EOFError:
                pass
        countCharacters(str)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
