# from collections import deque, Counter
# full text page
# print(page.text)

# cek status code
# print(page.status_code)
# print(page.ok)

# dapetin gambar
# with open('said_aqil.png', 'wb') as f:
#     f.write(page.content)

# extract judul
# title = soup.title.string
# with open('url.txt', 'w') as f:
#     f.write(title)

"""
# menggabungkan 2 array ke dict
fruits = ["Apple", "Pear", "Peach", "Banana"]

url_queue = deque([])
for i in fruits:
    url_queue.append(i)

print(url_queue)

prices = [0.35, 0.40, 0.40, 0.28]
fruit_dictionary = dict(zip(url_queue, prices))
print(fruit_dictionary)

# sort
sort_orders = sorted(fruit_dictionary.items(),
                     key=lambda x: x[1], reverse=True)

url_queue.clear()
for i in sort_orders:
    # print(i[0], i[1])
    # print(i)
    url_queue.append(i[0])

# url_queue baru
print(url_queue)
"""

# try:
#     print("%s : %d" % (kata, d[kata]))
# except KeyError as d:
#     print("%s : 0" % kata)


# def hitungKata(kata, kalimat):
#     li = kalimat.split(' ')
#     list_kata = Counter(li).most_common()
#     d = {}
#     for w in list_kata:
#         d[w[0]] = w[1]
#     jumlah_kata = d[kata]
#     return jumlah_kata


# kalimat = "muhammad fathan qoriiba dimana fathan dan fathan qoriiba tidak sama qoriiba dan fathan fathan qoriiba"
# kata = "fathan qoriiba"
# hasil = kalimat.count(kata)
# print(hasil)

        # # cek eror title dan text pada facebook / twitter / google sign in
        # if(url.count("/auth/") >= 1):
        #     title = "login"
        #     complete_text = "connect acount"
        # # cek twitter
        # elif(url.count("twitter.com") >= 1):
        #     title = "twitter"
        #     complete_text = "twitter"
        # # jika tidak eror, maka ambil title dan text sesuai page
        # else:

    
        # try:
        #     res = requests.get(link)    
        #     soup = BeautifulSoup(res.text, 'lxml')
        #     try:
        #         df = soup.title.string.strip()
        #     except (AttributeError, KeyError):
        #         df = ""

        #     print(df)
        # except IOError:
        #     pass


import os
import bs4
import requests
import re
import pandas as pd
from collections import deque, Counter
import urllib.request
from urllib.parse import urljoin
import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import time
import pymysql

def tag_visible(element):
    """Function untuk merapihkan content text.
    """
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, bs4.element.Comment):
        return False
    if re.match(r"[\n]+", str(element)):
        return False
    return True

try:

    url = "http://Manchester%20City"
    page = requests.get(url)
    request = page.content
    soup = bs4.BeautifulSoup(request, 'html.parser')
    response = requests.get(url).status_code
    if response == 200:
        print("yes", response)
    else:
        print("no", response)
    
    article_html5 = soup.find('article')
    if article_html5 is None:
        texts = soup.find('body').findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        text = u" ".join(t.strip() for t in visible_texts)
        text = text.lstrip().rstrip()
        text = text.split(',')
        clean_text = ''
        for sen in text:
            if sen:
                sen = sen.rstrip().lstrip()
                clean_text += sen+','
        complete_text = clean_text
        print(complete_text)
    else:
        texts = article_html5.findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        text = u" ".join(t.strip() for t in visible_texts)
        text = text.lstrip().rstrip()
        text = text.split(',')
        clean_text = ''
        for sen in text:
            if sen:
                sen = sen.rstrip().lstrip()
                clean_text += sen+','
        complete_text = clean_text
        print(complete_text)

except (AttributeError, KeyError, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
    print("haduh")

# description = soup.find("meta", property="og:description")
# keywords = soup.find("meta", property="og:keywords")
# meta = soup.find_all('meta')
# for tag in meta:
#     if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
#         # print ('NAME    :',tag.attrs['name'].lower())
#         # print ('CONTENT :',tag.attrs['content'])
#         print(type(tag.attrs['content']))
# print(meta.rs.keys() in 'description')
# desc = soup.find("meta",attrs={"name":"description"}).get("content")
# key = soup.find("meta",attrs={"name":"keywords"}).get("content")
# key = soup.find("meta",attrs={"name":"keywords"})
# if key is None:
#     key = "-"
# else:
#     key = key.get("content")

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

# texts = soup.find_all('article')
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
#     complete_text = clean_text
# print(texts)

# Get the whole body tag
# tag = soup.body
 
# Print each string recursively
# for string in tag.strings:
#     print(string)

# print(description)
# print(keywords)