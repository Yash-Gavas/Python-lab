import random

def odd_numbers():
    numbers = [random.randint(10, 9999) for _ in range(20)]
    print(f"Generated Numbers: {numbers}")
    odd_numbers = [num for num in numbers if num % 2 != 0 and len(str(num)) in [2, 4]]
    print(f"Odd Numbers of Length 2 and 4: {list(odd_numbers)}")

odd_numbers()

