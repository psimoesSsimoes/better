from lxml import html
import requests
from arr_utils import arr_utils
from game_analisys import game_Analisys
class forebetfootball_game_url:
   'Common base class for all games in forebet'


   def __init__(self, url):
      self.url = url
      self.analisys = game_Analisys()
      page = requests.get(self.url)
      self.tree = html.fromstring(page.content)



   def standings(self):
       #print (self.tree.xpath('//*[contains(@style,"#FFD463")]/td/text()'))
       standings_table_arr =  [self.tree.xpath('//*[contains(@style,"#FFD463")]/td/text()')[i] for i in (17,26)] #in position 0 and 8 are the standings positions of each team
       names_standings = [j for i in zip(self.tree.xpath('//*[contains(@style,"#FFD463")]/td/a/text()'),standings_table_arr) for j in i] #merge two list into a single list
       self.analisys.set_teams_points(names_standings)
       self.analisys.print_team_stats()

   def team_names(self):
       arr_names = (self.tree.xpath('//center/h1/a/text()'))
       arr_manipulator = arr_utils(arr_names)
       self.analisys.set_team_names(arr_manipulator.index_based_extract(0),arr_manipulator.index_based_extract(1))

   def displayUrl(self):
     print (self.url)
