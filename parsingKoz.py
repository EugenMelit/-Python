from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium. webdriver. common. keys import Keys
from bs4 import BeautifulSoup
with open ('__pycache__\index.html') as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# page_h1 = soup.find('h1')
# print(page_h1)
# user_name = soup.find('div', class_= "user__name").find("span").text
# print(user_name)
# find_all_span_in_user__info = soup.find(class_ = "user__info").find_all("span")
# print(find_all_span_in_user__info[0].text)
# for item in find_all_span_in_user__info:
#     print(item.text)
# social_links = soup.find(class_='social__networks').find('ul').find_all('a')
# print(social_links)
all_links = soup.find_all('a')
print(all_links)
for item in all_links:
    item_text = item.text
    item_url = item.get('href')
    print(f"{item.text}:{item_url}")


