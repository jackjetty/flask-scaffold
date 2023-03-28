#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import Decimal

class CalculateUtil:
    @staticmethod
    def getRate(numerator,denominator):
        if numerator is None:
            return None
        if denominator is None:
            return None 
        if int(denominator)==0 :
            return None      
        #to do 字符串判断
        #aa = Decimal('5.026').quantize(Decimal('0.00'))
        return round(100*numerator/denominator,2)

    @staticmethod
    def getGrowthRate(current_val,original_val):
        if current_val is None:
            return None
        if original_val is None:
            return None 
        return CalculateUtil.getRate(current_val-original_val,original_val)    

    @staticmethod
    def isNumber(num):
        try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
            float(num)
            return True
        except (TypeError, ValueError):  # ValueError为Python的一种标准异常，表示"传入无效的参数"
            pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
        '''
        try:
            import unicodedata  # 处理ASCii码的包
            unicodedata.numeric(num)  # 把一个表示数字的字符串转换为浮点数返回的函数
            return True
        except (TypeError, ValueError):
            pass
        '''
        return False 

    @staticmethod
    def myRound(num,digit):
        if not CalculateUtil.isNumber(num):
            return None
            
        return round(num,digit)

