string = ''
words = []


def read_file():
    for line in open("Wchain.in.txt"):
        stripped = line.strip("\n")
        words.append(stripped)
        # print(words)
    print("Got " + str(words.pop(0)) + " words in")
    words.sort()
    for i in words:
        print(str(i.strip("\n")) + ", ")
        print("-----------------------------------")


def math(words):
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
    # print(words_result)
    print(words_count)


if __name__ == "__main__":
    read_file()
    print("Enter main world: ")
    string = input()
    math(words)
