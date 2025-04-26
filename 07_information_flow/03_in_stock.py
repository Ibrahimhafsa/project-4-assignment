#funtion to check the stock of a given fruit
def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "orange": 250,
        "mango": 700,
    }    
    return inventory.get(fruit.lower(), 0) #return stock count or 0 if not found

def main():

    fruit = input("Enter a fruit: ").strip()

    stock = num_in_stock(fruit) #get number of fruit in stock

    if stock > 0:
        print("This fruit is in stock! Here is how many: ")
        print(stock)

    else:
        print("This fruit is not in stock.")



if __name__ == "__main__":
    main()
        