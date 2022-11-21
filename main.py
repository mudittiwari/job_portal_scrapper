import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import cloudscraper
scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 
session = HTMLSession()



def getMetaData(link):
    try:
        # print(link)
        r2 = scraper.get(link).text
        temp = BeautifulSoup(r2, 'html.parser')
        lhand=temp.select(".description__job-criteria-list > li > h3")
        rhand=temp.select(".description__job-criteria-list > li > span")
        meta_data=[]
        # print(lhand)
        for item1,item2 in zip(lhand,rhand):
            # print(item1.text.strip())
            meta_data.append((item1.text.strip(),item2.text.strip()))
        return meta_data
    except:
        print("exception")

def getAllJobs(job_title,job_state,job_country,experience):
    exp = None
    if experience == "internship":
        exp = 1
    elif experience == "entry":
        exp = 2
    elif experience == "associate":
        exp = 3
    elif experience == "senior":
        exp = 4
    elif experience == "director":
        exp = 5
    jobs_data = []
    job_title_list=job_title.split()
    job_title_string=""
    for item in job_title_list:
        job_title_string+=item+"%20"
    job_title_string=job_title_string[:-3]
    job_location=job_state+"%2C%20"+job_country
    for pagenum in range(1,10):
        url = f"https://www.linkedin.com/jobs/search?keywords={job_title_string}&location={job_location}&trk=public_jobs_jobs-search-bar_search-submit&position=1&f_E={exp}&pageNum={pagenum}"
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 '}
        r = scraper.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        try:
            table = soup.select('.jobs-search__results-list > li')
            for item in table:
                try:
                    link=item.find(class_="base-card__full-link").get("href")
                    job=item.find(class_="base-search-card__title").text.strip()
                    company=item.find(class_="base-search-card__subtitle").text.strip()
                    location=item.find(class_='base-search-card__metadata').find(class_="job-search-card__location").text.strip()
                    jobs_data.append((job,company,location,link,getMetaData(link)))
                except:
                    print("exception in jobs data")
        except:
            print("exception in getalljobs function")
    return jobs_data

def getAllJobsByComapny(company_name,country,experience):
    jobs_data = []
    exp=None
    if experience=="internship":
        exp=1
    elif experience=="entry":
        exp=2
    elif experience=="associate":
        exp=3
    elif experience=="senior":
        exp=4
    elif experience=="director":
        exp=5
    for pagenum in range(1, 10):
        url = f"https://www.linkedin.com/jobs/search?keywords={company_name}&location={country}&trk=public_jobs_jobs-search-bar_search-submit&position=1&f_E={exp}&pageNum={pagenum}"
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
        r = scraper.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        try:
            table = soup.select('.jobs-search__results-list > li')
            for item in table:
                try:
                    link = item.find(class_="base-card__full-link").get("href")
                    job = item.find(class_="base-search-card__title").text.strip()
                    company = item.find(class_="base-search-card__subtitle").text.strip()
                    location = item.find(class_='base-search-card__metadata').find(
                        class_="job-search-card__location").text.strip()
                    job_metadata=getMetaData(link)
                    # if job_metadata[0][0]=='Seniority level' and job_metadata[0][1]==experience.upper():
                    jobs_data.append((job, company, location, link, job_metadata))
                except:
                    print("exception in jobs data")
        except:
            print("exception in getalljobs function")
    return jobs_data

if __name__ == '__main__':
    while True:
        print("1. Find jobs by job title")
        print("2. Find jobs by company name")
        print("3. Exit")
        choice=int(input("type the choice"))
        if choice==1:
            print("Enter Job Title")
            job_title = input()
            print("Enter Job country")
            job_country = input()
            print("Enter job State")
            job_state = input()
            print("Enter experience")
            experience = input()
            jobs_data = getAllJobs(job_title, job_state, job_country, experience)
            print(jobs_data)
            print(len(jobs_data))
        elif choice==2:
            company_name=input("Enter company name")
            country=input("Enter country")
            experience=input("Enter experience")
            jobs=getAllJobsByComapny(company_name,country,experience)
            print(jobs)
            print(len(jobs))
        else:
            break

