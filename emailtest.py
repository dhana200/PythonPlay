import smtplib
import getpass
import os
from email.mime.text import MIMEText
import re

def start_smtp_connection():
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    return smtp_obj

def give_email_credentials():
    email = getpass.getpass(prompt='Enter your email: ')
    generated_pwd = getpass.getpass(prompt='Enter your app password: ')
    return email, generated_pwd

def get_file_contents(filepath):
    with open(filepath, 'r', encoding="utf-8") as file:  # ensure file read as utf-8
        lines = file.read().splitlines()
        subj_line = lines[0]
        content_data = "\n".join(lines[3:])
    return subj_line, content_data

def send_email(smtp_obj, msg):
    smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())

def convert_email_content(from_email, to_email, content_data, subj_line):
    # Prepare dynamic body
    number_pattern = re.compile(r'[^\d]+')
    text = 'pokalarajesh1414@gmail.com'
    recipient_name = re.findall(number_pattern,text)[0].capitalize()  # use part before '@' as name
    content = content_data.format(recipient_name)  # use part before '@' as name

    msg = MIMEText(content, "plain", "utf-8")
    msg['From'] = from_email
    msg['To'] = to_email
    # ✅ Build MIMEText object with headers
    msg['Subject'] = subj_line.split(': ', 1)[1]  # safer split

    return msg


if __name__ == "__main__":

    conection_retries,login_retries = 0, 0
    connection_waiting = True
    login_waiting = True
    login_failed = False
    current_directory = os.getcwd()
    text_file_path = os.path.join(current_directory, 'Applmail.txt')
    to_mail = 'pokalarajesh1414@gmail.com'

    subj_line, content_data = get_file_contents(text_file_path)
    print('Contents Successfully Read...!!!')

    # SMTP connection
    while connection_waiting:
        try:
            smtp_obj = start_smtp_connection()
            print('Connection Established....!!!')
        except smtplib.SMTPException as e:
            print('Error establishing SMTP connection:', e)
            conection_retries += 1
            if conection_retries > 2:
                print("Max retries exceeded. Exiting...")
                connection_waiting = False
        else:
            connection_waiting = False

    while login_waiting:
        try:
            email, generated_pwd = give_email_credentials()
            smtp_obj.login(email, generated_pwd)
            print('Login Successful....!!!')
        except smtplib.SMTPAuthenticationError as e:
            print('Error logging in:', e)
            login_retries += 1
            if login_retries > 2:
                print("Max retries exceeded. Exiting...")
                login_failed = True
                login_waiting = False
        else:
            login_waiting = False

    if not login_failed:
        msg = convert_email_content(email, to_mail, content_data, subj_line)

        # ✅ Send as string
        smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp_obj.quit()
        print("Email sent successfully!")
    