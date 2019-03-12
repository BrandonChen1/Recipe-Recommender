from bs4 import BeautifulSoup
from urllib.request import  urlopen

from FindAndPredict import MakePrediction

#print(MakePrediction("tomato.jpeg"))
#print(MakePrediction("Chicken.jpg"))
def ScrapeOfFoodNetwork(Link):
    fileHTML  = urlopen(Link)
    SoupySoup = BeautifulSoup(fileHTML,"html.parser")
    ingredients = SoupySoup.findAll(
        'p',
        {'class': 'o-Ingredients__a-Ingredient'}
    )
    ReturnIngredient = []
    for I in ingredients:
        ReturnIngredient.append(I.get_text())
    return ReturnIngredient

def ScrapeOfPrep(Link):
    fileHTML = urlopen(Link)
    SoupySoup = BeautifulSoup(fileHTML, "html.parser")
    ingredients = SoupySoup.findAll(
        'span',
        {'class': 'o-RecipeInfo__a-Description'}
    )
    for I in ingredients:
        print(I.get_text())
    Total = ingredients[1].get_text()
    Cook = ingredients[2].get_text()
    Prep = ingredients[3].get_text()
    #Prep,Cook,Total
    ReturnTime = []
    ReturnTime.append(Prep)
    ReturnTime.append(Cook)
    ReturnTime.append(Total)
    return ReturnTime

