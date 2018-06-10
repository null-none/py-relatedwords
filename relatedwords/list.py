import requests

class ReplatedWords(object):

    def __init__(self, email, password):
        self.url = 'http://relatedwords.org/api/related'

    def query(self, word):
        result = requests.get('{0}?term={1}'.format(self.url, word))
        return result.json()

