import requests
from bs4 import BeautifulSoup

# how to scrapping flow
# 1.get page
# 2.make request
# 3.extract job


# using URL
URL = "https://stackoverflow.com/jobs?q=python&sort=i"



def get_last_page():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser" )
  
  pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")

  last_page = pages[-2].get_text(strip=True)

  # print(last_page)

  return int(last_page)




def extract_jobs(last_page):
  jobs=[]
  print(last_page)
  for page in range(last_page):

    # 현재 295페이지를 가르키지만 정작 스크래핑은 1페이지만 함
    print(f"Scrapping stack page: {page}")

    result = requests.get(f"{URL}&pg={page+1}")
    
    
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class" : "-job"})

    for result in results:
      job = extract_job(result)
      jobs.append(job)
      
      # print(job)
    print(jobs)
    return jobs




def extract_job(html):
  # job name
  title = html.find("h2", {"class": "mb4"}).find("a")["title"]
  #print(title)


  # company name and location
  company, location = html.find("h3", {"class": "mb4"}).find_all("span", recursive=False)

  company = company.get_text(strip=True)
  location=  location.get_text(strip=True)


  # print(company, location)

  job_id = html['data-jobid']
  return{
    'title' : title
    , 'company' : company
    , 'location' : location
    , 'apply_link' : f"https://stackoverflow.com/jobs/{job_id}"
  }



def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
