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
import sys
import pymysql

#conneting mysql database
db = pymysql.connect( host = 'localhost', user = 'root', passwd = '', db='dbcrawl')
# prepare a cursor object using cursor() method
cursor = db.cursor()

# sql = "INSERT INTO `page_information` (`base_url`, `html5`, `title`, `description`, `keywords`, `content_text`, `hot_url`, `model_crawl`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

url = "https://www.indosport.com/basket"
html5 = "no"
hot_url = "no"
title = "Berita Olahraga Basket - INDOSPORT"
description = "Berita Basket, NBA, IBL"

# update database
sql = "UPDATE page_information SET hot_url = %s WHERE base_url = %s"
# Execute the query
cursor.execute(sql, (hot_url, url))
# commit to save our changes
db.commit()

# check table exist
cursor.execute(
    "SELECT base_url, COUNT(*) FROM page_information WHERE base_url = %s GROUP BY base_url",
    (url,)
)
# Add THIS LINE
results = cursor.fetchall()
# gets the number of rows affected by the command executed
row_count = cursor.rowcount
if row_count == 0:
    print("It Does Not Exist")
else:
    print("It Exist")

# Close the connection
db.close()