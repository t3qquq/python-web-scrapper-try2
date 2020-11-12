import requests
from bs4 import BeautifulSoup

STACKOVERFLOW_URL = 'https://stackoverflow.com/jobs?q=python&so_source=JobSearch&so_medium=Internal&pg=1'

stackoverflow_result = requests.get(STACKOVERFLOW_URL)
stackoverflow_soup = BeautifulSoup(stackoverflow_result.text, 'html.parser')

stackoverflow_page_number = stackoverflow_soup.find('div', {'class':'s-pagination'}).find_all('a')

MAX_PAGE = int(stackoverflow_page_number[-2].find('span').string)

def stackoverflow_job_extract():

    job_info_list=[]

    for page in range(MAX_PAGE):
        stackoverflow_page_soup = BeautifulSoup(requests.get(f'https://stackoverflow.com/jobs?q=python&so_source=JobSearch&so_medium=Internal&pg={page+1}').text, 'html.parser')
        stackoverflow_info_html = stackoverflow_page_soup.find_all('div',{'class':'-job'}) 
        
        
        for job_num in range(len(stackoverflow_info_html)):
            job_title = stackoverflow_info_html[job_num].find('div',{'class':'fl1'}).find('a').get('title')
            job_company = stackoverflow_info_html[job_num].find('div',{'class':'fl1'}).find('h3').find_all('span')[0].get_text(strip=True)
            job_location = stackoverflow_info_html[job_num].find('div',{'class':'fl1'}).find('h3').find_all('span')[1].get_text(strip=True)
            job_info = {'title':job_title , 'company':job_company, 'location':job_location}
            job_info_list.append(job_info)
    
    return job_info_list