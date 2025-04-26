def subtract_seven(num):
    return num - 7 #subtract 7 from given number


def main():

    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after Subtracting 7: ", result)


if __name__=="__main__":
    main()    
