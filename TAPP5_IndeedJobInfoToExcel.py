# This is inspired by my current job hunt and needing to keep all of my applications oragnized
# This takes the url of an Indeed job posting and pulls all of the relevant information and
# puts it into an excel spreadsheet

# To use, enter your workbook name on line 14 and run the script and paste in the indeed job url
# Then go to https://rapidapi.com/mantiks-mantiks-default/api/indeed12 and sign up for an API key
# Enter that API key on line 15

import requests # used for making the call to the Indeed API
from openpyxl import load_workbook # used for writing to the excel spreadsheet
import datetime # used for getting the current date

# enter the name of your workbook here, you could also ask for input but it would be tedious
WB_NAME = 'YOUR_WORKBOOK_NAME.xlsx'
API_KEY = "YOUR_API_KEY"

job_url = input('Enter the url of the job posting: ') # get the url of the job posting
job_id = job_url[job_url.index('jk=')+3:job_url.index('&vjs')] # get the job id from the url

url = "https://indeed12.p.rapidapi.com/job/"+job_id # create the url for the Indeed API call

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "indeed12.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers) # make the call to the Indeed API

posting_dict = response.json() # convert the response to a dictionary

job_title = posting_dict['job_title'] # get the job title

company = posting_dict['company']['name'] # get the company name

location_dirty = posting_dict['location'] # get the location
location = ''.join([i for i in location_dirty if not i.isdigit()]) # remove the zip code from the location if it exists

# get the pay range (only works if it is a pay range explicitly given by the company and it is in salary form, otherwise gives "Unknown")
try:
    pay_index = posting_dict['description'].find('$') # find the index of the first dollar sign (where pay range starts)
    pay_string = posting_dict['description'][pay_index: pay_index+25] # get a string that includes the entire pay range
    pay_separated = pay_string.split(' ')
    if '.' in pay_separated[0]: # remove the decimal from the pay range if it exists
        pay_separated[0] = pay_separated[0][:pay_separated[0].index('.')]
    if '.' in pay_separated[2]: # remove the decimal from the pay range if it exists
        pay_separated[2] = pay_separated[2][:pay_separated[2].index('.')]
    pay = pay_separated[0][1:] + '-' + pay_separated[2][1:]
except:
    pay = "Unknown"

wb = load_workbook(WB_NAME) # load the excel spreadsheet (must be in the same directory as the script)
page = wb.active
now = datetime.datetime.now()
page.append([job_title, company, location, pay, str(now.month) + '/' + str(now.day), job_url]) # add the job info to the excel spreadsheet
wb.save(filename=WB_NAME)