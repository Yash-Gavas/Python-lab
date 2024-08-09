def array_operations():
    array = list(map(int, input("Enter numbers separated by space: ").split()))

    def find_max_min(arr):
        return max(arr), min(arr)
    
    def find_second_largest(arr):
        unique_arr = list(set(arr))
        unique_arr.remove(max(unique_arr))
        return max(unique_arr)

    max_num, min_num = find_max_min(array)
    second_largest = find_second_largest(array)
    
    print(f"Maximum number: {max_num}")
    print(f"Minimum number: {min_num}")
    print(f"Second largest number: {second_largest}")

array_operations()
