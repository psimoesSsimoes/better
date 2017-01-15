from lxml import html
import requests
from arr_utils import arr_utils

class forebetfootball_game_url:
   'Common base class for all games in forebet'
   

   def __init__(self, url):
      self.url = url

   def html_from_string(self):
     page = requests.get(self.url)
     tree = html.fromstring(page.content)
     return tree

   def standings(self):
       standings_table_arr = self.html_from_string().xpath('//*[contains(@style,"#FFD463")]/td/text()')
       arr_manipulator = arr_utils(standings_table_arr)


   def displayUrl(self):
     print self.url
