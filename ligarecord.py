from lxml import html
import requests

class LigaRecord(object):

    def __init__(self):

    def getTree(self):
        page = requests.get('http://www.forebet.com/en/football-tips-and-predictions-for-today')
        tree = html.fromstring(page.content)
