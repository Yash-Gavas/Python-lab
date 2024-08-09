def sort_tuples_by_length():
    strings = input("Enter strings separated by space: ").split()
    tuples = [(s, len(s)) for s in strings]
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    print(f"Sorted tuples: {sorted_tuples}")

sort_tuples_by_length()
