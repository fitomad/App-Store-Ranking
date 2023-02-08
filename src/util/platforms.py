#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, unique

#
# Platforms
#
@unique
class iOSPlatform(Enum):
    iPhone = "iphone"
    iPad = "ipad"
    AppleTV = "appletv"
