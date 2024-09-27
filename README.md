# Gmail Bot for Auto-Filtering Rejection Emails

## Overview
This Python-based Gmail bot automatically filters and moves rejection emails to the trash. It connects to your Gmail account and continuously checks for new unread emails. If an email contains the word "unfortunately," it will be moved to the trash, helping to keep your inbox organized and free from negativity.

## Motivation
As a computer science student currently searching for job opportunities, I understand how frustrating it can be to receive rejection emails. This bot was created to turn a potentially negative experience into a more manageable one. When life gives you lemons, make lemonade!

## Features
- **IMAP Integration**: Connects to Gmail using the IMAP protocol.
- **Automatic Email Management**: Automatically filters unwanted rejection emails.
- **Python Programming**: Demonstrates practical skills in email handling and automation.

## Requirements
- Python 3.x
- `imaplib` and `email` libraries (included in the Python standard library)

## Setup Instructions
1. Clone the repository to your local machine:
   ```bash
   git clone <your-repository-url>
   
2. Navigate to the project directory:
cd <your-project-directory>

3.Update the username and app password in the script:

Replace Example@gmail.com with your Gmail address.
Replace the empty password field with your app password.

4.Run the bot:
python gmail_bot.py

Usage
The bot will start checking your inbox for new emails every 30 seconds. If it finds a new email that contains the word "unfortunately," it will move it to the trash.

Contributing
Feel free to fork the repository, make changes, and submit pull requests!

License
This project is licensed under the MIT License.

Contact
For any questions or feedback, please reach out to me at shai.shargal@gmail.com.

