import os
import bs4
import requests
import re
import pandas as pd
from collections import deque, Counter
import urllib.request
from urllib.parse import urljoin
import time

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
    if len(visited_url) >= 1:
        return

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

    # extract outgoing link
    links = soup.findAll("a", href=True)

    # memasukan outgoing link kedalam queue
    for i in links:
        flag = 0

        # Complete relative URLs and strip trailing slash
        complete_url = urljoin(url, i["href"]).rstrip('/')

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
url = "https://www.cnnindonesia.com/search/?query=omnibus+law"
crawl(url)

# print("Jumlah url yg sudah dilihat:", len(visited_url))
# print("Jumlan url dalam queue:", len(url_queue))
# print("Waktu yang dibutuhkan: %s detik" % (time.time() - start_time))
