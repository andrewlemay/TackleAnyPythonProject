# TAPP5: Job Info to Excel
# 
# This is inspired by my current job hunt and needing to keep all of my applications oragnized
# This takes the url of an Indeed or LinkedIn job posting, pulls all of the relevant information
# and puts it into an existing excel spreadsheet

# To use, enter your workbook name on line 22 and run the script and paste in the indeed job url
# Then go to https://rapidapi.com/mantiks-mantiks-default/api/indeed12 and sign up for an API key
# Enter that API key on line 23
# If you want to add multiple jobs, create a text file with the job urls separated by a new line and
# enter it on line 24

import requests # used for making the call to the Indeed API
from openpyxl import load_workbook # used for writing to the excel spreadsheet
import datetime # used for getting the current date
from bs4 import BeautifulSoup # used for parsing the LinkedIn job postings

"""Enter your workbook name, API key, and name of your text document with your job links
 here. I have chosen to keep them hardcoded but workbook name and the text document could
 be put into main and entered through input if you want separate workbooks for different 
 job searches or have different files you want to add jobs from"""
WB_NAME = "YOUR_WORKBOOK_NAME.xlsx"
API_KEY = "YOUR_API_KEY"
job_doc = "YOUR_JOB_DOC.txt"

def main():
    multiple = input('Are there multiple jobs you want to add? (y/n): ')
    if multiple.lower()[:1] == 'y': # enter if there are multiple jobs to add
        with open(job_doc) as job_links:
            for job_url in job_links:
                if "indeed" in job_url:
                    try:
                        info = get_indeed_job_info(job_url) # call the function to get the job info from the Indeed API
                        enter_info(info) # call the function to enter the info into the excel spreadsheet
                    except:
                        print("Invalid url")
                elif "linkedin" in job_url: # enter if the job is on LinkedIn
                    try:
                        info = get_linkedin_job_info(job_url) # call the function to get the job info from the LinkedIn API
                        enter_info(info)
                    except:
                        print("Invalid url")
    else:
        job_url = input('Enter the url of the job posting: ') # get the url of the job posting
        if "indeed" in job_url:
            try:
                info = get_indeed_job_info(job_url)
                enter_info(info)
            except:
                print("Invalid url")
        elif "linkedin" in job_url:
            try:
                info = get_linkedin_job_info(job_url)
                enter_info(info)
            except:
                print("Invalid url")

def get_indeed_job_info(job_url): # function to get the job info from the Indeed API
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
            if '-' in num_string: # if the pay is given as an hourly range
                num_string = num_string.replace('.00', '')
                num_string = num_string.replace(' ', '')
                pay = num_string.replace('$', '') + '/hour'
            elif "From" in pay_string or "from" in pay_string: # if the pay is given as an hourly minimum
                num_string = num_string.replace('.00', '')
                num_string = num_string.replace(' ', '')
                pay = num_string.replace('$', '') + '/hour+'
            elif "To" in pay_string or "to" in pay_string: # if the pay is given as an hourly maximum
                num_string = num_string.replace('.00', '')
                num_string = num_string.replace(' ', '')
                pay = "Up to " + num_string.replace('$', '') + "/hour"
            else:
                num_string = num_string.replace('.00', '')
                pay = num_string.replace('$', '') + '/hour'
        elif "year" in pay_string:
            if '-' in pay_string: # if the pay is given as a salary range
                num_string = num_string.replace('.00', '')
                num_string = num_string.replace(' ', '')
                pay = num_string.replace('$', '')
            elif "From" in pay_string or "from" in pay_string: # if the pay is given as a salary minimum
                num_string = num_string.replace('.00', '')
                num_string = num_string.replace(' ', '')
                pay = num_string.replace('$', '') + '+'
            elif "To" in pay_string or "to" in pay_string: # if the pay is given as a salary maximum
                num_string = num_string.replace('.00', '')
                num_string = num_string.replace(' ', '')
                pay = "Up to " + num_string.replace('$', '')
        else:
            pay = "Unknown"
    except:
        pay = "Unknown"

    return([job_title, company, location, pay, job_url])

def get_linkedin_job_info(job_url): # function to get the job info from the LinkedIn API

    response = requests.get(job_url) # get the html of the job posting
    job = response.content # convert the response to a string

    soup = BeautifulSoup(job, 'html.parser') # convert the string to a BeautifulSoup object
    
    job_title = soup.find('h1', attrs={'class':'topcard__title'}).text

    company = soup.find('a', attrs={'class':'sub-nav-cta__optional-url'}).text

    location = soup.find('span', attrs={'class':'sub-nav-cta__meta-text'}).text

    pay = "Unknown" # default pay is unknown
    # gets the pay (only works if it is an explicitly stated hourly pay)
    try:
        p = soup.find_all('p') # get all the p tags
        for i in p: 
            if '$' in i.text: # find the p tag that contains the pay
                pay_section = i.text
                pay = pay_section[pay_section.find('$')+1:pay_section.find('$')+7].rstrip() + "/hour" # get pay from the p tag and formats it
                break
    except:
        pass

    return([job_title, company, location, pay, job_url])
    
# enters the info into the excel spreadsheet, must pass a list with the job title, company, location, pay, and url
def enter_info(info):
    wb = load_workbook(WB_NAME) # load the excel spreadsheet (must be in the same directory as the script)
    page = wb.active

    now = datetime.datetime.now()
    date = str(now.month) + '/' + str(now.day)

    page.append([info[0], info[1], info[2], info[3], date, info[4]]) # add the job info to the excel spreadsheet
    wb.save(filename=WB_NAME)

if __name__ == "__main__":
    main()