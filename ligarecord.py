from lxml import html
import requests
import re
import json
from django.utils.encoding import smart_str, smart_unicode
#if you want to know why this is here check this
#http://www.saltycrane.com/blog/2008/11/python-unicodeencodeerror-ascii-codec-cant-encode-character/


class LigaRecord(object):

    def __init__(self):
        self=self

    def getTree(self):
        page = requests.get('http://liga.record.xl.pt/info/rankings.aspx')
        p = re.compile('(?<=playerArr =)(.*)(?=;)')
        #find all instances of regular expression in pageData
        parsed = p.findall(page.text)
        text = smart_str(parsed[0].split(';')[0])

        #load as JSON instead of using evaluate to prevent risky execution of unknown code
        player_json = json.loads(text)
        for i in player_json:
            print i['Name']
            print i['PointsTotal']
