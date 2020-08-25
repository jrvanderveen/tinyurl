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
