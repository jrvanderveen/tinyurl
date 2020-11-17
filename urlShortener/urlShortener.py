
'''

1. Shorten a URL
    - When the user provides a URL, shorten it using a generated unique identifier.
    For example, given the URL `https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927`,
    a value similar to `http://localhost/abc123` might be returned.

1.b. No Duplicates
    - If a URL has already been shortened, do not generate a new shortened URL (return the previous value)


3. Hit Counter
    - Track the number of times a shortened URL has been accessed


4. Custom URLs
    - The user should have an option to set a desired URL (e.g. http://localhost/custom-value) rather than an assigned ID.
'''
import string
from random import randint


class UrlShortener():
    letters = string.ascii_letters + string.digits
    url2Long = dict()
    url2Short = dict()
    urlIdLength = 6
    prefix = "http://localhost/"
    urlCount = "counter"
    urlVal = "longUrl"
    CUSTOM_ID_PRESENT = 1
    CUSTOM_ID_MIS_MATCH = 2

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
                        UrlShortener.urlVal: longUrl, UrlShortener.urlCount: 0}
                    UrlShortener.url2Short[longUrl] = shortId
                    break
        return UrlShortener.prefix + UrlShortener.url2Short[longUrl]

    def encodeUrlCustom(self, longUrl, customId):
        if customId in UrlShortener.url2Long:
            return UrlShortener.CUSTOM_ID_PRESENT

        if longUrl in UrlShortener.url2Short:
            if customId in UrlShortener.url2Long and UrlShortener.url2Long[customId] != longUrl:
                return UrlShortener.CUSTOM_ID_MIS_MATCH
            else:
                return UrlShortener.prefix + UrlShortener.url2Short[longUrl]

        UrlShortener.url2Long[customId] = {
            UrlShortener.urlVal: longUrl, UrlShortener.urlCount: 0}
        UrlShortener.url2Short[longUrl] = customId
        return UrlShortener.prefix + UrlShortener.url2Short[longUrl]

    def decodeUrl(self, shortUrl):
        # ensure we get an id
        try:
            urlId = shortUrl.split("/")[-1]
        except ValueError:
            return None
        # if the id has a long url return it other wise none
        if urlId in UrlShortener.url2Long:
            UrlShortener.url2Long[urlId][UrlShortener.urlCount] += 1
            return UrlShortener.url2Long[urlId][UrlShortener.urlVal]
        else:
            return None

    def getHitCountForShortenedUrl(self, shortUrl):
        try:
            urlId = shortUrl.split("/")[-1]
        except ValueError:
            return 0
        # if the id has a long url return it other wise none
        if urlId in UrlShortener.url2Long:
            return UrlShortener.url2Long[urlId][UrlShortener.urlCount]
        else:
            return 0
