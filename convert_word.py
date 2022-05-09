def main():
    input_file = '/home/zubair/game/word.txt'
    print('hello')

    output_file = '/home/zubair/game/new_word.txt'
    five_letter_word = []

    with open(input_file, "r") as f:
        for line in f.readlines():
            # print("line is", line)
            word = line.strip()
            if len(word) == 5:
                five_letter_word.append(word)
    with open(output_file, "w") as f:
        for word in five_letter_word:
            f.write(word + '\n')
        print(f"Found{len(five_letter_word)} in the word")


if __name__ == '__main__':
    main()
