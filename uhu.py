'''import urllib.request

opener = urllib.request.build_opener()
response = opener.open('https://httpbin.org/get')

print(response.read())

import requests
response = requests.get('https://httpbin.org/get')

print(response.content)'''

'''import urllib.request

opener = urllib.request.build_opener()
response = opener.open('https://httpbin.org/')

print(response.read())

import requests
response = requests.get('https://httpbin.org/')

print(response.content)'''

'''import requests
responce = requests.get('https://httpbin.org/get')

print(responce.text)
print(f'Datatype - {type(responce.text)}')'''

'''import requests
responce = requests.post('https://httpbin.org/post', data='Test data', headers={'hi':'Test title'})

print(responce.text)'''

'''import requests
responce = requests.post('https://httpbin.org/post', data={'test form':'me_form'})

print(responce.text)'''

'''import requests
res_parse_list=[]

responce = requests.get('https://coinmarketcap.com/')
responce_text = responce.text
responce_parse = responce_text.split('<span>')
for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith('$'):
        for parse_elem_2 in parse_elem_1.split('</span>'):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)


bitcoin_exchage_rate = res_parse_list[0]
print(bitcoin_exchage_rate)
ethereum_exchage_rate = res_parse_list[1]
print(ethereum_exchage_rate)
tether_exchage_rate = res_parse_list[2]
print(tether_exchage_rate)'''


from bs4 import BeautifulSoup
import requests

response=requests.get('https://coinmarketcap.com/')

if response.status_code==200:
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/bitcoin/markets/'})
    soup_list1 = soup.find_all('a', {'href':'/currencies/ethereum/markets/'})
    # for elem in soup_list:
    #     print(elem)
    res = soup_list[0].find('span')
    res = soup_list1[1].find('span')
    print(res.text)
