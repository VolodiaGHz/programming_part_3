string = ''
words = []


def read_file():
    for line in open("Wchain.in.txt"):
        stripped = line.strip("\n")
        words.append(stripped)
    print("Got " + str(words.pop(0)) + " words in")
    print(words)
    print("-------------------------------------------------")


def possible_word(words):
    for i in words:
        if i == string:
            words.remove(i)
    words_count = 0
    words_result = []
    for k in words:
        if string.find(k) > -1:
            words_count = words_count + 1
            words_result.append(k)
    total_result = open("wchain_out.txt", 'w')
    total_result.write(str(words_count))
    print("Count words: " + str(words_count))
    print("-------------------------------------------------")
    print(words_result)


if __name__ == "__main__":
    read_file()
    string = words[0]
    possible_word(words)
