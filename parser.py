import requests
from bs4 import BeautifulSoup
import lxml

URL_BASE = 'https://www.silverroom.ru'
URL_SEARCH = 'https://www.silverroom.ru/search'
URL_PHOTOS = 'https://www.silverroom.ru/photos/2'
url_test = 'https://www.silverroom.ru/photos/2/295848/1.jpg'


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    print(r.status_code)
    return r.text


def get_file(url):
    r = requests.get(url, stream=True)
    return r


def save_data(name, file_data):
    file = open(name, 'bw')
    for chunk in file_data.iter_content(4096):
        file.write(chunk)


def check_lot(lot):
    url = f'{URL_PHOTOS}/{lot}/1.jpg'
    file = get_file(url)
    print(file.status_code)
    if (file.status_code == 200):
        print(f'{lot} - ok')
        save_data(f'{lot}', file)
    else:
        print(f'{lot}   NOT FOUND   !!!!!')

# save_data('2', get_file('https://www.silverroom.ru/photos/2/215556/1.jpg'))
check_lot(209305)
check_lot(215556)
