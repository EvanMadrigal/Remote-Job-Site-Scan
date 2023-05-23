import requests
from bs4 import BeautifulSoup

URL = "https://remote.co/remote-jobs/developer/"
page_Html = requests.get(URL) #gets the URL

soup = BeautifulSoup(page_Html.content, "html.parser") #grabs html content from site


results = soup.find_all(class_="card-body p-0")
wanted_results = results[1]

filtered_backend_jobs = wanted_results.find_all(
    'a', href=lambda href: href and 'backend' in href)

for backend_link in filtered_backend_jobs:
    href = backend_link.get('href')
    print("remote.co" + href)

'''
backend_links = wanted_results.find_all('a')

for backend_link in backend_links:
    href = backend_link.get('href')
    print(href)

job_elements = results.find_all("div", class_="card-body px-3 py-0 pl-md-0")

backend_job_elements = [
    span_element.parent.parent.parent for span_element in backend_jobs
]

for job_element in backend_job_elements:

    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
'''
