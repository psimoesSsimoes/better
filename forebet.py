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
    '''
        the order needs to be the following: names, standings,
    '''
    game.team_names()
    if(game.standings()):
        game.head_to_head()
        game.last_6_matches()
        game.last_matches_home()
        game.last_matches_away()
        game.overall_statistics()
        game.displayTeamsStats()
    obj.append(game)

for elem in obj:
    elem.displayUrl()
'''buyers = tree.xpath('//div[@title="buyer-name"]/text()')'''
