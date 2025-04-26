def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    for fruit_name in fruits:
        price = fruits[fruit_name]

        while True:
            try:
                user_input = input(f"How many {fruit_name}s do you want? ")
                amount_bought = int(user_input)
                break  # break the loop if input is valid
            except ValueError:
                print(" Please enter a valid number.")

        total_cost += (price * amount_bought)

    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
