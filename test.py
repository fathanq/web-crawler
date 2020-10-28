from collections import deque, Counter
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


kalimat = "muhammad fathan qoriiba dimana fathan dan fathan qoriiba tidak sama qoriiba dan fathan fathan qoriiba"
kata = "fathan qoriiba"
hasil = kalimat.count(kata)
print(hasil)
