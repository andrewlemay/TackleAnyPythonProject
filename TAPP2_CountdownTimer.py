### Idea from: https://www.dataquest.io/blog/python-projects-for-beginners/
### Shows the number of days, hours, minutes, and seconds until the entered date
### Author: Andrew LeMay

from datetime import date, datetime, timedelta, time
from dateutil.relativedelta import relativedelta
invalidDate = True
while invalidDate:
    print("Please enter a year, month, and day in the future that you would like to get a countdown to.")
    year = int(input("Year (YYYY): "))
    month = int(input("Month (MM): "))
    day = int(input("Day (DD): "))

    futureDate = date(year, month, day)
    delta = futureDate - date.today()
    numDays = delta.days
    if numDays >= 0:
        invalidDate = False
        print(numDays)
        seconds = datetime.combine(datetime.now() + timedelta(days=numDays), time())
        seconds = int((seconds - datetime.now()).seconds)
        print(seconds)
        hours = seconds//3600
        seconds -= hours*3600
        minutes = seconds//60
        seconds -= minutes*60
        print(f"{month}/{day}/{year} is {numDays} days, {hours} hours, {minutes} minutes, and {seconds} seconds from now.")