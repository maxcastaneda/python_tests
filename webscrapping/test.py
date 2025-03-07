import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

print(resultado.text)
sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')
print(sopa.select('title'))
