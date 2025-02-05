def all_thing_is_obj(object: any) -> int:
    obj_types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    obj_type = type(object)


    if obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    elif obj_type in obj_types:
        obj_name = obj_types[obj_type]
        print(f"{obj_name} : {obj_type}")
    else:
        print("Type not found")

    return 42