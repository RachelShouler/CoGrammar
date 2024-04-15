### --- Creating an email simulator using OOP --- ###

# --- Email Class --- #

# Create the class, constructor and methods to create a new Email object:

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

# --- Lists --- #
    # Initialise an empty list to store the email objects.

# --- Functions --- #
    # Build out the required functions for your program.


# Creating the Email class
class Email:

    # Empty variable list to store apended emails
    inbox = []

    # Constructor to initialise instance variables for each email
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address # Email address of sender
        self.subject_line = subject_line   # Subject line of email
        self.email_content = email_content # Content of the email
        self.has_been_read = False         

    # Instance method to edit the has_been_read variable to
    # True after email is read
    def mark_as_read(self):
        self.has_been_read = True
    
    
# Functions

# Populating inbox with sample emails with 
# email address, subject line, and email contents
def populate_inbox():
    Email.inbox.append(Email("yeah@gmail.com", "Welcome to HyperionDev!", 
                             "Hello student! Welcome to HyperionDev and thanks for joining us."))
    
    Email.inbox.append(Email("maybe@gmail.com", "Great work on the bootcamp!", 
                             "You are doing an excellent job. Keep it up."))
    
    Email.inbox.append(Email("nah@gmail.com", "Your excellent marks!", 
                             "Your score on the last task was excellent. Keep up the good work"))


# A function to loop through the inbox and apply
# index to each. 
def list_emails():
    # Counts number of emails in inbox then prints that number
    inbox_count = len(Email.inbox)
    if inbox_count == 0 or inbox_count > 1:
        print("_" * 30)
        print(f"\nYour Inbox - You have {inbox_count} emails.\n")
    else:
        print("_" * 30)
        print(f"\nYour Inbox - You have {inbox_count} email.\n")     
    
    # Print each email's subject_line and corresponding index
    for index, email in enumerate(Email.inbox):
        print(f"{index} Subject: {email.subject_line}")
    print("_" * 30)


# Function to display selected email with email address,
# subject line, and email content displayed.
# This function will also set has_been_read to True 
def read_email(index):
      
    print("_" * 30)
    email = Email.inbox[index]
    print(f"\nEmail {index}:\n")
    print(f"From: {email.email_address}")    # Print email address
    print(f"Subject: {email.subject_line}")  # Print subject line
    print(f"Content: {email.email_content}") # Print email content

    # Mark the email as read and print response
    email.mark_as_read()
    print(f"\nThe email from {email.email_address} has been marked as read.")
    print("_" * 30)


# Function for unread emails
def get_unread_email():
    unread_emails = [email for email in Email.inbox if not email.has_been_read]
    
    # If there are no unread emails
    if not unread_emails:
        print("_" * 30)
        print("\nYou currently have no unread emails.")
        print("_" * 30)
        
    # If there are unread emails present, print number of 
    # unread emails and subject line/s
    else:
        print("_" * 30)
        print(f"\nYou have {len(unread_emails)} unread email/s: \n")
        
        for email in unread_emails:
            print(f"Subject: {email.subject_line}")
        print("_" * 30)

# Call the function to populate the Inbox.
populate_inbox()

# --- Email Program --- #

# Generic welcome message
print("\nWelcome to your Email application.")
print("_" * 30)

# While loop for user menu options
while True:

    # Count of number of emails in the inbox
    inbox_count = len(Email.inbox)
    
    # Menu option for end user
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    
    try:

        # User chooses to read an email and there are
        # emails present in the inbox. Prestents the user
        # with the sender details, subject line, and content.
        if user_choice == '1' and inbox_count > 0 :
            list_emails()
            index = int(input("\nEnter the number of the email you want to read (0, 1, 2 etc.): "))
            read_email(index)

        # User chooses to read an email but there are
        # no emails in the inbox. Quits application.
        elif user_choice == '1' and inbox_count == 0:
            print("_" * 30)
            print("\nYou currently have no emails.")
            print("Quitting the email application.")
            print("_" * 30)
            break

        # User chooses to view unread emails    
        elif user_choice == '2':
            # Call function for unread emails
            get_unread_email()

        elif user_choice == '3':# User chooses to exit the program
            print("_" * 30)
            print("\nQuitting the email application.")
            print("_" * 30)
            break

        else: # user enters incorrect input
            print("_" * 52)
            print("\nOops - incorrect input.")
            print("_" * 52)

    except: # user enters incorrect input
        print("_" * 52)
        print("\nInvalid selection. Please enter a valid option.")
        print("_" * 52)