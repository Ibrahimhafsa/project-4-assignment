import hashlib

def hash_password(password):
    """Return the SHA-256 hash of the given password"""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the given email's stored password hash matches the hash of the password_to_check
    Returns True if the login is successful , else False.
    """

    if email in stored_logins: #check if email exists in stored logins
        stored_hash = stored_logins[email] #get stored hash
        return stored_hash == hash_password(password_to_check) #compare hashes
    return False # false return if email is wrong

def main():
    #stored logins(email:hash password)
    stored_logins = {
        "user@exapmle.com": hash_password("securepassword123"),
        "hafsaib@gmail.com": hash_password("mysecretpass"),
    }

    #user input
    email = input("Enter your Email: ")
    password = input("Enter your password: ")

    #check login
    if login(email, password, stored_logins):
        print("Login Successful! ✔")
    else:
        print("Login failed! ❌ Incorrect email or password.")

if __name__ == "__main__":
    main()            
