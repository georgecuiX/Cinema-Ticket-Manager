"""
Program Description:
The problem is calculating the total amount of revenue from selling tickets to a movie theatre.
The user acts as the customers and in the end, the amount of revenue from all the transactions is outputted.

There are 10 seats in the theatre, each costing $50. The user is prompted to buy a ticket and if bought, will reserve
the seat and contribute to the total amount of revenue. If the seat they want to purchase is taken, prompt the user to
buy a different ticket.

The user should also be able to see the updated layout of the theatre to observe which seats are taken or reserved at
any given time. When the user chooses to exit, the total income is outputted, and if half the seats are bought, the
cinema made a profit. If not, the cinema lost money.
"""

# Function to display income statistic and if the cinema made profit
def income_statistics():

    # Print the total revenue
    print(f"Total revenue = ${ttl_income}")

    # If the total revenue is greater than or equal to 250 (5+ seats sold), output that profit has been made
    if ttl_income >= 250:
        print("Profit has been made!")

    # If total revenue is less than 250 (0 - 5 seats sold), output that money has been lost
    else:
        print("Money has been lost!")

# Function to buy ticket to the concert
def buy_ticket(num_seats, seat_list):

    # Changes that are made to ttl_income will be done so globally
    global ttl_income

    # Initialize flag variable to be true for loop to function
    flag = True

    # Loop iterates when flag is True
    while flag == True:

        # Prompt user for a seat number
        seat_num = int(input("Enter a seat number (1 to 10): "))

        # If the seat number is greater than the number of seats available, prompt user for seat number again
        if seat_num > num_seats:
            print("Invalid seat number")

        # Compare the chosen seat character with the character X.
        # Prompt user that the ticket has been purchased if chosen seat character is an X
        elif seat_list[seat_num - 1] == "X":
            print("The ticket for that seat has already been purchased")

        # If seat number is valid and not reserved
        else:
            # Ask user if they want to buy the ticket (Assume user inputs valid input)
            option = input("This seat costs $50, would you like to purchase a ticket for it (y/n)?\n")

            # If user inputs "y"
            if option == "y":

                # Modify seat character to be an X
                seat_list[seat_num - 1] = "X"
                # Print statement which shows that payment has been made
                print("Successful Transaction!")

                # Increment the total income by 50
                ttl_income += 50

                # Set the flag variable to be false to redirect the user to the theatre menu
                flag = False

            # If user inputs "n"
            elif option == "n":
                # Set the flag variable to be false to redirect the user to the theatre menu
                flag = False

            # If user inputs an invalid value, tell them, and continue iterating through the loop
            else:
                print("Invalid Input")

# Function to print the concert layout and display if each seat is taken or not
def print_concert(num_seats, seat_list):

    # Print the seat layout
    print("Seat Layout:")
    # Ensure seats and surroundings are correctly aligned
    print("|||", end = " ")

    # Print the row of seats separated by a space
    for i in range(num_seats):
        print(seat_list[i], end = " ")

    # Print characters to represent a theatre layout
    print("|||")
    for i in range(27):
        # Ensure the lines are printed all in one line using end
        print("|", end = "")

    # Print an empty line for clarity purposes
    print()

# Main function
if __name__ == "__main__":

    # Initialize list for seats
    seat_list = []
    # Ten seats in the theatre
    num_seats = 10

    # Append each seat in the theatre with the character "S" (Represents available seat)
    for i in range(num_seats):
        seat_list.append("S")

    # Initialize total income (Will be altered through the global keyword)
    ttl_income = 0

    # Initialize flag variable to be true for loop to function
    flag = True

    # Loop iterates when flag is True
    while flag == True:

        # Prompt user to navigate the theatre menu
        print("\nWelcome to the theatre menu! What would you like to do?")
        # Assumes user inputs an integer
        print('Enter "1" to show the concert layout')
        print('Enter "2" to buy a ticket')
        print('Enter "3" to exit')

        # Store user input
        choice = int(input())

        # If user inputted 1
        if choice == 1:

            # Call the print_concert function, passing the number of seats and the list of seats as arguments
            print_concert(num_seats, seat_list)

        # If user inputted 2
        elif choice == 2:
            # Call the buy_ticket function, passing the number of seats and the list of seats as arguments
            buy_ticket(num_seats, seat_list)

        # If user inputted 3
        elif choice == 3:
            # Call the income_statistics function to display the total revenue and if the cinema made profit
            income_statistics()

            # Set flag to be False, breaking out of the loop, ultimately terminating the program
            flag = False

        # If user inputted an invalid number, tell them, and iterate through the loop again
        else:
            print("Please enter a valid number")
