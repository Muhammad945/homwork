"""import bs4
import requests

url = ''
x = requests.get(url).text
soup = bs4.BeautifulSoup(x, 'lxml')

smileys = {}

for i in soup.find_all('a'):
    symbol=i.get('data-symbol')
    title = i.get('title')
    if symbol and title:
        smileys[title.lower()]=symbol

word = input('input word: ')
print(smileys.get(word))"""

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😞"
}
output= ""
for word in words:
    output+= emojis.get(word, word)+ " "
print(output)
