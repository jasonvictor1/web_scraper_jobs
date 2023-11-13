# Import the 'requests' library to handle HTTP requests
import requests

# Import the 'BeautifulSoup' class from the 'bs4' module for parsing HTML
from bs4 import BeautifulSoup

# Send a GET request to the Python job board website
# The 'requests.get()' function fetches the content from the URL
# The response from the server is stored in the variable 'response'
response = requests.get('https://www.python.org/jobs/')

# Parse the HTML content of the response using BeautifulSoup
# 'response.content' contains the raw HTML content
# 'html.parser' is the parser included with Python that BeautifulSoup uses to parse HTML
# The parsed HTML is stored in the variable 'soup'
soup = BeautifulSoup(response.content, 'html.parser')

# Find all HTML elements that match the criteria: <h2> tags with the class 'listing-company'
# This is done using the 'find_all()' method of 'soup'
# The method returns a list of all matching elements, representing job postings
# These elements are stored in the variable 'job_posts'
job_posts = soup.find_all('h2', class_='listing-company')

# Iterate over each element in 'job_posts' (each job posting)
for job_post in job_posts:
    # Extract the text from the first <a> tag within each 'job_post' element
    # The text is assumed to be the job title
    # The text is stored in the variable 'title'
    title = job_post.a.text

    # Print the job title to the console
    print(title)
