def ft_percentile(array, value):
    if not isinstance(array, (tuple, list)):
        raise TypeError("Input must be a tulpe or list")
    if not array:
        raise ValueError("Input cannot be empty")
    for x in array:
        if not isinstance(x, (int, float)):
            raise TypeError("All elements must be numbers")
    if not isinstance(value, int):
        raise ValueError("input needs to be between 1 and 100")
    sorted_array = sorted(array)
    pos = int((len(array) - 1) * (value / 100))
    return sorted_array[pos]