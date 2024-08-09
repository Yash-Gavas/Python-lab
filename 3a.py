def dictionary_operations():
    dictionary = {}

    while True:
        print("\n1. Add entry\n2. Search word\n3. Find words by meaning\n4. Remove entry\n5. Display all words\n6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            word = input("Enter word: ")
            meaning = input("Enter meaning: ")
            dictionary[word] = meaning
        elif choice == 2:
            word = input("Enter word to search: ")
            print(f"Meaning: {dictionary.get(word, 'Word not found')}")
        elif choice == 3:
            meaning = input("Enter meaning to search: ")
            words = [word for word, mean in dictionary.items() if mean == meaning]
            print(f"Words with meaning {meaning}: {words}")
        elif choice == 4:
            word = input("Enter word to remove: ")
            dictionary.pop(word, None)
        elif choice == 5:
            for word in sorted(dictionary.keys()):
                print(f"{word}: {dictionary[word]}")
        elif choice == 6:
            break
        else:
            print("Invalid choice")

dictionary_operations()
