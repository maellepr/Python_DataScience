import sys

def check_odd_even():
    if len(sys.argv) == 1:
        exit()

    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"

    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")
    
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    try:
        check_odd_even()
    except AssertionError as e:
        print(e)