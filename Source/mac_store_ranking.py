#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import json
import datetime

from genres import mac
from util import countries

store_server = str("itunes.apple.com")

# Your App ID. Located at iTunesConnect.
AppID = str("APP-ID-HERE")
# Your App Category inside Mac App Store
genre = mac.MacAppStoreGenre.Productivity
# Stores
store_countries = countries.AppleWorld

# Procesamos los paises

# Select all countries availables (True)
store_countries = filter(lambda country: country[0] == True, store_countries)
# Sorted by country name
store_countries.sort(key=lambda country: country[2])

"""
Top free Mac app ranking
"""
def ranking_free(iso_code):
    store_uri = str("/" + iso_code + "/rss/topfreemacapps/limit=200/genre=" + str(genre.value) + "/json")

    return request_url(store_uri)

"""
Top paid Mac applications
"""
def ranking_paid(iso_code):
    store_uri = str("/" + iso_code + "/rss/toppaidmacapps/limit=200/genre=" + str(genre.value) + "/json")

    return request_url(store_uri)

"""
Top grossing Mac applications
"""
def ranking_grossing(iso_code):
    store_uri = str("/" + iso_code + "/rss/topgrossingmacapps/limit=200/genre=" + str(genre.value) + "/json")
    
    return request_url(store_uri)

"""
Request an URL
"""
def request_url(url):
    conn = httplib.HTTPSConnection(store_server)
    conn.request("GET", url)
    r1 = conn.getresponse()

    data1 = r1.read()

    ranking = json.loads(data1)

    conn.close()

    # JSON document
    posicion = process_result(ranking)

    return posicion

"""
Process JSON and recover results
"""
def process_result(result):
    entries = result["feed"]["entry"]

    for idx, entry in enumerate(entries):
        app_id = entry["id"]["attributes"]["im:id"]

        if app_id == AppID:
            return str(idx + 1)

    return "---"

#
# Workflow.
#

print("\r\n\t{0:^50}\r\n".format("Mac App Store. Ranking"))
print("\t{0:20}{1:>10}{2:>10}{3:>10}\r\n".format("Country", "Free", "Paid", "Grossing"))

for country in store_countries:
    posicion_free = ranking_free(country[1])
    posicion_paid = ranking_paid(country[1])
    posicion_grossing = ranking_grossing(country[1])

    print("\t{0:20.17}{1:>10}{2:>10}{3:>10}".format(country[2], posicion_free, posicion_paid, posicion_grossing))

print("\r\n\t{0:^50}".format("A script by @fitomad."))
print("\t{0:^50}\r\n".format("GitHub: https://github.com/fitomad/App-Store-Ranking"))
