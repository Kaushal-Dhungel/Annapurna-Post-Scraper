import requests

endpoint = "https://bg.annapurnapost.com/api/search?title="

def scraper(url:str):
    """
    returns scrapped Annapurna Post's articles
    """
    response = requests.get(url)
   
    # if any error occurs
    if response.status_code == 400:
        return []
    
    # access the actual data we need
    items = response.json() ['data']['items']
    return items


def scrape(word:str):

    url = endpoint + word 
    result = scraper(url= url)

    # no items returned after searching
    if len(result) == 0:
        return result

    # for pagination
    i = 2    
    while True:
        url = endpoint + word + "&page=" + str(i)
        items = scraper(url)
        
        # if after pagination no more search result esixts OR it total items exceeds 30 then break the loop
        if len(items) == 0 or len(result) >= 30:
            break
        
        result += items

    return result


result = scrape('काङ्ग्रेस')
# result = scrape('lol')

# print(len(result))

print(result)