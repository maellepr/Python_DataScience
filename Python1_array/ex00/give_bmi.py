

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    This function takes a list of height and a list 
    of weight and returns a list of bmi
    """
    try:
        if len(height) != len(weight):
            raise ValueError("The length of the lists must be the same")
        bmi = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise ValueError("The height and weight must be numbers")
            if h <= 0 or w <= 0:
                raise ValueError("The height and weight must be greater than 0")
            bmi.append(w / h ** 2)

        return bmi
    except ValueError as e:
        print(f"Error: {e}")

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function takes a list of bmi and a limit and returns a list of booleans
    indicating if the bmi is above the limit
    """
    try:
        if not isinstance(limit, int) and not isinstance(limit, float):
            raise ValueError("The limit must be a int or a float")
        if limit < 0:
            raise ValueError("The limit must be greater than 0")
        above_limit = []
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise ValueError("The bmi must be a number")
            above_limit.append(b > limit)
        return above_limit
    except ValueError as e:
        print(f"Error: {e}")

def main():
    """
    Some tests for the functions give_bmi and apply_limit
    """
    height = [2.71, 1.15]
    weight = [90.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    

if __name__ == "__main__":
    main()