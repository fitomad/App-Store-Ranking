#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from util import countries, platforms, genres, common


def ranking_free(iso_code, platform, genre):
    """
    Top free iPhone & iPad app ranking
    """
    store_section = str()

    if platform == platforms.iOSPlatform.iPhone.value:
        store_section = "FreeApplications"
    elif platform == platforms.iOSPlatform.iPad.value:
        store_section = "FreeIpadApplications"
    else:
        store_section = "FreeAppleTVApps"

    store_uri = common.make_store_uri(iso_code, genre, store_section)
    
    return common.fetch(store_uri, AppID)


def ranking_paid(iso_code, platform, genre):
    """
    Top paid iPhone & iPad app ranking
    """
    if platform == platforms.iOSPlatform.iPhone.value:
        store_section = "PaidApplications"
    elif platform == platforms.iOSPlatform.iPad.value:
        store_section = "PaidIpadApplications"
    else:
        store_section = "PaidAppleTVApps"

    store_uri = common.make_store_uri(iso_code, genre, store_section)

    return common.fetch(store_uri, AppID)


def ranking_grossing(iso_code, platform, genre):
    """
    Top grossing iPhone & iPad app ranking
    """
    if platform == platforms.iOSPlatform.iPhone.value:
        store_section = "AppsByRevenue"
    elif platform == platforms.iOSPlatform.iPad.value:
        store_section = "IpadAppsByRevenue"
    else:
        store_section = "AppleTVAppsByRevenue"

    store_uri = common.make_store_uri(iso_code, genre, store_section)
    
    return common.fetch(store_uri, AppID)


def print_parameters():
    """
    Print help information
    """
    print("\r\n\t{0:^26}\r\n".format("App Store Categories"))

    for genre in genres.AppStoreGenre:
        print("\t{0:^20} = {1:<6}".format(genre.name, genre.value))

    
    print("\r\n\t{0:^26}\r\n".format("Countries availables"))
    print("\t{0:^20} = {1:<6}".format("All countries", "world"))
    print("\t{0:^20} = {1:<6}\r\n".format("Top 10 (by revenue)", "top"))

    print("\r\n\t{0:^26}\r\n".format("Platforms"))
    print("\t{0:^20} = {1:<6}".format("iPhone", "iphone"))
    print("\t{0:^20} = {1:<6}".format("iPad", "ipad"))
    print("\t{0:^20} = {1:<6}\r\n".format("Apple TV", "appleTV"))

    print("\tExample: ios-ranking.py -appid 123456789 -category 12014 -stores top -platform iphone\r\n")

#
# Workflow
#
# Command line argument parser
parser = argparse.ArgumentParser(description='App Store Ranking.')

parser.add_argument('-appid', type=int, help='iTunesConnect application identifier.')
parser.add_argument('-stores', type=str, help='App Store country sets.')
parser.add_argument('-category', type=int, help='App category inside Mac App Store.')
parser.add_argument("-platform", type=str, help="Choose iPhone or iPad")
parser.add_argument('-p', '--parameters', action="store_true", help='List all posible values for Stores and Category.')

args = parser.parse_args()

if args.parameters:
    print_parameters()
    sys.exit()


# App Store Countries

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
    genre = genres.AppStoreGenre(args.category)
except ValueError:
    print_parameters()
    print("\tCategory not available. Take a look at category section above.\r\n")

    sys.exit()

# Platform

try:
    platform_arg = args.platform.lower()
    platform = platforms.iOSPlatform(platform_arg)
except ValueError:
    print_parameters()
    print("\tPlatform doen't exists. Take a look at platforms list above.\r\n")

    sys.exit()

# App ID. Located at iTunesConnect.

AppID = args.appid 

print("\r\n\t{0:^50}\r\n".format("App Store. Ranking " + platform.value))
print("\t{0:20}{1:>10}{2:>10}{3:>10}\r\n".format("Country", "Free", "Paid", "Grossing"))  

for country in store_countries:
    position_free = ranking_free(country[1], platform.value, genre.value)
    position_paid = ranking_paid(country[1], platform.value, genre.value)
    position_grossing = ranking_grossing(country[1], platform.value, genre.value)

    print("\t{0:20.17}{1:>10}{2:>10}{3:>10}".format(country[2], position_free, position_paid, position_grossing))

