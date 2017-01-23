from lxml import html
import requests
import urllib



class Transfer_market(object):

    list_formations = ['4-3-3','4-4-2','5-4-1','3-1-4-2','4-4-1-1','4-5-1','4-1-2-1-2','5-3-2','4-2-3-1','4-3-2-1','3-4-3','3-3-1-3','3-4-2-1','3-6-1','1-4-3-2','4-2-4']

    def __init__(self,home_name,away_name):
        self.home_name=home_name
        self.away_name=away_name

    def getTeamMainPageTree(self,team_name):
        parameters = team_name.replace(' ', '+')
        url = "http://www.transfermarkt.co.uk/schnellsuche/ergebnis/schnellsuche?query="+parameters+"&x=0&y=0"
        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.com'  # This is another valid field
        }

        page = requests.get(url, headers=headers)
        #print (page.content)
        tree = html.fromstring(page.text)
        allhref = tree.xpath('//*[@id]/@href')
        url = "http://www.transfermarkt.co.uk/"+allhref[7]
        page = requests.get(url, headers=headers)
        tree = html.fromstring(page.text)
        return tree

    def extract_team(self,team_name):
        tree = self.getTeamMainPageTree(team_name)
        self.extract_formation(tree)
        print (tree.xpath('/html/body/div[5]/div[10]/div[1]/div[2]/div[5]/div[2]/div/div[2]/span/a/text()'))

    def extract_formation(self,tree):
        # formation will be a list with only one string
        formation = tree.xpath('//*[@id="main"]/div[10]/div[1]/div[2]/div[4]/div[1]/text()')
        for i in self.list_formations:
            if i in formation[0]:
                print (i)









# result.info() will contain the HTTP headers

# To get say the content-length header
