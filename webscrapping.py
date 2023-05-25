import requests
import soupsieve.css_parser
from bs4 import BeautifulSoup
import pandas as pd
product_name = []
prices =[]
Description = []
Reviews = []
for i in range (2,12):
    url = "https://www.flipkart.com/search?q=mobile+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobile+under+10000%7CMobiles&requestId=f0a6bb85-c4dc-4a0e-90e1-765ea161dcd0&as-searchtext=mobile%20under"+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"xml")
    box = soup.find("div",class_ ="_1kfTjk")
    names = soup.find("div",class_="_3voSl0")
for i in names:
    name = i.text
    product_name.append(name)
    prices = box.findAll("div",class_="_1EcK2J _38JCdA")
for i in prices:
    name = i.text
    prices.append(name)
    descr= box.findAll('ul',class_ = "_1YokD2 _3Mn1Gg")
for i in descr:
    name = i.text
    Description.append(name)
Reviews = box.findAll('div',class_="_36fx1h _6t1WkM _3HqJxg")
for i in Reviews:
    name = i.text
    Reviews.append(name)
df = pd.DataFrame({"ProductName":product_name,"Prices":prices,"description":Description,"Reviews":Reviews})
df.to_csv("Akku1213.csv")



