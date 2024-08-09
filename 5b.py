def longest_shortest_word():
    filename = "text.txt"
    with open(filename, 'w') as f:
        for _ in range(5):
            f.write(input("Enter line of text: ") + "\n")

    with open(filename, 'r') as f:
        words = f.read().split()

    longest = max(words, key=len)
    shortest = min(words, key=len)

    print(f"Longest word: {longest} (length: {len(longest)})")
    print(f"Shortest word: {shortest} (length: {len(shortest)})")

longest_shortest_word()
