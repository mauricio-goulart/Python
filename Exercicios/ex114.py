import urllib.request
import urllib


try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('deu ruim')
else:
    print('Deu bom')