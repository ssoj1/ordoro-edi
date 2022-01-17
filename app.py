import requests
# from datetime import timezone
import datetime
# from dateutil import parser

api_url = "https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest"

try: 
    response = requests.get(api_url)
    respose_data = response.json()["data"]
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

# Initial data structures for POST request
unique_emails = set()
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
    If email is absent, prints "bad email".
    Returns None. 
    """
    try: 
        domain = email.split("@")[1]
        user_domain_counts[domain]= user_domain_counts.get(domain, 0) + 1
    except AttributeError:
        print("bad email")

def check_april_login(timestamp, email):
    """ Accepts a time and date timestamp from the API formatted as 
    "yyyy-mm-ddThh:mm:ss+h" and checks if the month is April. 
    If so, adds the email to april_emails. 
    If email is absent, prints "bad date".
    Return None."""
    # NOT CURRENTLY CONVERTING TO UTC FIRST - TO DO
    # utc_datetime = datetime.date.fromtimestamp(timestamp, tz=timezone.utc)
    try:
        date_time = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
        if date_time.month == 4:
            april_emails.append(email)
    except TypeError:
        print("bad date")
    except ValueError:
        print("bad date")

# loop through list of dictionaries returned by the API
for data in respose_data:
    email = data["email"]
    login_date = data["login_date"]

    # add email to unique_emails if not already there
    check_unique_email(email)
    
    # add domain to user_domain_counts and increase count
    check_domain(email)

    # add email to april_emails if user logged in in April
    check_april_login(login_date, email)


request_obj = {
    "your_email_address": "ssojensen@gmail.com", 
    "unique_emails": unique_emails, 
    "user_domain_counts": user_domain_counts, 
    "april_emails": april_emails,
}
post_response = requests.post(api_url, data=request_obj)




# TO DO:
#   users who logged in in April (UTC) ????
#   add unit tests
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



