from lxml import html
import requests
import urllib



class Transfer_market(object):

    def __init__(self,home_name,away_name):
        self.home_name=home_name
        self.away_name=away_name

    def getTeamMainPageUrl(self,team_name):
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
        '''
         
        '''
        print (allhref[7])

        mainUrl = tree.xpath('/html/body/div[4]/div[8]/div/div/div[2]/div/table/tr[1]/td[2]/table/tr[1]/td/a/@href')


# result.info() will contain the HTTP headers

# To get say the content-length header
