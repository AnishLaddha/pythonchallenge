import requests
from bs4 import BeautifulSoup
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# trial = "44827"

# req = requests.get(base_url+trial)
# soup_data = str(BeautifulSoup(req.text, 'html.parser'))
# numbers = [int(word) for word in str(soup_data).split() if word.isdigit()]

# num_str = "".join(str(x) for x in numbers)
# print(soup_data)
# print(num_str)

def safety_check(page_text):
    i = -1
    newlet = ""
    num = ""
    while newlet != " ":
        num = newlet+num
        newlet = page_text[i]
        i-=1
    
    return num.strip("\n")
#66831
#last^^^
a=True
num_str = "79607"
while a == True:
    req = requests.get(base_url+num_str)
    soup_data = str(BeautifulSoup(req.text, 'html.parser'))
    numbers = [int(word) for word in str(soup_data).split() if word.isdigit()]
    if len(numbers) == 0:
        a=False
    num_str = "".join(str(x) for x in numbers)
    safety = safety_check(soup_data)
    if safety!=num_str:
        num_str=safety
    print(soup_data)
    print(num_str)


