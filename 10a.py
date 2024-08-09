def handle_specific_exceptions():
    try:
        # NameError
        print(unknown_variable)
    except NameError as e:
        print(f"NameError: {e}")

    try:
        # IndexError
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError as e:
        print(f"IndexError: {e}")

    try:
        # KeyError
        dct = {'key': 'value'}
        print(dct['unknown_key'])
    except KeyError as e:
        print(f"KeyError: {e}")

    try:
        # ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

handle_specific_exceptions()
