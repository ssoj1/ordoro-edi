import requests
from datetime import datetime

response = requests.get(
    "https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest")

respose_data = response.json()['data']

unique_emails = {} #set - needs to be unique
user_domain_counts = {}
april_emails = []

def check_unique_email(email):
    """Accepts a string email address and checks if it's in unique_emails. 
    If not, adds the email. 
    Returns None. 
    """
    if email not in unique_emails:
        unique_emails.add(email)


def check_domain(email):
    """Accepts a string email. If email domain is in user_domain_counts, 
    increases count by 1.
    If not, adds the domain and sets count to 1.
    Returns None. 
    """
    domain = email.split('@')[1]
    user_domain_counts[domain]= user_domain_counts.get(domain, 0) + 1

# def check_april_login(timestamp):
#     """ Accepts a timestamp from the API formatted as TO DO!!!!!!!!!!!"""
#     utc_datetime = datetime.utcfromtimestamp(timestamp)
#     print(utc_datetime)

# check_april_login('2014-04-22T09:31:56+04:00')


for data in respose_data:
    # add to unique_emails if not already there
    check_unique_email(data['email'])
    
    # add domain to user_domain_counts and increase count
    check_domain(data['email'])

    # add email to april_emails if user logged in in April




# TO DO:
#   response.status_code - for a try/ except?
#   list of distinct emails
#   number of users per domain (as a dictionary)
#   users who logged in in April (UTC) ????
#   formatted like this: 
#       {
#           "your_email_address": 'whoareu@whowho.com',
#           "unique_emails": ["email1@test.com", "email2@test.com"],
#           "user_domain_counts": {
#           "bing.com": 2,
#           "sling.com": 3
#       },
#           "april_emails": ["email1@test.com", "email2@test.com"]
#       }
#   runtime complexity


# DECISION NOTES:
    # DECISION TO USE REQUESTS
    # did a bit of research and decided to use requests library - not part of the 
    # standard library, so installed and imported

    # API DOCS SAY THE RESPONSE IS JSON
    # so using the standard library json package

    # Classes or helper functions?
    # Testability 

    # To run tests: 
        # python3 -m doctest -v app.py


# Time
    # Thinking about it after reading
        # Googled a couple of random things


#c