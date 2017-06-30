"""Send Email Module
This module sends the specific message in MSG to the users specified
in the parsed CSV file
"""
import csv
import smtplib
#from datetime import datetime
from settings import SENDER_EMAIL, SENDER_PASSWORD


#CURRENT_TIME = str(datetime.now().hour) + ":" + str(datetime.now().minute)
MSG = """From: Asa Gayle <asimplesmtptest@gmail.com>
To: {} <{}>
Subject: Testing

Hello {},
It is currently {}
This is Asa Gayle testing out his SMTP client via Python. 
Please send a message back if you recieved this!

Best,
Asa Gayle

P.S. OnBase by Highland
"""

def send_emails(message, csv_file):
    """Sends one message to emails parsed from csv file"""
    with open(csv_file) as csv_file:
        print("Here's the message: " + message)
        csv_reader = csv.reader(csv_file, delimiter=',')

        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.ehlo()

        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

        for row in csv_reader:
            name, email = row
            try:
                smtp.sendmail(SENDER_EMAIL, email, message.format(name, email))
            except smtplib.SMTPException:
                print('wtf Yahoo')
        smtp.quit()
