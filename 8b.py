import re

def count_file_details():
    filename = "text.txt"
    with open(filename, 'w') as f:
        for _ in range(5):
            f.write(input("Enter line of text: ") + "\n")

    with open(filename, 'r') as f:
        text = f.read()

    upper_case = len(re.findall(r'[A-Z]', text))
    lower_case = len(re.findall(r'[a-z]', text))
    digits = len(re.findall(r'\d', text))

    print(f"Upper case letters: {upper_case}")
    print(f"Lower case letters: {lower_case}")
    print(f"Digits: {digits}")

count_file_details()
