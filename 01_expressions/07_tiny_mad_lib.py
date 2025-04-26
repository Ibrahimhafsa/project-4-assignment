SENTENCE_START : str = "Panversity is fun. I Learned to program and used python to make my "

def main():
    adjective : str = (input("Enter an Adjective and press enter:"))
    noun : str = (input("Enter a Noun and press enter:"))
    verb : str = (input("Enter a Verb and press enter:"))

    print(SENTENCE_START + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()

