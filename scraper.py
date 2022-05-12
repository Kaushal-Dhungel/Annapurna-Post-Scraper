import json
import requests
import os

endpoint = "https://bg.annapurnapost.com/api/search?title="

def scraper(url:str):
    """
    returns scrapped Annapurna Post's articles
    """
    response = requests.get(url)
    
    # if any error occurs
    if response.status_code == 404:
        return []
    
    # access the actual data we need
    items = response.json() ['data']['items']
    return items


def scrape(word:str):
    url = endpoint + word 
    filename = word + ".json"
    pages_read = None
   
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
        items = scraper(url)
        
        # if no search result exists / if after pagination no more search result esixts OR it total no of items exceeds 30 then break the loop
        if len(items) == 0 or len(result) >= 30:
            break
        
        result += items
        i += 1

    # json will be saved in this format
    value = {
        "pages_read" : i-1 if len(result)<30 else i,
        "data" : result
    }

    # if we do not get any searchresult then no need to create a json file
    if not len(result) == 0:
        with open(filename, 'w') as file:
            json.dump(value,file, indent=4)

    return value


result = scrape('काङ्ग्रेस')
# result = scrape('lol')
print(len(result['data']))
# print(result)