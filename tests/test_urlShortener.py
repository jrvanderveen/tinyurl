import unittest
from urlShortener.urlShortener import UrlShortener


class TestUrlShortener(unittest.TestCase):

    def setUp(self):
        self.urlShortener = UrlShortener()

    def test_encodeUrl(self):
        url1 = "https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927"
        url2 = "https://www.t-mobile.com/cell-phone/samsung-galaxy-note11-plus-5g?sku=610214662927"
        encoded = self.urlShortener.encodeUrl(url1)
        urlId = encoded.split("/")[-1]
        # Ensure url id  is length 6
        self.assertEqual(len(urlId), self.urlShortener.urlIdLength)
        # Ensure same url give us the same result
        self.assertEqual(self.urlShortener.encodeUrl(url1), encoded)
        # Ensure different urls give different results
        self.assertNotEqual(self.urlShortener.encodeUrl(
            url1), self.urlShortener.encodeUrl(url2))

    def test_decodeUrl(self):
        # Encode urls and ensure we can properly decode them
        url1 = "https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927"
        url2 = "https://www.t-mobile.com/cell-phone/samsung-galaxy-note11-plus-5g?sku=610214662927"
        encoded1 = self.urlShortener.encodeUrl(url1)
        encoded2 = self.urlShortener.encodeUrl(url2)
        self.assertEqual(url1, self.urlShortener.decodeUrl(encoded1))
        self.assertEqual(url2, self.urlShortener.decodeUrl(encoded2))
        # ensure error handeling and non encoded urls return None
        self.assertEqual(None, self.urlShortener.decodeUrl(
            "https://www.dropbox.com/scl/fi/5ayblyqlttzhjvjps23wk/URL-Shortener"))
        self.assertEqual(None, self.urlShortener.decodeUrl("www.dropbox.com/"))
        self.assertEqual(None, self.urlShortener.decodeUrl(""))

    def test_getHitCountForShortenedUrl(self):
        UrlShortener.url2Long = dict()
        UrlShortener.url2Short = dict()
        # Encode hit count for returning longurls is correct
        url1 = "https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927"
        encoded1 = self.urlShortener.encodeUrl(url1)
        # No decodes yet
        self.assertEqual(
            self.urlShortener.getHitCountForShortenedUrl(encoded1), 0)
        # Decode url1 twice
        self.urlShortener.decodeUrl(encoded1)
        self.urlShortener.decodeUrl(encoded1)
        # Hit count should be 2 for url1
        self.assertEqual(
            self.urlShortener.getHitCountForShortenedUrl(encoded1), 2)

        # ensure error handeling and non encoded urls return 0
        self.assertEqual(0, self.urlShortener.getHitCountForShortenedUrl(
            "https://www.dropbox.com/scl/fi/5ayblyqlttzhjvjps23wk/URL-Shortener"))
        self.assertEqual(
            0, self.urlShortener.getHitCountForShortenedUrl("www.dropbox.com/"))
        self.assertEqual(0, self.urlShortener.getHitCountForShortenedUrl(""))

    def test_encodeUrlCustom(self):
        UrlShortener.url2Long = dict()
        UrlShortener.url2Short = dict()
        url1 = "https://www.t-mobile.com/cell-phone/samsung-galaxy-note10-plus-5g?sku=610214662927"
        customId = "test_id"
        encoded = self.urlShortener.encodeUrlCustom(url1, customId)
        urlId = encoded.split("/")[-1]
        # Ensure url id  is length 6
        self.assertEqual(customId, urlId)

