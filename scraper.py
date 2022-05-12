import json
import requests
import os
import time

endpoint = "https://bg.annapurnapost.com/api/search?title="

def scraper(url:str):
    """
    returns scrapped Annapurna Post's articles
    """

    try:
        response = requests.get(url)

        # if any error occurs
        if response.status_code == 404:
            return []
        
        # access the actual data we need
        items = response.json() ['data']['items']
        return items

    except:
        return []

def scrape(word:str):
    url = endpoint + word 
    filename = word + ".json"
    pages_read = None
    json_file = {
        "pages_read":pages_read,
        "data":[]
    }

    # the script has been already run before
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            json_file = json.loads(file.read())
            pages_read = json_file.get('pages_read')

    # for pagination
    result = []
    i = 1   
   
    # if we had previously run the script
    if pages_read:
        i = int(pages_read) + 1

    while True:
        if i > 1:
            url = endpoint + word + "&page=" + str(i)
        
        print("url is ---------------", url)

        # this to check if how the script reruns if the internet connection is lost in the middle
        if i == 2:
            print("turn wifi off")
            time.sleep(4)  

        items = scraper(url)
        
        # if no search result exists / if after pagination no more search result esixts OR it total no of items exceeds 30 then break the loop
        if len(items) == 0 or len(result) >= 30:
            break
        
        result += items
        i += 1
    
    # if we do not get any searchresult then no need to create a json file
    if not len(result) == 0:
        data = json_file['data'] + result   # add previously saved data (in json file) to the newly fetched data
        value = {   # json will be saved in this format
            "pages_read" : i-1 if len(data)<30 else i,
            "data" : data
        }
        with open(filename, 'w') as file:
            json.dump(value,file, indent=4)

        return value
    
    return json_file


result = scrape('काङ्ग्रेस')
# result = scrape('lol')
print(len(result['data']))
print(result)