""""""
import sched
import time
from datetime import datetime
from send_emails import send_emails
from track_disk import get_free_space_mb, get_disk_percentage

s = sched.scheduler(time.time, time.sleep)

def print_time(a='default'):asdsad
    print("From print_time", time.time(), a)

def print_some_times():
    print(time.time())
    s.enter(1, 1, print_time)
    s.enter(2, 2, print_time, argument=('positional',))
    s.enter(3, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())

print_some_times()
CURRENT_TIME = str(datetime.now().hour) + ":" + str(datetime.now().minute)
MSG = """From: Asa Gayle <asimplesmtptest@gmail.com>
Subject: Testing
         
         Hey bro it's {}. Just thought I'd let you know""".format(CURRENT_TIME)
print(MSG)
send_emails(MSG, 'people.csv')
