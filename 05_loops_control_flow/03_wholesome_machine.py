def main():
    affirmation = "I am capable of doing anything I put in my mind too."
    print(f"Please type the following affirmation: {affirmation}")

    while True:
        user_input = input("\033[34m") #by using this user input will get blue
        print("\033[34m", end="") #by using this color back to normal

        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("hmm That was not the affirmation. Please type the folowing affirmation:", affirmation)


if __name__=="__main__":
    main()           

