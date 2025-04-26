def main():

    num1: int = int(input("\033[1;3mPlease enter an integer to be divided:\033[0m "))
    num2: int = int(input("\033[1;3mPlease enter an integer to be divide by:\033[0m "))

    quotient: int = num1 // num2
    remainder: int = num1 % num2

    print(f"The Result of this Division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
    