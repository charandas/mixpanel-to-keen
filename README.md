# mixpanel-to-keen

Export events out of mixpanel to keen.io

## dotenv file

Have the following variables be defined in your root `.env` file:

```
MIXPANEL_API_KEY="your-key"
MIXPANEL_API_SECRET="your-secret"
KEEN_PROJECT_ID="your-project-id"
KEEN_WRITE_KEY="your-write-key"
KEEN_READ_KEY="your-read-key"
KEEN_MASTER_KEY="your-master-key"
```

## Other Requirements

1. Have python 2.7.10 installed. A setup with `pyenv` and `virtualenv` is recommended.
2. `pip install` to get all the dependencies listed in `requirements.txt`.
3. `python export-events.py`

## Mixpanel Client Library included under `./lib`

This is just [downloaded](https://mixpanel.com/site_media/api/v2/mixpanel.py) 
off of mixpanel's site. This client library doesn't do much
except serializing the arguments to its `request` method and do REST calls to
their API.

I modified the `API_ENDPOINT` in it to use `https://data.mixpanel.com`, so you can actually get access the export API (not accessible through the usual `http://mixpanel.com`). Otherwise, the other endpoint provides access to all the endpoints but the `export` one.
