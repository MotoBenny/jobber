import requests
from bs4 import BeautifulSoup


"""
TODO: structure indeed URL with queries.
"""

# https://www.indeed.com/q-junior-software-engineer-l-Seattle,-WA-jobs.html?vjk=8db6a695e03d6eb2

# https://www.indeed.com/jobs?q=junior%20software%20engineer&l=Seattle%2C%20WA


url = (
    'https://www.indeed.com/jobs'
    '?q=junior%20software%20engineer'
    '&l=Seattle%2C%20WA')


def get_data(url: str) -> str:
    results = requests.get(url)
    return results.text


def html_parse_with_soup(url: str):
    html = get_data(url)
    soup = BeautifulSoup(html, 'html.parser')

    return (soup)
