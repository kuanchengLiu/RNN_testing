# -*- coding: UTF-8 -*-

import urllib.request

RESPONSE_URL = urllib.request.urlopen('https://www.python.org')

print(RESPONSE_URL.status)

print(RESPONSE_URL.getheaders())

print(RESPONSE_URL.getheader('Server'))
