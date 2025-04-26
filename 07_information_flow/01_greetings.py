def greet(name):
    """print a greeting with name"""
    print(f"Greetings {name}!")


def main():
    name = input("What's your name? ")

    greet(name)

if __name__ == "__main__":
    main()    