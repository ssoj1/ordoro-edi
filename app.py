import requests
# from datetime import timezone
import datetime
# from dateutil import parser


response = requests.get(
    "https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest")

respose_data = response.json()['data']

unique_emails = set() #set - needs to be unique
user_domain_counts = {}
april_emails = []

def check_unique_email(email):
    """Accepts a string email address and checks if it's in unique_emails. 
    If not, adds the email. 
    Returns None. 
    """
    if email not in unique_emails and email is not None:
        unique_emails.add(email)


def check_domain(email):
    """Accepts a string email. If email domain is in user_domain_counts, 
    increases count by 1.
    If not, adds the domain and sets count to 1.
    Returns None. 
    """
    try: 
        domain = email.split('@')[1]
        user_domain_counts[domain]= user_domain_counts.get(domain, 0) + 1
    except AttributeError:
        print("no email")

def check_april_login(timestamp, email):
    """ Accepts a time and date timestamp from the API formatted as 
    "yyyy-mm-ddThh:mm:ss+h" and checks if their last login was in April. 
    If so, adds the email to april_emails. 
    Return None."""
    # NOT CURRENTLY CONVERTING TO UTC FIRST - TO DO
    # utc_datetime = datetime.date.fromtimestamp(timestamp, tz=timezone.utc)

    date_time = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    if date_time.month == 4:
        april_emails.append(email)


for data in respose_data:
    # add to unique_emails if not already there
    print(data['email'])
    check_unique_email(data['email'])
    
    # add domain to user_domain_counts and increase count
    check_domain(data['email'])

    # add email to april_emails if user logged in in April




# TO DO:
#   response.status_code - for a try/ except?
#   handle empty emails (null) and login_dates ("", null)
#   add try/ excepts to 3 functions
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