from lxml import html
import requests


class Transfer_market(object):

    def __init__(self,home_name,away_name):
        self.home_name=home_name
        self.away_name=away_name

    def getTeamMainPageUrl(self,team_name):
        page = requests.get('http://www.transfermarkt.co.uk/schnellsuche/ergebnis/schnellsuche?query='+team_name)
        tree = html.fromstring(page.content)
        print (tree.xpath('/html/body/div[4]/div[8]/div/div/div[2]/div/table/tr[1]/td[2]/table/tr[1]/td/a/text()'))
        mainUrl = tree.xpath('/html/body/div[4]/div[8]/div/div/div[2]/div/table/tr[1]/td[2]/table/tr[1]/td/a/@href')
'''
find the home and away team url
'''
