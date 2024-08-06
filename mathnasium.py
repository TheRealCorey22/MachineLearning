import numpy as np
from typing import List


array1 = np.array([1, 3, 5])

array2 = np.array([2, 4, 6])


class NeuralMath:
    
    def arrayOperations(self, arr1: List[int], arr2: List[int]) -> int:
        

        maximum = np.maximum(arr1, arr2)


        dot_product = np.dot(arr1, arr2)


        print(f"\nArray 1: {arr1}\nArray 2: {arr2}")

        print(f"\nDot Product: {dot_product}")

        print(f"\nMaximum: {maximum}")

    
        return dot_product, maximum



        
    






NeuralMath().arrayOperations(array1, array2)
