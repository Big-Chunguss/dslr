from .avg import ft_avg

def ft_std(array):
    if not isinstance(array, (tuple, list)):
        raise TypeError("Input must be a tulpe or list")
    if not array:
        raise ValueError("Input cannot be empty")
    for x in array:
        if not isinstance(x, (int, float)):
            raise TypeError("All elements must be numbers")
    avg = ft_avg(array)
    res = 0
    len = 0
    for x in array:
        res += (x - avg) ** 2
        len += 1
    return (res / len) ** 0.5
