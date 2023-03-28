#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
import json
class ListUtil:
    
    @staticmethod
    def emptyIfNone(input_list):
        if input_list is None:
            input_list=[]
        return input_list   

    @staticmethod
    def splitGroups(input_list,n):
        for i in range(0, len(input_list), n):
            yield input_list[i:i + n]

