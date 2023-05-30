
from donations_pkq.hompage import show_donations, show_homepage, donate
from donations_pkq.user import login, register

# global variables
database = {"admin": "password123"}
donation_string_list = []
donation_amt_list = []
authorized_user = ""

while True:
    # display menu options
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print("Logged in as", authorized_user)
    # prompt user to input a selection
    option = input("Choose an option")
    if option == "1":
        username = input("Inpute Username: ")
        password = input("Input Password: ")
        # checks if username and password is in database
        authorized_user = login(database, username, password)
    elif option == "2":
        # Adds a new username and password to database if it doesn't exist already
        username = input("Inpute Username: ")
        password = input("Input Password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password
    elif option == "3":
        # checks if user is logged in
        if authorized_user == "":
            print("You are not logged in")
        else:
            # prompts user input a amount to donate and records donation string
            # returns a list where [0] is a string record of transaction and [1] is the numerical value
            donation = donate(authorized_user)
            # only updates donation list if a valid donation is placed
            if donation:
                # add string record to donation_string_list
                donation_string_list.append(donation[0])
                # add numeric value of donation to donation_amt_list
                donation_amt_list.append(donation[1])
    elif option == "4":
        # displays all donations
        show_donations(donation_string_list, donation_amt_list)
    elif option == "5":
        # logout user and break while loop
        print("Goodbye")
        break
    else:
        print("invalid option")
