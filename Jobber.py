import requests
# import urllib
from bs4 import BeautifulSoup
# import time


"""
TODO: structure indeed URL with queries.
"""

url = ("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/"
       "search?keywords=Software%2BEngineer&location=Seattle%2C%2BWashington"
       "%2C%2BUnited%2BStates&locationId=&"
       "geoId=104116203&sortBy=R&f_TPR=r604800&distance=50&start=")  # 0 or 25


def linkedin_scrape(url, page_num):
    next_page = url + str(page_num)  # constructing the URL
    response = requests.get(str(next_page))  # getting content wuth requests
    # parsing content with BS4d
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('a', class_="base-card__full-link")

    scraped_jobs_list = []

    for listing in jobs:
        job_url = listing.get('href')

        response = requests.get(job_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # if we have not already seen this job, scrape its data.
        if job_url not in scraped_jobs_list:
            # gets the job post body text
            body = soup.find('div', class_="show-more-less-html__markup").text

            # a is append, W will write a new file each time
            with open('bulk_search_text.txt', 'a') as f:
                f.write('\n')
                f.write(str(job_url))  # writes the job URL
                f.write('\n' + body + '\n')
                # creates a human readable seperation between job postings

            # adds the job_url to the scraped jobs list,
            # after the scrape has been completed
            scraped_jobs_list.append(job_url)
            print(job_url)
        else:
            # if we hit this else, we have already scraped this job\
            # and should proceed to the next in the for loop.
            continue
