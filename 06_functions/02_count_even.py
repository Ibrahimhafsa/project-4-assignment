def count_even():
    lst = [] #Initialize an empty list

    while True:
        user_input = input("Enter an integar or press enter to stop: ")

        if user_input == "": #stop if Enter is pressed
            break

        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("Invalid input. Please enter in integar.")

    even_count = sum(1 for num in lst if num % 2 == 0) 

    print(f"Number of even numbers: {even_count}")


def main():
    count_even()


if __name__ == "__main__":
    main()    