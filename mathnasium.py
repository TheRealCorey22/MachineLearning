import numpy as np
from typing import List


array1 = np.array([1, 3, 5])

array2 = np.array([2, 4, 6])


class NeuralMath:
    
    def arrayDotProduct(self, arr1: np.ndarray, arr2: np.ndarray) -> int:
        
        
        dot_product = np.dot(arr1, arr2)


        print(f"\nArray 1: {arr1}\nArray 2: {arr2}")

        print(f"Dot Product: {dot_product}")


        return dot_product

    def arrayMaximum(self, arr1: np.ndarray, arr2: np.ndarray) -> int:
        

        maximum = np.maximum(arr1, arr2)


        print(f"\nArray 1: {arr1}\nArray 2: {arr2}")

        print(f"Maximum: {maximum}")


        return maximum
    
    def arrayExponent(self, arr1: np.ndarray, arr2: np.ndarray) -> int:
        

        exp_arr1 = np.exp(arr1)

        exp_arr2 = np.exp(arr2)


        print(f"\nArray 1: {arr1}\nArray 2: {arr2}")

        print(f"Exponential Array 1: {exp_arr1}\nExponential Array 2: {exp_arr2}")



        return exp_arr1, exp_arr2

    def arraySum(self, arr1: np.ndarray, arr2: np.ndarray) -> int:
        

        sum_arr1 = arr1.sum()

        sum_arr2 = arr2.sum()


        print(f"\nArray 1: {arr1}\nArray 2: {arr2}")

        print(f"Array 1 Sum: {arr1}\nArray 2 Sum: {arr2}")

    
        return sum_arr1, sum_arr2

    def arrayLog(self, arr1: List[int], arr2: List[int]) -> int:
        

        log_arr1 = np.log(arr1)

        log_arr2 = np.log(arr2)


        print(f"\nArray 1: {arr1}\nArray 2: {arr2}")

        print(f"Array 1 Log: {log_arr1}\nArray 2 Log: {log_arr2}")

    

NeuralMath().arrayDotProduct(array1, array2)

NeuralMath().arrayMaximum(array1, array2)

NeuralMath().arrayExponent(array1, array2)

NeuralMath().arraySum(array1, array2)

NeuralMath().arrayLog(array1, array2)