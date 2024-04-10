import numpy as np
from testsort import test_trouble

np.random.seed(0)
arr = np.random.randint(0,10001, size = 10000)

error_index = test_trouble(arr)
if error_index == -1:
    print("Trouble Sorted")
else:
    print(f"failed at index: {error_index}")