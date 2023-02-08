#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import http.client
import datetime
import argparse

from genres import mac
from util import countries

store_server = str("itunes.apple.com")

def make_store_uri(country_code: str, genre: str, section: str) -> str:
    store_uri = f"/WebObjects/MZStoreServices.woa/ws/charts?cc={country_code}&g={genre}&name={section}}&limit=400"

    return store_uri

    

def ranking_free(iso_code):
    """
    Top free Mac app ranking
    """
    store_uri = make_store_uri(iso_code, str(genre.value), "FreeMacApps")
    
    return request_url(store_uri)


def ranking_paid(iso_code):
    """
    Top paid Mac applications
    """
    store_uri = make_store_uri(iso_code, str(genre.value), "PaidMacApps")
    
    return request_url(store_uri)


def ranking_grossing(iso_code):
    """
    Top grossing Mac applications
    """
    store_uri = make_store_uri(iso_code, str(genre.value), "MacAppsByRevenue")
    
    return request_url(store_uri)

"""
Request an URL
"""
def request_url(url):
    conn = http.client.HTTPSConnection(store_server)
    headers = { "Cache-Control" : "no-cache" }
    conn.request("GET", url, None, headers)
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


def print_parameters():
    """
    Print help information
    """
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
store_countries = [country for country in store_countries if country[0] == True]
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