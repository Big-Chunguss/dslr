from helper_functions.min import ft_min
from helper_functions.max import ft_max
from helper_functions.avg import ft_avg
from helper_functions.percentile import ft_percentile
from helper_functions.std import ft_std
array = [2, 2, 0 , 1, 3 , 4 , -5]
print(ft_min(array))
print(ft_max(array))
print(ft_avg(array))
print(ft_std(array))
print(ft_percentile(array, 25))
print(ft_percentile(array, 75))