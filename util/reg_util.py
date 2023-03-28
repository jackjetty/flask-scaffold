from datetime import datetime
import re

class RegUtil:

    @staticmethod
    def is_integer(val):
        reg='^0$|^[1-9]\d*$'
        pattern=re.compile(reg)
        if pattern.search(val):
            return True
        return False

    @staticmethod
    def is_date_yyyy_MM_dd(val):
        reg='^\d{4}[-/]\d{1,2}[-/]\d{1,2}$'
        pattern=re.compile(reg)
        if pattern.search(val):
            return True
        return False


    @staticmethod
    def is_date_yyyy_MM_dd_hh_mm_ss(val):
        reg='^\d{4}[-]\d{1,2}[-]\d{1,2}[ ]\d{1,2}:\d{1,2}:\d{1,2}$'
        pattern=re.compile(reg)
        if pattern.search(val):
            return True
        return False    

    @staticmethod
    def is_date_dd(val):
        reg='^0$|^[1-9]\d{0,1}$'
        pattern=re.compile(reg)
        if pattern.search(val):
            return True
        return False

    @staticmethod
    def is_date_yyyyMMdd(val):
        reg='^\d{4}\d{1,2}\d{1,2}$'
        pattern=re.compile(reg)
        if pattern.search(val):
            return True
        return False

