def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(words_number(file_contents), "words found in the document\n")
    letters_stats = calculate_letters(file_contents)
    sorted_list = sorted(list(letters_stats.items()), key=lambda x: -x[1])
    for c, n in sorted_list:
        print(f"The '{c}' character was found {n} times")

def words_number(text):
    words = text.split()
    return len(words)

def calculate_letters(text):
    letters = {}
    for t in text:
        t = t.lower()
        if t.isalpha():
            if t in letters:
                letters[t] += 1
            else:
                letters[t] = 1
    return letters

if __name__ == '__main__':
    main()