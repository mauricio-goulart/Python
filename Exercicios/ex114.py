import urllib.request
import urllib


try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('Deu ruim')
else:
    print('Deu bom')