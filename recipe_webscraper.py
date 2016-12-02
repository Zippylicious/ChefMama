#you need to download unirest, beautifulsoup, requests, and json if you dont have them
#pip install beautifulsoup4 
#pip install BeautifulSoup
#pip install jsonschema
#pip install requests
#pip install Unirest 
import unirest 
from bs4 import BeautifulSoup
import requests
import json

urlstack=['http://allrecipes.com/recipes/']
out_file=''
recipes={}

while len(urlstack)>0 and len(recipes)<10:
    url=urlstack.pop()
    if 'allrecipes.com/recipe' in url and '.com/recipes' not in url:
#        print url
        element = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/extract?forceExtraction=false&url="+url,
        headers={
            "X-Mashape-Key": ""#go on the account for the key or ask me for it so this actually works
        })
        recipes[element.body['title']]=[element.body['extendedIngredients'],element.body['instructions'],element.body['imageUrls']]
    if(len(urlstack)<50):
        soup=BeautifulSoup(requests.get(url).text)
        souper=soup.find_all('a')
        for link in souper:
            text=link.get('href')
            if text!=None:
                if'http://' not in text:
                    text='http://allrecipes.com'+text
                urlstack.append(text)
#                print(text)
#dump it into a json               
#with open(out_file,'w') as recipe_json:
#    json.dump(recipes,recipe_json)