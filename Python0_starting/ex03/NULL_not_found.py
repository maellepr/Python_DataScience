def NULL_not_found(object: any) -> int:
    obj_types = {
        None: "Nothing",
        float("NaN"): "Cheese",
        '0': "Zero",
        '': "Empty",
        False: "Fake"     
    }

    obj_type = type(object)

    if object is None:
        print(f"Nothing: {object} {obj_type}")
    elif type(object) is float:
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif type(object) is str and object == '':
        print (f"Empty: {type(object)}")
    elif type(object) is bool:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
    return 1