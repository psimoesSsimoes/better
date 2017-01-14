from lxml import html
import requests

class forebetfootball_game:
   'Common base class for all games in forebet'


   def __init__(self, url):
      self.url = url

   def displayUrl(self):
     print self.url
