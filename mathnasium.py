import numpy as np
from typing import List


array1 = np.array([1, 3, 5])

array2 = np.array([2, 4, 6])


def arrayDotProduct(arr1: List[int], arr2: List[int]) -> int:
    
    dot_product = np.dot(arr1, arr2)


    print(f"\nArray 1: {arr1}\nArray 2: {arr2}")

    print(f"Dot Product: {dot_product}")

    
    return dot_product

arrayDotProduct(array1, array2)

