import numpy as np

def numpy_operations():
    n = int(input("Enter the size of the NxN array: "))
    
    arr = np.zeros((n, n), dtype=int)
    
    print("Enter the elements of the array row by row:")
    for i in range(n):
        for j in range(n):
            arr[i][j] = int(input(f"Element at position ({i},{j}): "))
    
    print("\nOriginal Array:")
    print(arr)
    
    print("\nArray in Reverse Order:")
    print(np.flip(arr))
    
    print("\nPrincipal Diagonal Elements:")
    print(np.diag(arr))
    
    print("\nArray Sorted in Ascending Order:")
    print(np.sort(arr, axis=None))
    
    print("\nArray Sorted in Descending Order:")
    print(np.sort(arr, axis=None)[::-1])

# Run the numpy_operations function
numpy_operations()