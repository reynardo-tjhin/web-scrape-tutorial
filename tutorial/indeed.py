import requests

from bs4 import BeautifulSoup

def main():

    # get the url
    url = "https://au.indeed.com/"
    query = "jobs?"
    query_parameter = "q=" + "software"
    location_parameter = "l=" + "Sydney+NSW"
    url += query + "/" + query_parameter + "&" + location_parameter


    test_url = "https://au.indeed.com/"
    test_url += "jobs?q=software&l=Sydney+NSW&ts=1727928812335&from=searchOnHP&rq=1&rsIdx=0&fromage=last&vjk=cebd2939bb4606d7"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    }

    response = requests.get(test_url, headers=headers)
    print(response.headers['Content-Type'])
    # print(response.text)

    soup = BeautifulSoup(response.text, features="html.parser")
    print(soup.prettify())

if (__name__ == "__main__"):
    main()