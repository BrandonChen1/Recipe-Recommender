import requests
from AllRecipeScraper import ScrapeOfFoodNetwork,ScrapeOfPrep
from decimal import Decimal
from recipe_scrapers import scrape_me
def ProductSearch(Item):
    url = "https://api.wegmans.io/products/search"

    querystring = {"query":Item,"api-version":"2018-10-18","subscription-key":"a09416d5943d41cd9c928828ebc515e1"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "6dcb4fd7-129c-4b27-b532-55ae719c7b82"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    #print(Name)
    """
    Get the price and then convert into a list contained
    ["Name","Price","SKU","Nutrition"]
    """
    Name = response.json().get("results")[0].get('name')
    SKU = response.json().get("results")[0].get('sku')
    NewList = []
    NewList.append(Name)

    Price = PriceSearch(SKU)
    NewList.append(Price)
    NewList.append(SKU)
    return NewList

"""
Takes in a SKU for price search"""
def PriceSearch(Item):

    url = "https://api.wegmans.io/products/"+Item+"/prices"

    querystring = { "api-version": "2018-10-18", "subscription-key": "a09416d5943d41cd9c928828ebc515e1"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "7cf6e77f-d4eb-4458-a24d-8d22530b84f1"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return (response.json().get('stores')[0].get('price'))


#ListofItem = ScrapeOfFoodNetwork("https://www.foodnetwork.com/recipes/food-network-kitchen/slow-cooker-beef-stew-3361678")
def GetRidofDigit(InString):
    RL = ''.join([i for i in InString if i.isdigit() == False])
    return RL

def FormatData(ListofItem):
    #ListofItem = scrape_me(Link).ingredients()
    UpdatedArray = []

    for n in ListofItem:
        UpdatedArray.append(GetRidofDigit(n))
    price = 0
    #Validate website here

    for n in UpdatedArray:
        price += ProductSearch(n)[1]
    return(ListofItem, price)



