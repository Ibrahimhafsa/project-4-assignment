import math 

def main():
    ab = float(input("Enter the Length of the side AB: "))
    ac = float(input("Enter the Length of the side BC: "))

    bc = math.sqrt(ab**2 + ac ** 2)

    print(f"The Length of hypotenuse is {bc}")

if __name__ == "__main__":
    main() 