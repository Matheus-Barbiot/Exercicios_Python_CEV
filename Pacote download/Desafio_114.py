import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.youtube.com')
except:
    print('Nãoe stá no ar no momento.')
else:
    print('o site está acessível ')
    print(site.read())