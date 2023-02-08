#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from util import countries, genres, common


def ranking(iso_code, section):
    """
    Mac App Store ranking for a country and a section
    """
    store_uri = common.make_store_uri(iso_code, str(genre.value), section)
    position = common.fetch(store_uri, AppID)

    return position


def print_parameters():
    """
    Print help information
    """
    print("\r\n\t{0:^26}\r\n".format("Mac App Store Categories"))

    for genre in genres.MacAppStoreGenre:
        print("\t{0:^20} = {1:<6}".format(genre.name, genre.value))

    
    print("\r\n\t{0:^26}\r\n".format("Countries availables"))
    print("\t{0:^20} = {1:<6}".format("All countries", "world"))
    print("\t{0:^20} = {1:<6}\r\n".format("Top 10 (by revenue)", "top"))

    print("\tExample: mac-ranking.py -appid 123456789 -category 12014 -stores top\r\n")
    
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
    genre = genres.MacAppStoreGenre(args.category)
except ValueError:
    print_parameters()
    print("\tCategory not available. Take a look at category section above.\r\n")

    sys.exit()

# App ID. Located at iTunesConnect.

AppID = args.appid

print("\r\n\t{0:^50}\r\n".format("Mac App Store. Ranking"))
print("\t{0:20}{1:>10}{2:>10}{3:>10}\r\n".format("Country", "Free", "Paid", "Grossing"))

for country in store_countries:
    position_free = ranking(country[1], "FreeMacApps")
    position_paid = ranking(country[1], "PaidMacApps")
    position_grossing = ranking(country[1], "MacAppsByRevenue")

    print("\t{0:20.17}{1:>10}{2:>10}{3:>10}".format(country[2], position_free, position_paid, position_grossing))

print("\r\n\t{0:^50}".format("A script by @fitomad."))
print("\t{0:^50}\r\n".format("GitHub: https://github.com/fitomad/App-Store-Ranking"))