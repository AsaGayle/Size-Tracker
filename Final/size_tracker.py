"""Size Tracker Module
This module tracks the size of the specified disk and sends emails
when it reaches set thresholds (i.e. 20%, 10%, 5%, etc)
"""
from send_emails import send_emails
from track_disk import get_disk_percentage

def size_tracker(dirname, thresholds):
