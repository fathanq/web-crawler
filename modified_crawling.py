from BFS_crawling import *


def reorder_queue(queue):
    """Function untuk reorder queue
    """
    value_backlink = []
    for u in queue:
        # menentukan nilai backlink_count
        backlink_count = 1
        # memasukan backlink_count ke array value_backlink
        value_backlink.append(backlink_count)

    # membuat dictionary backlink untuk proses sorting
    backlink_dictionary = dict(zip(queue, value_backlink))
    # sorting backlink_dictionary
    sort_orders = sorted(backlink_dictionary.items(),
                         key=lambda x: x[1], reverse=True)
    # mengkosongkan queue
    queue.clear()

    # membuat queue yang sudah di sort
    for i in sort_orders:
        queue.append(i[0])
        # melihat value backlink dari setiap url
        # print(i)

    return queue


# reorder url_queue dari crawl sebelumnya
reorder_queue(url_queue)

# membuat hot_queue
hot_queue = deque([])

# new start_time_MSB
start_time_MSB = time.time()


def jumlah_key_body(complete_text):
    """Function untuk menghitung jumlah key di text
    """
    keyword = "Barcelona"
    keyword2 = "Klub bola Barcelona"
    keyword3 = "klub bola Barcelona"
    jumlah_keyword = complete_text.count(
        keyword) + complete_text.count(keyword2) + complete_text.count(keyword3)
    # jumlah_keyword = complete_text.count(keyword)
    return jumlah_keyword


def jumlah_key_title(title):
    """Function untuk menghitung jumlah key di title
    """
    keyword = "Barcelona"
    keyword2 = "Klub bola Barcelona"
    keyword3 = "klub bola Barcelona"
    jumlah_keyword = title.count(
        keyword) + title.count(keyword2) + title.count(keyword3)
    # jumlah_keyword = title.count(keyword)
    return jumlah_keyword


def modified_crawl(url):
    """Function untuk modified crawling page.
    """
    try:
        # kondisi berhenti biar ga running all the time
        time_now = time.time() - start_time_MSB
        time_now_int = int(time_now)
        if time_now_int >= 120:
            return
        # if len(visited_url) >= 1800:
        #     return
        # kondisi berhenti dari algoritma
        if (len(hot_queue) == 0) and (len(url_queue) == 0):
            return

        # memasukan url kedalam visited_url
        visited_url.append(url)

        # crawl page
        print("page yang sedang di crawl:", url)
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

        # get meta description
        description = soup.find("meta",attrs={"name":"description"})
        if description is None:
            description = "-"
        else:
            description = description.get("content")

        # get meta keywords
        keywords = soup.find("meta",attrs={"name":"keywords"})
        if keywords is None:
            keywords = "-"
        else:
            keywords = keywords.get("content")

        # check HTML5
        html5 = "no"

        # check hot_url
        hot_url = False
        hot_link = "no"
        if (jumlah_key_body(complete_text) >= 10) or (jumlah_key_title(title) >= 1):
            hot_url = True
            hot_link = "yes"

        # Create a new record
        sql = "INSERT INTO `page_information` (`base_url`, `html5`, `title`, `description`, `keywords`, `content_text`, `hot_url`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # Execute the query
        cursor.execute(sql, (url, html5, title, description, keywords, complete_text, hot_link))
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
                if (j == complete_url):
                    flag = 1
                    break

            # Check if the URL already exists in the hot_queue
            for j in hot_queue:
                if (j == complete_url):
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
                    # kondisi yang dimasukan ke hot_queue dan url_queue
                    if (hot_url == True) or ((complete_url.count("klub-bola-barcelona") >= 1)):
                        hot_queue.append(complete_url)
                    else:
                        url_queue.append(complete_url)

        reorder_queue(hot_queue)
        reorder_queue(url_queue)

    except (AttributeError, KeyError):
        title = "no-title"
        complete_text = "no-text"

    # crawl url selanjutnya
    if len(hot_queue) > 0:
        current = hot_queue.popleft()
    else:
        current = url_queue.popleft()
    modified_crawl(current)


# karena sebelumnya hanya ada url_queue, jadi yang url ini yg dicrawl duluan
url = url_queue.popleft()
modified_crawl(url)

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
print("Jumlan url dalam hot queue:", len(hot_queue))
print("Waktu yang dibutuhkan: %s detik" % (time.time() - start_time))

# Close the connection
db.close()
