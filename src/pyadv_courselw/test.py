from pyadv_courselw import algos

out = algos.add_one(1)

assert out == 2, f'output should be 2 but is {out}'

import numpy as np

my_array = np.array([1,2,3])
output = np.array([2,3,4])

my_output = algos.add_one(my_array)

assert output == my_output
