#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
import json
import calendar
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta 
import re
class DateUtil:
    @staticmethod
    def getDateRange(fromDate,toDate):
        dates = []
        current_date = datetime.strptime(fromDate, "%Y-%m-%d")
        date_str = fromDate[:]
        while date_str <= toDate:
            dates.append(date_str)
            current_date = current_date +  timedelta(days=1)
            date_str = current_date.strftime("%Y-%m-%d")
        return dates

    @staticmethod
    def getMonthRange(fromMonth,toMonth):
        months = []
        current_date = datetime.strptime(fromMonth, "%Y-%m")
        month_str = fromMonth[:]
        while month_str <= toMonth:
            months.append(month_str)
            current_date = current_date +  relativedelta(months=1)
            month_str = current_date.strftime("%Y-%m")
        return months

    def getLastMonth(todo_month):
        
        current_date = datetime.strptime(todo_month, "%Y-%m")
        current_date = current_date +  relativedelta(months=-1)
        return current_date.strftime("%Y-%m")


    def getPlusMonth(todo_month,puls_months):
        
        current_date = datetime.strptime(todo_month, "%Y-%m")
        current_date = current_date +  relativedelta(months=puls_months)
        return current_date.strftime("%Y-%m")    

    def getLastYearMonth(todo_month):

        current_date = datetime.strptime(todo_month, "%Y-%m")
        current_date = current_date +  relativedelta(years=-1)
        return current_date.strftime("%Y-%m")    
       

    @staticmethod
    def getMonthLastDay(todo_month):

        current_date = datetime.strptime(todo_month, "%Y-%m")
        current_date = DateUtil.getMonthFirstDayAndLastDay(current_date.year,current_date.month)[1]
        return current_date.strftime("%Y-%m-%d")   
 
    @staticmethod
    def transferStandardDateString(todo_date): 
        if isinstance(todo_date,date):
            return todo_date.strftime("%Y-%m-%d")
        return todo_date  

    @staticmethod
    def transferStandardFormat(count_date):
        p=re.compile('(\d{4})-(\d{1,2})-(\d{1,2})')
        m=p.match(count_date) 
        if m: 
            return "{0:*>4}-{1:0>2}-{2:0>2}".format(m.group(1),m.group(2),m.group(3))
        return count_date    

    @staticmethod
    def getMonthFirstDayAndLastDay(year=None, month=None):
        """
        :param year: 年份，默认是本年，可传int或str类型
        :param month: 月份，默认是本月，可传int或str类型
        :return: firstDay: 当月的第一天，datetime.date类型
                lastDay: 当月的最后一天，datetime.date类型
        """
        if year:
            year = int(year)
        else:
            year = date.today().year

        if month:
            month = int(month)
        else:
            month = date.today().month

        # 获取当月第一天的星期和当月的总天数
        firstDayWeekDay, monthRange = calendar.monthrange(year, month)

        # 获取当月的第一天
        firstDay = date(year=year, month=month, day=1)
        lastDay = date(year=year, month=month, day=monthRange)

        return firstDay, lastDay    