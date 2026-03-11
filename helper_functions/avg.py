def ft_avg(array):
    if not isinstance(array, (tuple, list)):
        raise TypeError("Input must be a tulpe or list")
    if not array:
        raise ValueError("Input cannot be empty")
    res = 0
    len = 0
    for x in array:
        if not isinstance(x, (int, float)):
            raise TypeError("All elements must be numbers")
        res += x
        len+=1
    return res/len
