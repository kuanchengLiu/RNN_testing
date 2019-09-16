
import urllib.request

RESPONSE_URL = urllib.request.urlopen('https://www.python.org')
print(RESPONSE_URL.read().decode('utf-8'))
