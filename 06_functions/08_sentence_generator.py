def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:
        print(f"I'm excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid choice! Please enter 0 for Noun, 1 for Verb, or 2 for Adjective.")


def main():
    word = input("Please type a Noun, Verb or Adjective: ")
    part_of_speech = int(input("Is this a noun, verb or adjective? Type 0 for Noun, 1 for Verb, 2 for Adjective: "))
    make_sentence(word, part_of_speech)



if __name__ == "__main__":
    main()    