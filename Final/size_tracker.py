"""Size Tracker Module
This module tracks the size of the specified disk and sends emails
when it reaches set thresholds (i.e. 20%, 10%, 5%, etc)

If the drive reaches 5% or under the folder is cleared and the
Apache Tomcat server is restarted automatically
"""
from send_emails import send_emails
from track_disk import get_disk_percentage
from warning_messages import MESSAGE_20_PERCENT, MESSAGE_15_PERCENT, MESSAGE_5_PERCENT

EMAIL_LIST = "C:/Size_Tracker/Final/people.csv"

def size_tracker(dirname):
    """
    Tracks size of disk and sends appropriate emails
    if they reach the 20, 15 or 5% thresholds
    """
    percentage = get_disk_percentage(dirname)

    if percentage <= 20 and percentage > 15:
        send_emails(MESSAGE_20_PERCENT, EMAIL_LIST)
    elif percentage <= 15 and percentage > 5:
        send_emails(MESSAGE_15_PERCENT, EMAIL_LIST)
    elif percentage <= 5:
        send_emails(MESSAGE_5_PERCENT, EMAIL_LIST)
