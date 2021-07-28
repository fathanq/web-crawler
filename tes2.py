import os
import bs4
import requests
import re
import pandas as pd
from collections import deque, Counter
import urllib.request
from urllib.parse import urljoin
import time
import pymysql

u = "www.indosport.com"

list_g = []
branch = []
branch.append("www.indosport.com")
branch.append("www.adidas.com")
list_g.append(branch)
branch = []
branch.append("www.indosport.com")
branch.append("www.zalora.com")
list_g.append(branch)
result = list_g.count(u)
print(result)

# def tag_visible(element):
#     """Function untuk merapihkan content text.
#     """
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, bs4.element.Comment):
#         return False
#     if re.match(r"[\n]+", str(element)):
#         return False
#     return True

# url = "https://www.indosport.com/sepakbola/20210625/bantah-hengkang-dari-persija-karena-uang-ini-penjelasan-marc-klok"

# print("page yang sedang di crawl:", url)
# page = requests.get(url)
# request = page.content
# soup = bs4.BeautifulSoup(request, 'html.parser')

# # extract title
# title = soup.title.string
# print("judul:", title)

# # extract text content
# texts = soup.findAll(text=True)
# visible_texts = filter(tag_visible, texts)
# text = u" ".join(t.strip() for t in visible_texts)
# text = text.lstrip().rstrip()
# text = text.split(',')
# clean_text = ''
# for sen in text:
#     if sen:
#         sen = sen.rstrip().lstrip()
#         clean_text += sen+','
# complete_text = clean_text
# print(complete_text)