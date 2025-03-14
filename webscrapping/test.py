import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

print(sopa.select('title'))

for i in sopa.select('a'):
    print(i.get('href'))

for i in sopa.select('.r-snippetized'): # <-- el punto permite traer los elementos que tengan la clase "r-sniooetized"
    print(i.getText())

# obtener imagenes
""" n = 1
for i in sopa.select('img'):
    print(i.get('src'))    
    imagen = requests.get(i.get('src'))
    with open(f'imagen{n}.jpg', 'wb') as f: # <-- wb es para escribir en binario
        f.write(imagen.content)
    n += 1 """

# usar toscrape.com sandbox para scrapping:
# traer los titulos de los libros que tengan 5 estrallas.
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

for i in range(1, 51):
    resultado = requests.get(url_base.format(i))
    sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')
    for i in sopa.select('.star-rating.Five'):
        print(i.parent.select('h3')[0].getText())

print("-" * 50)
# otro metodo
titulos_ratingalto = []
for i in range(1, 51):
    resultado = requests.get(url_base.format(i))
    sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')
    for pod in sopa.select(".product_pod"):
        if len(pod.select('.star-rating.Four')) != 0 or len(pod.select('.star-rating.Five'))  != 0:
            titulos_ratingalto.append(pod.select('h3')[0].getText())

for titulo in titulos_ratingalto:
    print(titulo)