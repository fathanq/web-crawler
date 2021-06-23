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

#conneting mysql database
db = pymysql.connect( host = 'localhost', user = 'root', passwd = '', db='dbcrawl')
# prepare a cursor object using cursor() method
cursor = db.cursor()

# daftar url yang akan dicrawl
url_queue = deque([])

# daftar url yang sudah di crawl
visited_url = []


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


def crawl(url):
    """Function untuk crawling page.
    """
    # kondisi berhenti
    time_now = time.time() - start_time
    time_now_int = int(time_now)
    if time_now_int >= 30:
        return
    # if len(visited_url) >= 1:
    #     return

    # memasukan url kedalam visited_url
    visited_url.append(url)

    # crawl page
    print("page yang akan di crawl:", url)
    page = requests.get(url)
    request = page.content
    soup = bs4.BeautifulSoup(request, 'html.parser')

    # extract title
    title = soup.title.string
    # print("judul:", title)

    # extract text content
    texts = soup.findAll(text=True)
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
    # print(complete_text)

    # Create a new record
    sql = "INSERT INTO `page_content` (`base_url`, `title`, `content_text`) VALUES (%s, %s, %s)"
    # Execute the query
    cursor.execute(sql, (url, title, complete_text))
    # commit to save our changes
    db.commit()

    # extract style
    for style in soup.findAll('style'):
        # Create a new record
        sql = "INSERT INTO `style_resource` (`base_url`, `style`) VALUES (%s, %s)"
        # Execute the query
        cursor.execute(sql, (url, style))
        # commit to save our changes
        db.commit()

    # extract script
    for script in soup.findAll('script'):
        # Create a new record
        sql = "INSERT INTO `script_resource` (`base_url`, `script`) VALUES (%s, %s)"
        # Execute the query
        cursor.execute(sql, (url, script))
        # commit to save our changes
        db.commit()

    # extract lists
    for lists in soup.findAll('li'):
        # Create a new record
        sql = "INSERT INTO `list` (`base_url`, `list`) VALUES (%s, %s)"
        # Execute the query
        cursor.execute(sql, (url, lists))
        # commit to save our changes
        db.commit()

    # extract forms
    for form in soup.findAll('form'):
        # Create a new record
        sql = "INSERT INTO `forms` (`base_url`, `form`) VALUES (%s, %s)"
        # Execute the query
        cursor.execute(sql, (url, form))
        # commit to save our changes
        db.commit()

    # extract tables
    for table in soup.findAll('table'):
        # Create a new record
        sql = "INSERT INTO `tables` (`base_url`, `tables`) VALUES (%s, %s)"
        # Execute the query
        cursor.execute(sql, (url, table))
        # commit to save our changes
        db.commit()

    # extract images
    for image in soup.findAll('img'):
        # Create a new record
        sql = "INSERT INTO `images` (`base_url`, `image`) VALUES (%s, %s)"
        # Execute the query
        cursor.execute(sql, (url, image))
        # commit to save our changes
        db.commit()

    # extract outgoing link
    links = soup.findAll("a", href=True)

    # memasukan outgoing link kedalam queue
    for i in links:
        flag = 0

        # Complete relative URLs and strip trailing slash
        complete_url = urljoin(url, i["href"]).rstrip('/')

        # Create a new record
        sql = "INSERT INTO `linking` (`crawl_id`, `url`, `outgoing_link`) VALUES (%s, %s, %s)"
        # Execute the query
        cursor.execute(sql, (1, url, complete_url))
        # commit to save our changes
        db.commit()

        # Check if the URL already exists in the url_queue
        for j in url_queue:
            if j == complete_url:
                flag = 1
                break

        # Check if the URL already exists in the visited_url
        for j in visited_url:
            if (j == complete_url):
                flag = 1
                break

        # If not found in queue
        if flag == 0:
            if (visited_url.count(complete_url)) == 0:
                url_queue.append(complete_url)
    
    # crawl url selanjutnya
    current = url_queue.popleft()
    crawl(current)


# time
start_time = time.time()

# titik awal: 1 situs
url = "https://www.indosport.com/"
crawl(url)

# # Create a new record
sql = "INSERT INTO `crawling` (`total_page`, `duration_crawl`) VALUES (%s, %s)"
# Execute the query
time_now = time.time() - start_time
time_now_int = int(time_now)
cursor.execute(sql, (len(visited_url), time_now_int))
# commit to save our changes
db.commit()

print("Jumlah url yg sudah dilihat:", len(visited_url))
print("Jumlan url dalam queue:", len(url_queue))
# print("Waktu yang dibutuhkan: %s detik" % (time.time() - start_time))

# Close the connection
db.close()