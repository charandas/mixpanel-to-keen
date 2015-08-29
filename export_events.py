# -- coding: utf-8 --

import os
import urllib2

from lib.mixpanel import Mixpanel
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api = Mixpanel(
    api_key = os.environ.get('MIXPANEL_API_KEY'),
    api_secret = os.environ.get('MIXPANEL_API_SECRET'),
)
data = api.request(['export'], {
	'from_date': '2015-08-22',
	'to_date': '2015-08-26',
    'event' : ['ad-click'],
    'where': urllib2.quote('properties["network"] == "nyc"')
})

