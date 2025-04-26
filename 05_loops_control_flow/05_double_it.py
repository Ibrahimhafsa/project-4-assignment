def main():
    while True:
        try:
            curr_value = int(input("Enter a number: "))
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")

if __name__ == "__main__":
    main()
