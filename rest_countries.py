#! python3
# rest_countries.py is a utility for pulling geographic data from an API

REST_EU_ROOT_URL = "https://restcountries.eu/rest/v2"

def REST_country_request(field='all', name=None, params=None):
    headers={'User-Agent': 'Mozilla/5.0'}

    if not params:
        params = {}

    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')

    url = '%s/%s/%s'%(REST_EU_ROOT_URL, field, name)
    print('Requesting URL: ' + url)

    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception('Request failed with status code ' + str(response.status_code))

    return response