# -- coding: utf-8 --

import os
import urllib2
import simplejson as json
import keen

from lib.mixpanel import Mixpanel
from os.path import join, dirname
from dotenv import load_dotenv

from datetime import date

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

# print(lines)

for line in lines:
    metadata = json.loads(line)
        
    properties = { key: metadata['properties'][key] \
        for key, value in metadata['properties'].iteritems() \
        if not key.startswith('$')}

    timestamp = properties['time']    
    properties['keen'] = {}
    properties['keen']['timestamp'] = date.fromtimestamp(timestamp).isoformat()

    properties['event'] = metadata['event']

    keen.add_event('core', properties)
