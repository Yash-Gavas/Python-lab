def tuple_operations():
    t = (1, 2, 3, 4, 5)

    def add_item(t, item):
        return t + (item,)

    def display_length(t):
        return len(t)

    def check_item(t, item):
        return item in t

    def access_item(t, index):
        return t[index]
    
    print(t)
    t = add_item(t, 6)
    print(f"Tuple: {t}")
    print(f"Length: {display_length(t)}")
    print(f"Contains 3: {check_item(t, 3)}")
    print(f"Item at index 2: {access_item(t, 2)}")

tuple_operations()
