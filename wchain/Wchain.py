words = []
main_word = ""


def read_file():
    for line in open("Wchain.in.txt"):
        stripped = line.strip("\n")
        words.append(stripped)
    print("Got " + str(words.pop(0)) + " words in")
    words.sort(key=lambda s: len(s))
    words.reverse()
    print(words)
    print("-------------------------------------------------")


def possible_word(words):
    for i in words:
        if i == main_word:
            words.remove(i)
    words_count = 0
    words_result = set()
    word_in_words = words[0]
    another_count = 0
    for letter in main_word:
        string = main_word.replace(letter, "")
        for word in words:
            if len(string) > len(word_in_words):
                total_result = open("wchain.out.txt", 'w')
                total_result.write(str(another_count + 1))
                words_result.add(main_word)
            else:
                if string.find(word) != -1:
                    words.remove(word)
                    words_count = words_count + 1
                    words_result.add(word)
                    total_result = open("wchain.out.txt", 'w')
                    total_result.write(str(words_count))
    print(words_result)


if __name__ == "__main__":
    read_file()
    main_word = words[0]
    possible_word(words)

