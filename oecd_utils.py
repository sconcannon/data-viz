#! python3
# oecd_utils.py contains functions useful for querying the OECD API
# API docs at https://data.oecd.org/api/sdmx-json-documentation/

import requests
OECD_ROOT_URL = 'http://stats.oecd.org/sdmx-json/data'

def make_OECD_request(dsname, dimensions, params=None, root_dir=OECD_ROOT_URL):
    """ Make a URL for the OECD API and return a response """

    if not params:
        params = {}

    dim_args = ['+'.join(d) for d in dimensions]
    dim_str = '.'.join(dim_args)

    url = root_dir + '/' + dsname + '/' + dim_str + '/all'
    print('Requesting URL: ' + url)
    return requests.get(url, params=params)
