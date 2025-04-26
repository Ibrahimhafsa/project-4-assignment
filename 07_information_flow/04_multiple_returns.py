def get_user_data():

    first_name = input("What's your First name?: ").strip()
    last_name = input("What's your Last name?: ").strip()
    email = input("What's your Email Address?: ").strip()

    return first_name, last_name, email #returning a tupple

def main():
    user_data = get_user_data()

    print("Recieved the following user data:", user_data)


if __name__=="__main__":
    main()    
