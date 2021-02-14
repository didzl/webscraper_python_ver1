import requests
from bs4 import BeautifulSoup

limit= 50
URL = f"https://www.indeed.com/jobs?q=python&limit={limit}"


def extract_indeed_pages():
  result= requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"})

  ##print(pagination)


  pages = pagination.find_all('a')

  spans = []

  for page in pages[:-1]:
    spans.append(int(page.string))

  ##get all item except last one

  
  max_page=spans[-1]

  return max_page


def extract_indeed_jobs(last_page):
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*limit}")

    print(result.status_code)
