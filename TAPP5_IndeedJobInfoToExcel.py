# This is inspired by my current job hunt and needing to keep all of my applications oragnized
# This takes the url of an Indeed job posting and pulls all of the relevant information and
# puts it into an excel spreadsheet

# To use, enter your workbook name on line 14 and run the script and paste in the indeed job url
# Then go to https://rapidapi.com/mantiks-mantiks-default/api/indeed12 and sign up for an API key
# Enter that API key on line 15

import requests # used for making the call to the Indeed API
from openpyxl import load_workbook # used for writing to the excel spreadsheet
import datetime # used for getting the current date

"""Enter your workbook name and API key here. I have chosen to keep both of them hardcoded
but workbook name could be put into main and entered through input if you want separate
workbooks for different job searches"""
WB_NAME = "YOUR_WORKBOOK_NAME.xlsx"
API_KEY = "YOUR_API_KEY"

def main():
    multiple = input('Are there multiple jobs you want to add? (y/n): ')
    if multiple.lower()[:1] == 'y': # enter if there are multiple jobs to add
        job_doc = input('Enter the name of the file with the job links: ')
        with open(job_doc) as job_links: # open the file with the job links
            for link in job_links: # loop through the links
                get_job_info(link) # call the function to get the job info from the Indeed API
    else:
        job_url = input('Enter the url of the job posting: ') # get the url of the job posting
        get_job_info(job_url) # call the function to get the job info from the Indeed API
    

def get_job_info(job_url): # function to get the job info from the Indeed API
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
        pay_string = posting_dict['description'][pay_index-15: pay_index+35] # get a string that includes the entire pay range
        num_string = pay_string[pay_string.find('$'):pay_string.find("per")-1] # get a string that only includes the pay range

        if "hour" in pay_string:
            if '-' in pay_string: # if the pay is given as an hourly range
                pay_string = pay_string.replace('.00', '')
                pay_string = pay_string.replace(' ', '')
                pay = pay_string.replace('$', '') + '/hour'
            elif "From" in pay_string or "from" in pay_string: # if the pay is given as an hourly minimum
                pay_string = pay_string.replace('.00', '')
                pay_string = pay_string.replace(' ', '')
                pay = pay_string.replace('$', '') + '/hour+'
            elif "To" in pay_string or "to" in pay_string: # if the pay is given as an hourly maximum
                pay_string = pay_string.replace('.00', '')
                pay_string = pay_string.replace(' ', '')
                pay = "Up to " + pay_string.replace('$', '') + "/hour"
            else:
                pay_string = pay_string.replace('.00', '')
                pay = pay_string.replace('$', '') + '/hour'

        elif "year" in pay_string:
            if '-' in pay_string: # if the pay is given as a salary range
                pay_string = pay_string.replace('.00', '')
                pay_string = pay_string.replace(' ', '')
                pay = pay_string.replace('$', '') + '/year'
            elif "From" in pay_string or "from" in pay_string: # if the pay is given as a salary minimum
                pay_string = pay_string.replace('.00', '')
                pay_string = pay_string.replace(' ', '')
                pay = pay_string.replace('$', '') + '/year+'
            elif "To" in pay_string or "to" in pay_string: # if the pay is given as a salary maximum
                pay_string = pay_string.replace('.00', '')
                pay_string = pay_string.replace(' ', '')
                pay = "Up to " + pay_string.replace('$', '') + "/year"
        else:
            pay = "Unknown"
    except:
        pay = "Unknown"

    enter_info([job_title, company, location, pay, job_url]) # call the function to enter the info into the excel spreadsheet

    
# enters the info into the excel spreadsheet, must pass a list with the job title, company, location, pay, and url
def enter_info(info):
    wb = load_workbook(WB_NAME) # load the excel spreadsheet (must be in the same directory as the script)
    page = wb.active
    now = datetime.datetime.now()
    page.append([info[0], info[1], info[2], info[3], str(now.month) + '/' + str(now.day), info[4]]) # add the job info to the excel spreadsheet
    wb.save(filename=WB_NAME)

if __name__ == "__main__":
    main()