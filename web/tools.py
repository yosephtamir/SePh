#!/usr/bin/python3
"""Tools used in seph project"""
from datetime import datetime


class Tools():
    """Tools used for this projects"""
    timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
    def timestring(strtime):
        """This is used to format a datetime to one line string"""
        if strtime == None:
            return -1
        
        strtime = str(strtime)
        if len(strtime) != 26:
            return -2
        
        strng = ""
        for char in strtime:
            if char != " " and char != "-" and char != ":" and char != ".":
                strng = strng + char
        return strng

    def datetimeformat(strng):
        """This is used to format a datetime to a string date format"""
        if strng == None:
            return -1
        
        strng = str(strng)
        if len(strng) != 20:
            return -2
        

        dtimef = ""
        count = 0
        for char in strng:
            if count == 4 or count == 6:
                dtimef = dtimef + "-"
            if count == 8:
                dtimef = dtimef + "T"
            if count == 10 or count == 12:
                dtimef = dtimef + ":"
            if count == 14:
                dtimef = dtimef + "."
            dtimef = dtimef + char
            count = count + 1
        return dtimef