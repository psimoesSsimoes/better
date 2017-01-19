from lxml import html
import requests
from arr_utils import arr_utils
from game_analisys import game_Analisys
from transfermarket import Transfer_market

class forebetfootball_game_url:
   'Common base class for all games in forebet'


   def __init__(self, url):
      self.url = url
      self.analisys = game_Analisys()
      self.transfermarkt = None
      page = requests.get(self.url)
      self.tree = html.fromstring(page.content)



   def standings(self):
       #print (self.tree.xpath('//*[contains(@style,"#FFD463")]/td/text()'))
       try:
           standings_table_arr =  [self.tree.xpath('//*[contains(@style,"#FFD463")]/td/text()')[i] for i in (17,26)] #in position 0 and 8 are the standings positions of each team
           names_standings = [j for i in zip(self.tree.xpath('//*[contains(@style,"#FFD463")]/td/a/text()'),standings_table_arr) for j in i] #merge two list into a single list
           self.analisys.set_teams_points(names_standings)
           return True

       except IndexError:
           print ("Competition hasn't started so there are no standings")
           return False



   def team_names(self):
       arr_names = (self.tree.xpath('//center/h1/a/text()'))
       arr_manipulator = arr_utils(arr_names)
       self.analisys.set_team_names(arr_manipulator.index_based_extract(0),arr_manipulator.index_based_extract(1))
       self.transfermarkt= Transfer_market(arr_manipulator.index_based_extract(0),arr_manipulator.index_based_extract(1))
   '''
    One of this xpaths will be empty. Sum up the lists will always give us the wanted percentages
   '''
   def last_6_matches(self):
       percentages_home = self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[3]/td[1]/div/table/tr[5]/td/text()") + self.tree.xpath ("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[3]/td[1]/div/table/tr[9]/td/text()")
       percentages_away = self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[3]/td[2]/div/table/tr[8]/td/text()") + self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[3]/td[2]/div/table/tr[5]/td/text()")
       if '%' not in percentages_away[0]:
           percentages_away = self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[3]/td[2]/div/table/tr[9]/td/text()")
       self.analisys.last_6_matches_percentage_home__team(percentages_home)
       self.analisys.last_6_matches_percentage_away__team(percentages_away)

   def last_matches_home(self):
       percentages_home = self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[4]/td[1]/div/table/tr[3]/td/text()")
       self.analisys.latest_home_matches(percentages_home)

   def last_matches_away(self):
       percentages_away = self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[4]/td[2]/div/table/tr[3]/td/text()")
       self.analisys.latest_away_matches(percentages_away)

   def overall_statistics(self):
       page_info = self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[5]/td[1]/div/table/tr[2]/td[1]/table/tr/td[2]/text()")
       overall_home = page_info[:2]
       overall_home+=[x for x in page_info[2:] if '%' in x]
       self.analisys.overall_stats_home(overall_home)
       page_info = self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[5]/td[1]/div/table/tr[2]/td[2]/table/tr/td[2]/text()")
       overall_away = page_info[:2]
       overall_away+=[x for x in page_info[2:] if '%' in x]
       self.analisys.overall_stats_away(overall_away)
       #overall_away = self.tree.xpath("")

   def head_to_head(self):
       self.analisys.vs(self.tree.xpath("/html/body/div[3]/table/tr[4]/td/table/tr[1]/td[2]/table/tr/td[2]/div/table[9]/tr[1]/td[2]/div/table/tr[3]/td/text()"))

   def displayTeamsStats(self):
       self.analisys.print_team_stats()

   def head_to_head_by_position(self):
       self.transfermarkt.getTeamMainPageUrl("Fc Porto")

   def displayUrl(self):
     print (self.url)
