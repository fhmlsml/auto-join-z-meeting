# PyAutoGUI soon will be added to pass the continue button after joining if there's a recorded meeting

import webbrowser
import schedule
import time

url = input("Your zoom meeting url : ") # Change with your z-meeting url

chrome_path = '/usr/bin/google-chrome' # This path is from linux ubuntu, change your own chrome path

# One Time job
def job():
    webbrowser.get(chrome_path).open(url) # Do some work that only needs to happen once...
    return schedule.CancelJob

schedule.every().day.at('15:00').do(job) # Change your meeting time

print("Waiting for the time to join . . .")

while True:
    schedule.run_pending()
    time.sleep(1)   

