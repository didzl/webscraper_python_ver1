import requests
from bs4 import BeautifulSoup

# how to scrapping flow
# 1.get page
# 2.make request
# 3.extract job



# how many jobcard on each page
limit= 50
# using URL
URL = f"https://www.indeed.com/jobs?q=python&limit={limit}"

# bring last page return last page number
def get_last_page():
  result= requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"})

  # print(pagination)


  pages = pagination.find_all('a')

  spans = []

  # get all item except last one
  for page in pages[:-1]:
    spans.append(int(page.string))

  
  
  # delete next button
  max_page=spans[-1]

  
  return max_page

# bring job info 
def extract_job(html):
  title = html.find("h2", {"class": "title"}).find("a")["title"]
  company = html.find("span", {"class": "company"})

  if company:
    com_a= company.find("a")
    if com_a is not None:
      company = str(com_a.string)
    else:
      company = str(company.string)
    company = company.strip()
  else :
    company =None


  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]

  return {
    'title': title
    , 'company' :company
    , 'location' : location
    , "link": f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"
    }

# bring job info until last_page
def get_jobs_info(last_page):
  #use job
  jobs = []

  for page in range(last_page):
    #page check
    print(f"Scrapping indeed page: {page}")

    result = requests.get(f"{URL}&start={last_page*limit}")

    # status check
    # print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    
    # bring job info each page
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  
  # return []
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = get_jobs_info(last_page)
  return jobs