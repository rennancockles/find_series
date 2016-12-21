#! /usr/bin/python -B
# -*- coding: utf-8 -*-

import json
import requests
from lxml import html


r = requests.get('https://api.tvshowtime.com/v1/to_watch', auth=('USERNAME', 'PASSWORD'))
parsed = json.loads(r.text)

for episode in parsed['episodes']:
    episodio = "S%02dE%02d" % (episode['season_number'],episode['number'])
    mais_episodios = episode['show']['aired_episodes'] - episode['show']['seen_episodes'] - 1
    print "{} {} +{}".format(episode['show']['name'], episodio, mais_episodios)

    r = requests.get('https://thepiratebay.org/search/%s/0/99/0' % episode['show']['name'])
    tree = html.fromstring(r.content)
    magnet = tree.xpath('//*[contains(@title,"%s")]/../following-sibling::a[1]/@href' % episodio)
    if len(magnet) > 0: print magnet[0]
    print

