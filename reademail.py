import imaplib
import getpass
import email

## Establish a connection to the Gmail IMAP server
M = imaplib.IMAP4_SSL('imap.gmail.com')

## Login to your Gmail account
useremail = getpass.getpass(prompt='Enter your email: ')
password = getpass.getpass(prompt='Enter your password: ')
M.login(useremail, password)

## Get the list of mailboxes
print(M.list()[1])

## Select the "Sent Mail" folder
M.select('"[Gmail]/Sent Mail"')

## Search for the email
typ, data = M.search(None, 'SUBJECT "Application for Playwright Automation role"')
mid = data[0].split()[0]
result, data = M.fetch(mid, '(RFC822)')

## convert the raw email string to a message object
raw_mail_string = data[0][1].decode('utf-8')
print(type(raw_mail_string))

## Create a message object from the raw email string
message = email.message_from_string(raw_mail_string)

## Print the email content
for part in message.walk():
    if part.get_content_type() == "text/plain":
        print(part.get_payload(decode=True).decode('utf-8'))