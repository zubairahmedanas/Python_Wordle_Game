from wordle import Wordle


def main():
    # print("hello")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Type your word: ")

        if len(x) != wordle.WORD_LENGTH:
            print(f"Word must be {wordle.WORD_LENGTH} character")
            continue

        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="\n")
    if wordle.is_solved:
        print("You have solve it")
    else:
        print("you failed...!!!")


if __name__ == "__main__":
    main()
