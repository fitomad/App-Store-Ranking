#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import httplib
import datetime
import argparse

from genres import mac
from util import countries

store_server = str("itunes.apple.com")

"""
Top free Mac app ranking
"""
def ranking_free(iso_code):
    store_uri = "/WebObjects/MZStoreServices.woa/ws/charts?cc={0}&g={1}&name=FreeMacApps&limit=400".format(iso_code, str(genre.value))

    return request_url(store_uri)

"""
Top paid Mac applications
"""
def ranking_paid(iso_code):
    store_uri = "/WebObjects/MZStoreServices.woa/ws/charts?cc={0}&g={1}&name=PaidMacApps&limit=400".format(iso_code, str(genre.value))
    return request_url(store_uri)

"""
Top grossing Mac applications
"""
def ranking_grossing(iso_code):
    store_uri = "/WebObjects/MZStoreServices.woa/ws/charts?cc={0}&g={1}&name=MacAppsByRevenue&limit=400".format(iso_code, str(genre.value))
    
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
    entries = result["resultIds"]

    try:
        position = entries.index(AppID)
        return (position + 1)
    except ValueError:
        return "---"

"""
Print help information
"""
def print_parameters():
    print("\r\n\t{0:^26}\r\n".format("Mac App Store Categories"))

    for genre in mac.MacAppStoreGenre:
        print("\t{0:^20} = {1:<6}".format(genre.name, genre.value))

    
    print("\r\n\t{0:^26}\r\n".format("Countries availables"))
    print("\t{0:^20} = {1:<6}".format("All countries", "world"))
    print("\t{0:^20} = {1:<6}\r\n".format("Top 10 (by revenue)", "top"))

    print("\tExample: macr.py -appid 123456789 -category 12014 -stores top\r\n")
    
#
# Workflow.
#

# Command line argument parser
parser = argparse.ArgumentParser(description='Mac App Store Ranking.')

parser.add_argument('-appid', type=int, help='iTunesConnect application identifier.')
parser.add_argument('-stores', type=str, help='App Store country sets.')
parser.add_argument('-category', type=int, help='App category inside Mac App Store.')
parser.add_argument('-p', '--parameters', action="store_true", help='List all posible values for Stores and Category.')

args = parser.parse_args()

if args.parameters:
    print_parameters()
    sys.exit()

# Mac App Store Countries

store_countries = None

if args.stores == "world":
    store_countries = countries.AppleWorld
elif args.stores == "top":
    store_countries = countries.TopMarkets
else:
    print_parameters()
    print("\tMarket not available. Take a look above.")

    sys.exit()

# Select all countries availables (True)
store_countries = filter(lambda country: country[0] == True, store_countries)
# Sorted by country name
store_countries.sort(key=lambda country: country[2])

# App category
try:
    genre = mac.MacAppStoreGenre(args.category)
except ValueError:
    print_parameters()
    print("\tCategory not available. Take a look at category section above.\r\n")

    sys.exit()

# App ID. Located at iTunesConnect.

AppID = args.appid

print("\r\n\t{0:^50}\r\n".format("Mac App Store. Ranking"))
print("\t{0:20}{1:>10}{2:>10}{3:>10}\r\n".format("Country", "Free", "Paid", "Grossing"))

for country in store_countries:
    posicion_free = ranking_free(country[1])
    posicion_paid = ranking_paid(country[1])
    posicion_grossing = ranking_grossing(country[1])

    print("\t{0:20.17}{1:>10}{2:>10}{3:>10}".format(country[2], posicion_free, posicion_paid, posicion_grossing))

print("\r\n\t{0:^50}".format("A script by @fitomad."))
print("\t{0:^50}\r\n".format("GitHub: https://github.com/fitomad/App-Store-Ranking"))