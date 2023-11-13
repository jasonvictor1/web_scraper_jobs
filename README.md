# Python Job Board Scraper

This Python script uses the `requests` and `BeautifulSoup` libraries to scrape job postings from the Python job board.

## Description

The script sends an HTTP GET request to the Python job board at 'https://www.python.org/jobs/'. It then parses the HTML content of the page, searches for job posting titles, and prints each title to the console.

## Dependencies

- Python 3
- `requests`
- `beautifulsoup4`

## Setup and Execution

1. Ensure you have Python 3 installed on your machine.
2. Install the required Python packages:
pip install requests beautifulsoup4

3. Run the script:
python job_scraper.py


## How It Works

1. The script imports the necessary libraries.
2. It sends a GET request to the Python job board.
3. The HTML content of the response is parsed using BeautifulSoup.
4. The script finds all `<h2>` tags with the class 'listing-company', which contain the job postings.
5. It iterates over these elements, extracts, and prints the job titles.

