__author__ = 'OliPicard'
import requests
import sys



site_one = input('url:')
try:
    r = requests.get('{}'.format(site_one))
    ox = r.status_code
    if ox == 200:
        print('Site is alive!')

    if ox == 403:
        print('Its dead jim!')

    if ox == 404:

        print('Whoops, That page cannot be found! (404)')

    if ox == 503:
        print('Someone forgot to turn off the stargate. (Gateway Error)')

except requests.exceptions.RequestException as e:
    print(e)











