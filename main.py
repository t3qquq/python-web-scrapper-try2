import requests
from bs4 import BeautifulSoup

START = 0
INDEED_URL = f'https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start={START}'

indeed_result = requests.get(INDEED_URL)
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

indeed_page_number = len(indeed_soup.find('div', {'class':'pagination'}).find_all('span', {'class':'pn'}))

job_info_list = []

for page in range(indeed_page_number):
    indeed_page_soup =BeautifulSoup(requests.get(f'https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start={page*50}').text, 'html.parser')
    job_info_html = indeed_page_soup.find_all('div', {'class':'jobsearch-SerpJobCard'})

    for job_num in range(len(job_info_html)):
        job_title = job_info_html[job_num].find('a').get('title')
        job_company = job_info_html[job_num].find('span',{'class' : 'company'}).string
        if(job_info_html[job_num].find('span',{'class' : 'location'}) is not None):
            job_location = job_info_html[job_num].find('span',{'class' : 'location'}).string
        else:
            job_location = job_info_html[job_num].find('div',{'class':'location'}).string
        job_info = {'title':job_title , 'company':job_company, 'location':job_location}
        job_info_list.append(job_info)

for num in range(len(job_info_list)):
    print(job_info_list[num]) 


# indeed_page_soup =BeautifulSoup(requests.get(f'https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=0').text, 'html.parser')
# job_info_html = indeed_page_soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
# print(job_info_html[0].find('span',{'class' : 'location'}).string)