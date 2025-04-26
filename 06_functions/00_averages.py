def find_average(num1, num2):
    return (num1 + num2) / 2

def main():

    num1 = float(input("Enter the First number: "))
    num2 = float(input("Enter the Second number: "))

    average = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is: {average}")


if __name__ == "__main__":
    main()