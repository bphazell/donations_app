
def login(database, username, password):
    # normalizes username so it's case insenstive
    username = username.lower()
    # Conditional logic checks if the username is containted in the database
    # and the password matches the corresponding password. Returns errors messge if not
    if username in database.keys() and password == database[username]:
        print("Welcome back admin")
        return username
    elif username in database.keys() and password != database[username]:
        print("Invalid Password")
    elif username not in database.keys():
        print("User not found, please register")


def register(database, username, password):
    # verifies username is less than 10 characters
    if len(username) > 10:
        print("Username must be less that 10 characters")
        return ""
    # verifieds password is at least 5 characters
    if len(password) < 5:
        print("Password must be at least 5 characters")
        return ""
    # normalizes username
    username = username.lower()
    # verifies username is not already in the database, if not adds to database
    if username.lower() in database.keys():
        print("Username already registered")
        return ""
    else:
        print("The username has been registered")
        return username
