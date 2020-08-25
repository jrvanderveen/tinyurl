
'''

1. Shorten a URL
    - When the user provides a URL, shorten it using a generated unique identifier. 
    For example, given the URL `https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927`, 
    a value similar to `http://localhost/abc123` might be returned.

'''
import string
from random import randint


class UrlShortener():
    letters = string.ascii_letters + string.digits
    url2Long = dict()
    url2Short = dict()
    urlIdLength = 6
    prefix = "http://localhost/"

    # https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927 -> http://localhost/abc123

    def encodeUrl(self, longUrl):
        # reutn shortened url
        if longUrl not in UrlShortener.url2Short:
            while True:
                shortId = ""
                for _ in range(UrlShortener.urlIdLength):
                    shortId = shortId + UrlShortener.letters[randint(0, 61)]

                if shortId not in UrlShortener.url2Long:
                    UrlShortener.url2Long[shortId] = {
                        "longUrl": longUrl, "counter": 0}
                    UrlShortener.url2Short[longUrl] = shortId
                    break
        # print(UrlShortener.prefix + UrlShortener.url2Short[longUrl])
        return UrlShortener.prefix + UrlShortener.url2Short[longUrl]

    def decodeUrl(self, shortUrl):
        # reutrn the full url
        pass
