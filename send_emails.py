"""

"""
import csv
import smtplib
from settings import SENDER_EMAIL, SENDER_PASSWORD

def send_emails(message, csv_file):
    """Sends one message to emails parsed from csv file"""
    with open(csv_file) as csv_file:
        print("Here's the message: " + message)
        csv_reader = csv.reader(csv_file, delimiter=',')

        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.ehlo()

        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

        for row in csv_reader:
            email = row
            try:
                smtp.sendmail(SENDER_EMAIL, email, message)
            except smtplib.SMTPException:
                print('wtf Yahoo')
        smtp.quit()
