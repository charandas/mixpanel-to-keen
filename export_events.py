# -- coding: utf-8 --

import os
import urllib2
import simplejson as json
import keen

from lib.mixpanel import Mixpanel
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api = Mixpanel(
    api_key = os.environ.get('MIXPANEL_API_KEY'),
    api_secret = os.environ.get('MIXPANEL_API_SECRET'),
)
lines = api.request(['export'], {
    'from_date': '2015-08-01',
    'to_date': '2015-08-7',
    'event' : ['ad-click'],
    'where': 'properties["network"] == "chi"'
})

for line in lines:
    properties = json.loads(line)
    print(properties)
    keen.add_event('core', properties)
