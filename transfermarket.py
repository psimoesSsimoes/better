from lxml import html
import requests
import urllib



class Transfer_market(object):

    def __init__(self,home_name,away_name):
        self.home_name=home_name
        self.away_name=away_name

    def getTeamMainPageUrl(self,team_name):
        parameters = team_name.replace(' ', '+')
        print (parameters)
        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.com'  # This is another valid field
        }

        page = requests.get("http://www.transfermarkt.co.uk", headers=headers)
        print (page.content)


# result.info() will contain the HTTP headers

# To get say the content-length header
