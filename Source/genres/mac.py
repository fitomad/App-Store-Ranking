#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, unique

#
# Codigos de categoría para la Mac App Store
#
@unique
class MacAppStoreGenre(Enum):
    Business = 2001
    Developer = 12002
    Education = 12003
    Entertainment = 12004
    Finance = 12005
    Games = 12006
    Game_Action = 12201
    Game_Adventure = 12202
    Game_Arcade = 12203
    Game_Board = 12204
    Game_Card = 12205
    Game_Casino = 12206
    Game_Dice = 12207
    Game_Educational = 12208
    Game_Family = 12209
    Game_Kids = 12210
    Game_Music = 12211
    Game_Puzzle = 12212
    Game_Racing = 12213
    Game_RolePlaying = 12214
    Game_Simulation = 12215
    Game_Sports = 12216
    Game_Strategy = 12217
    Game_Trivia = 12218
    Game_Word = 12219
    Health = 2007 
    Lifestyle = 12008
    Medical = 12010
    Music = 12011
    News = 12012
    Photography = 12013
    Productivity = 12014
    Reference = 12015
    Social = 12016
    Sports = 12017
    Travel = 12018
    Utilities = 12019
    Video = 12020
    Weather = 12021
    Design = 12022
