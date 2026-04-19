import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# File paths
cred = os.path.join(os.getcwd(), 'creds.txt')
resume = os.path.join(os.getcwd(), 'P_Dhanush_Resume.pdf')


def start_smtp_connection():
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    return smtp_obj


def give_email_credentials():
    with open(cred, 'r') as f:
        email = f.readline().strip().strip('"')
        generated_pwd = f.readline().strip().strip('"')
    return email, generated_pwd


def get_file_contents(filepath):
    with open(filepath, 'r', encoding="utf-8") as file:
        lines = file.read().splitlines()
        subj_line = lines[0]
        content_data = "\n".join(lines[3:])
    return subj_line, content_data


def convert_email_content(from_email, to_email, content_data, subj_line):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subj_line.split(': ', 1)[1]

    # Email body
    msg.attach(MIMEText(content_data, "plain", "utf-8"))

    # Attach resume
    try:
        with open(resume, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(resume)}'
        )
        msg.attach(part)

    except FileNotFoundError:
        print(f"⚠️ Resume not found at: {resume}")

    return msg


if __name__ == "__main__":

    current_directory = os.getcwd()
    text_file_path = os.path.join(current_directory, 'Applmail.txt')

    # to_mail = [
    #     'harpreet.kaur1@programming.com',
    #     'careers.allies22@gmail.com',
    #     'ajithkaran.n@hirexera.in',
    #     'viknesh.sr@ust.com',
    #     'mahima.rawat@tdnewton.com'
    # ]
    to_mail = ['dhanushpoloJU@gmail.com','bendhana521@gmail.com']

    # Read email content
    subj_line, content_data = get_file_contents(text_file_path)
    print('✅ Email content loaded...')

    try:
        # Start SMTP session ONCE
        smtp_obj = start_smtp_connection()
        print('✅ SMTP connection established')

        email, generated_pwd = give_email_credentials()
        smtp_obj.login(email, generated_pwd)
        print('✅ Login successful')

        # Send emails
        for mail in to_mail:
            try:
                msg = convert_email_content(email, mail, content_data, subj_line)

                smtp_obj.sendmail(email, mail, msg.as_string())
                print(f"📤 Email sent to {mail}")

                time.sleep(2)  # Prevent Gmail rate limiting

            except Exception as e:
                print(f"❌ Failed for {mail}: {e}")

        smtp_obj.quit()
        print("✅ All emails processed successfully")

    except Exception as e:
        print(f"🚨 Fatal error: {e}")