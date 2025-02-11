def slice_me(family: list, start: int, end: int) -> list:
    """
    This function truncates a 2D array to a smaller 2D array
    based on the start and end intergers provided.

    It returns the truncated 2D array.
    """
    try:
        if not isinstance(family, list) or \
            not isinstance(start, int) or \
                not isinstance(end, int):
            raise AssertionError("Input should be a list and two integers.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("All rows should have the same length.")

        print(f"My shape is ({len(family)}, {len(family[0])})")

        x = slice(start, end)
        slicing_array = family[x]

        print(f"My new shape is ({len(slicing_array)}, \
{len(slicing_array[0])})")
        return family[start:end]
    except AssertionError as e:
        print("AssersionError:", e)
        return ""


def main():
    """
    This is the main function that calls the slice_me function
    and does some testing.
    """
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2],
              [1.75, 70.0]]

    print(slice_me(family, 0, 4))
    print(slice_me(family, 1, 3))


if __name__ == "__main__":
    main()
