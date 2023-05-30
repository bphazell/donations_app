# displays menue options
def show_homepage():
    print("""
          === DonateMe Homepage   ===         
  
    ------------------------------------------
    | 1.    Login     | 2.    Register      |
    
    ------------------------------------------
    | 3.    Donate    | 4.    Show Donations |
    ------------------------------------------ 
    |          5.    Exit                    |
    ------------------------------------------ """)

# Prompts user to input amoutn to donate and records username and amount in a string

# checks if donation is a positive number.


def donation_validation(donation):
    try:
        float(donation)
        if float(donation) <= 0:
            return 0
        else:
            return 1
    except ValueError:
        return 0


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    valid_username = donation_validation(donation_amt)
    if valid_username == 1:
        donation_string = username + " donated $" + donation_amt
        print("Thank you for your donation")
        # retruns a list where [0] contains string record of transaction
        # and [1] returns value donated as a float
        return [donation_string, float(donation_amt)]
    else:
        print("Donation must be a positive number")

# Displays all donations and users who made them


def show_donations(donation_string_list, donation_amt_list):
    print("\n--- All Donations ---")
    # checks if there are any donations
    if len(donation_string_list) == 0:
        print("Currently, there are no donations. ")
    else:
        # iterate through donation_string_list and print all records
        for donation in donation_string_list:
            print(donation)
        # sum donation_amt_list and print as string
        donation_toal = str(sum(donation_amt_list))
        print("Total = $" + donation_toal)
