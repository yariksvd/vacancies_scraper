from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re

opts = Options()
opts.add_argument('--incognito')
opts.add_argument('--headless')
browser = webdriver.Firefox(options=opts)
browser.get("https://rabota.ua/%d0%b2%d0%b0%d0%ba%d0%b0%d0%bd%d1%81%d0%b8%d0%b8/%d0%b2_%d0%b8%d0%bd%d1%82%d0%b5%d1%80%d0%bd%d0%b5%d1%82%d0%b5/%d1%83%d0%ba%d1%80%d0%b0%d0%b8%d0%bd%d0%b0")
html = browser.page_source

def get_city(full_location):
    return full_location[0].text.split()[0]

soup = BeautifulSoup(html, features="html.parser")
job_list = soup.find_all('div', class_="fd-f1")
with open("vacancies.txt", "w") as f:
    for job in job_list:
        job_location = job.select("p[class=fd-merchant]")
        job_title = job.find('h3', class_="fd-beefy-gunso f-vacancylist-vacancytitle")
        job_company = job.find('p', class_="f-vacancylist-companyname") 
        if None in (job_location, job_title, job_company):
            continue 
        f.writelines(f'{job_title.text.strip()}\n')
        f.writelines(f'{job_company.text.strip()}\n')
        f.writelines(f'{get_city(job_location)}\n\n')
browser.quit()