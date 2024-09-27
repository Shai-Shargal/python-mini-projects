#By Shai Shmuel Shargal
import imaplib
import email
from email.policy import default
import time


# Function to login to Gmail
def login_to_gmail(username, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com") #Access to gmail server
    mail.login(username, password)
    return mail


# Function to check if the email contains the keyword
def email_contains_keyword(msg, keyword):
    if msg.is_multipart():#checking if the email is of type Multipart
        for part in msg.iter_parts(): #It checks if the content type of the part is text/plain, meaning it is intended to display plain text.
            if part.get_content_type() == 'text/plain':
                decoded_payload = part.get_payload(decode=True).decode(errors='replace')
                if keyword.lower() in decoded_payload.lower(): #this line provides a means to check for the presence of the word or phrase within the message in a flexible, case-insensitive manner.
                    return True
    else:
        decoded_payload = msg.get_payload(decode=True).decode(errors='replace')
        if keyword.lower() in decoded_payload.lower(): #The function checks if the keyword is present in the decoded content
            return True #ignoring case differences
    return False


# Function to move an email to trash
def move_to_trash(mail, msg_id):
    try:
        mail.store(msg_id, '+X-GM-LABELS', '\\Trash')
        print(f"Moved message ID {msg_id} to trash.")
    except Exception as e: #ensure that any errors that occur while attempting to move an email are handled properly,
        print(f"Failed to move message ID {msg_id}: {e}") #providing useful error messages


# Main function to run the bot
def run_bot(username, password):
    try:
        mail = login_to_gmail(username, password)
        print("Checking for new emails...")

        last_msg_id = None  # Initialize variable to store last processed email ID

        while True:
            mail.select("inbox") #Selects the inbox folder to work with
            status, messages = mail.search(None, 'UNSEEN')  # Look for unseen emails , Uses the search method to look for unseen emails in the inbox It returns a status and a list of message IDs for the emails that match the search criteria.

            if status == 'OK' and messages[0]: #Checks if the search was successful (status == 'OK') and whether there are any unseen messages (messages[0]).
                msg_ids = messages[0].split() #Splits the string of message IDs into a list and assigns it to msg_ids. Each ID corresponds to an unseen email.
                latest_msg_id = msg_ids[-1]  # Get the last unseen email

                # Only process if it's a new email (not processed before)
                if latest_msg_id != last_msg_id: #Checks if the latest message ID is different from the last processed message ID. This ensures that the bot only processes new emails.
                    last_msg_id = latest_msg_id  # Update last processed ID
                    _, msg_data = mail.fetch(latest_msg_id, '(RFC822)') #Fetches the full email data for the latest unseen email using its message ID. The '(RFC822)' argument indicates that the complete message should be retrieved.
                    msg = email.message_from_bytes(msg_data[0][1], policy=default) #Converts the raw byte data of the email into an email.message.Message object for easier manipulation and analysis.

                    if email_contains_keyword(msg, "Unfortunately"): #Calls the email_contains_keyword function to check if the email contains the word "Unfortunately". If it does, the next line will execute
                        move_to_trash(mail, latest_msg_id)
            else:
                print("No new emails found.")

            time.sleep(30)  # Wait before checking again , Pauses the execution of the loop for 30 seconds before checking for new emails again. This helps reduce the frequency of requests to the email server.

    except Exception as e:
        print(f"An error occurred: {e}")
    finally: #The finally block ensures that the logout method is called to close the connection to the Gmail server, regardless of whether an error occurred or not.
        mail.logout()



# Example usage
if __name__ == "__main__":
    username = "Example@gmail.com"  # Your Gmail address
    password = ""         # Your App Password
    run_bot(username, password)


