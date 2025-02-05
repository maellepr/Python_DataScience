import sys
import string

def countCharacters(str):
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
    try:
        if len(sys.argv) == 2:
            str = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("AssertionError: more than one argument is provided")
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