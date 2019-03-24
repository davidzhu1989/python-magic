#!/usr/bin/env python
# @Time : 2019/3/24 11:17 
__author__ = 'Boaz'


def location(city,country,population=''):
    if population:
        formatted = city+','+country+" - "+str(population)
    else:
        formatted = city+','+country
    return formatted.title()
