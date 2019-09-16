
import urllib.request

RESPONSE_URL = urllib.request.urlopen('https://www.python.org')

print(type(RESPONSE_URL))
