def prime_numbers_in_range():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

prime_numbers_in_range()
