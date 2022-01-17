import requests
# from datetime import timezone
import datetime


api_url = "https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest"


# make a GET request to the API for data
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

    try:
        date_time = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
        # utc_datetime = datetime.date.fromtimestamp(date_time, tz=timezone.utc)

        if date_time.month == 4:
            april_emails.append(email)
    except TypeError:
        print("bad date")
    except ValueError:
        print("bad date")

def remove_domains_with_only_one_email(user_domain_counts):
    """Accepts the user_domain_counts dictionary and removes any domains
    that only have one email associated. 
    Returns None.""" 
    to_delete = [key for key in user_domain_counts if user_domain_counts[key] == 1]

    for key in to_delete:
        del user_domain_counts[key]


# loop through data by the API
for data in respose_data:
    email = data["email"]
    login_date = data["login_date"]

    # add email to unique_emails if not already there
    check_unique_email(email)
    
    # add domain to user_domain_counts and increase count
    check_domain(email)

    # add email to april_emails if user logged in in April
    check_april_login(login_date, email)

# remove domains with only 1 email associated
remove_domains_with_only_one_email(user_domain_counts)


# make a POST request to the API with transformed data
try:
    request_obj = {
        "your_email_address": "ssojensen@gmail.com", 
        "unique_emails": list(unique_emails), 
        "user_domain_counts": user_domain_counts, 
        "april_emails": april_emails,
    }

    post_response = requests.post(api_url, data=request_obj)
    print(post_response.status_code)
    post_response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)



# TO DO:
#   update check_april_login to convert time to UTC first
#   add unit tests




