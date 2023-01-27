import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

pagina = requests.get('https://www.google.com/search?q=dolar&oq=dolar&aqs=edge.0.69i59j69i57j69i59l2.687j0j1&sourceid=chrome&ie=UTF-8',headers=headers)

soup = BeautifulSoup(pagina.content, 'html.parser')

atributos = {'class':'DFlfde SwHCTb'}


dolar = soup.find_all('span', attrs=atributos)[0]



print(f'{"Casa de Câmbio":=^30}')
print(f'Dolar:$[{dolar["data-value"]}]')
print(30 * '=')






