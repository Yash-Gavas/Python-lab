import re

def count_vowels_consonants_digits():
    text = input("Enter text: ")

    vowels = len(re.findall(r'[aeiouAEIOU]', text))
    consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text))
    digits = len(re.findall(r'\d', text))

    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")

count_vowels_consonants_digits()
