from lxml import html
import requests
from forefootball_game import forebetfootball_game_url
'''
read page source
'''
page = requests.get('http://www.forebet.com/en/football-tips-and-predictions-for-today')
tree = html.fromstring(page.content)
'''
retrive all href for today's games
'''
href_today_games = [match for match in tree.xpath('//td[1]/a[1]/@href') if '/en/predictions' in match]
''' array containing gameurl objects'''
obj=[]

'''loop all href'''
for url in href_today_games:
    '''create object with url'''
    game = forebetfootball_game_url("http://www.forebet.com/"+url)
    ''' call methods of the class'''
    game.standings()
    obj.append(game)

for elem in obj:
    elem.displayUrl()
'''buyers = tree.xpath('//div[@title="buyer-name"]/text()')'''
