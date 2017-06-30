"""
Message Formats
"""

#Headers to MESSAGE_FORMAT are needed to properly send emails via SMTP Client
#Headers = The lines with From, To and Subject
MESSAGE_FORMAT = """From: Asa Gayle <asimplesmtptest@gmail.com>
To: {} <{}>
Subject: Testing

"""

MESSAGE_20_PERCENT = """From: Asa Gayle <asimplesmtptest@gmail.com>
To: {} <{}>
Subject: Testing

Hello,
This is an automated message from the automated log file tracker.
The disk currently has less than 20% remaining.
It is advised that you clear the log files soon!

Thank You!
"""

MESSAGE_15_PERCENT = """From: Asa Gayle <asimplesmtptest@gmail.com>
To: {} <{}>
Subject: Testing

Hello,
This is an automated message from the automated log file tracker.
The disk currently has less than 10% remaining.
It is advised that you clear the log files as soon as possible to avoid
future issues.

Thank You!
"""

MESSAGE_5_PERCENT = """From: Asa Gayle <asimplesmtptest@gmail.com>
To: {} <{}>
Subject: Testing

Hello,
This is an automated message from the automated log file tracker.
The disk currently has less than 5% remaining.
This message is to alert you that the log files will now be erased and the
Tomcat server will be restarted in 5 minutes. 

If there is an issue with this please stop the current process via the 
Task Scheduler on the server 

Task name is Size Tracker

Thank You!
"""