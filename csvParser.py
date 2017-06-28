import csv

ACCEPTED_MSG = """
Hi {},

We are thrilled to let you know that you are accepted to our
programming workshop.abs

Your coach is {}.

Can't wait to see you there!

Thank you,
Workshop Organizers
"""
REJECTED_MSG = """
Hi {},

We are very sorry to let you know that due to a big number
of applications we couldn't fit you at the workshop this time.abs

We hope to see you next time.abs

Thank you,
Workshop Organizers
"""


with open('application.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) #skip header row

    for row in csv_reader:
        name, email, accepted, coach, language = row

        if accepted == "Yes":
            msg = ACCEPTED_MSG.format(name, coach)
        else:
            msg = REJECTED_MSG.format(name)

        print("Send email to: {}".format(email))
        print("Email content:")
        print(msg)
