import requests
import json
import re

from bs4 import BeautifulSoup

def test_use_api():
    # use the API
    url = "https://jobsearch-api-ts.cloud.seek.com.au"

    # create some query parameters
    query_parameters = {
        "siteKey": "AU-Main",
        "sourceSystem": "houston",
        "userid": "9540d0d1-ecd3-4c73-9a5d-21aa336b610c",
        "usersessionid": "9540d0d1-ecd3-4c73-9a5d-21aa336b610c",
        "eventCaptureSessionId": "9540d0d1-ecd3-4c73-9a5d-21aa336b610c",
        "where": "All+Sydney+NSW",
        "page": "1",
        "seekSelectAllPages": "true",
        "keywords": "software",
        "include": "seodata",
        "locale": "en-AU",
    }

    # get the complete url with query parameters
    complete_url = url + "/v4/counts?"
    for i, key in enumerate(query_parameters.keys()):
        if (i == 0):
            complete_url += key + "=" + query_parameters[key]
        else:
            complete_url += "&" + key + "=" + query_parameters[key]

    # get the response
    response = requests.get(complete_url)
    print(response.headers['content-type']) # get the type of responses (html/json/css/etc.)
    print(response.json())


def test_use_script():

    # get url
    url = "https://seek.com.au/"
    search_query = "software" + "-jobs"
    location_query = "in-" + "All-Sydney-NSW"
    page = "page=" + "1"
    url += search_query + "/" + location_query + "?" + page

    # get response
    response = requests.get(url)

    # use Beautiful Soup 4
    soup = BeautifulSoup(response.content, "html.parser")

    # get the data-automation attribute
    script_tag = soup.find("script", {"data-automation": "server-state"})
    script_content = script_tag.string

    # Define regular expressions to extract JSON-like data
    seek_redux_pattern = re.search(r'window\.SEEK_REDUX_DATA\s*=\s*({.*?});', script_content, re.DOTALL)

    # Extract and clean the JSON-like strings
    seek_redux_data = seek_redux_pattern.group(1) if seek_redux_pattern else None

    # Function to safely load JSON data
    def parse_json(data_str):
        try:
            return json.loads(data_str)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    # Convert to Python dictionaries
    seek_redux_data_data = parse_json(seek_redux_data) if seek_redux_data else None

    # Output the data
    print("Total Jobs Found: ", end="")
    print(seek_redux_data_data['results']['results']['summary']['displayTotalCount'])

    print("Search Parameters: ", end="")
    print(seek_redux_data_data['results']['results']['searchParams'])

    print("Number of Jobs: ", end="")
    print(len(seek_redux_data_data['results']['results']['jobs']))

    print("Job 1:")
    job = seek_redux_data_data['results']['results']['jobs'][0]
    for key in job.keys():
        print(key, job[key])


if (__name__ == "__main__"):
    test_use_script()