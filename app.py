import requests

response = requests.get(
    "https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest")

unique_emails = {} #set - needs to be unique
user_domain_count = {}
april_emails = []

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