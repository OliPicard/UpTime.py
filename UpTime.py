__author__ = 'OliPicard'
import requests
import requests.exceptions


print("-" * 25)
print("Welcome to UpTime.py, A simple uptime checker for http/https connections. developed by OliPicard - github.com/olipicard\n Once you have entered a URL press enter")
print("-" * 25)



site_one = input('Enter a URL:(including HTTP:// || HTTPS://)')

try:
    r = requests.get('{}'.format(site_one))
    ox = r.status_code
    r.raise_for_status()
    if ox == 200:
        input('Site is alive!')

    if ox == 403:
        input('Its dead jim!')

    if ox == 404:

        input('Whoops, That page cannot be found! (404)')

    if ox == 503:
        input('Someone forgot to turn off the stargate. (Gateway Error)')
except requests.exceptions.MissingSchema as site_one:
    print("Please re-run the program and enter in HTTP or HTTPs.")
except requests.exceptions.Timeout:
    input('Oh dear, it seems the site is timing out. Have you considered checking the DNS?')
except requests.exceptions.RequestException as site_one:
    input(site_one)

