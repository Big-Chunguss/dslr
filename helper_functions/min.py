def ft_min(array):
    if not isinstance(array, (tuple, list)):
        raise TypeError("Input must be a tulpe or list")
    if not array:
        raise ValueError("Input cannot be empty")
    for x in array:
        if not isinstance(x, (int, float)):
            raise TypeError("All elements must be numbers")
    res = array[0]
    for x in array:
        if x < res:
            res = x
    return res