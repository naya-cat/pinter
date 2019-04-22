import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

base_url = 'https://ivanovo.hh.ru/search/vacancy?text=Python&area=32&from=suggest_post'

def parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text #Названия вакансий
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href'] #Ссылки на вакансии
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text #Компании
            text1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            text2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            content = text1 + ' ' + text2 #описание
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content
            })
        print(jobs)
    else:
        print('ERROR')



parse(base_url, headers)
