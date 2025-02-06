def ft_filter(function, iterable):
    """
    This function takes a function and an iterable
    If function is None, it filters out only truthly values (similar to filter(None, iterable))
    Otherwise it applies function to each item and includes it in the output if function(item) return True
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
