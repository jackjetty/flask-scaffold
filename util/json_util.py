#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
import json
import decimal
from util import DictUtil
class JsonUtil:

    @staticmethod
    def json_serialize(obj):

        if str(type(obj)) == "<class 'list'>": 
            obj_dic=[]
            for index in range(0,obj.__len__()): 
                obj_dic.append(JsonUtil.class2dic(obj[index]))
        else:
            obj_dic = JsonUtil.class2dic(obj)
        return json.dumps(obj_dic,ensure_ascii=False)


    @staticmethod
    def class2dic_no_none(obj):
        obj_dic=JsonUtil.class2dic(obj)
        return DictUtil.remove_None_value_elements(obj_dic)


    @staticmethod
    def class2dic(obj):

        obj_dic = obj.__dict__
        #print(obj_dic)
        for key in obj_dic.keys():
            
            value = obj_dic[key]
            obj_dic[key] = JsonUtil.value2py_data(value)
        return obj_dic    

    @staticmethod
    def value2py_data(value):
        
        if isinstance(value, decimal.Decimal): 
            return float(value)
        '''
        if type(value) is int:
            return str(value)   
        '''     
        if str(type(value)).__contains__('.'):
            # value 为自定义类
            value = JsonUtil.class2dic(value)
        elif str(type(value)) == "<class 'list'>":
            # value 为列表
            for index in range(0, value.__len__()):
                value[index] = JsonUtil.value2py_data(value[index])
        return value

    @staticmethod
    def json_deserialize(json_data, obj):
        py_data = json.loads(json_data)
        JsonUtil.dic2class(py_data, obj)

    @staticmethod
    def dic2class(py_data, obj):
        for name in [name for name in dir(obj) if not name.startswith('_')]:
            if name not in py_data:
                setattr(obj, name, None)
            else:
                value = getattr(obj, name)
                setattr(obj, name, JsonUtil.set_value(value, py_data[name]))

    @staticmethod
    def set_value(value, py_data):
        if str(type(value)).__contains__('.'):
            # value 为自定义类
            JsonUtil.dic2class(py_data, value)
        elif str(type(value)) == "<class 'list'>":
            # value为列表
            if value.__len__() == 0:
                # value列表中没有元素，无法确认类型
                value = py_data
            else:
                # value列表中有元素，以第一个元素类型为准
                child_value_type = type(value[0])
                value.clear()
                for child_py_data in py_data:
                    child_value = child_value_type()
                    child_value = JsonUtil.set_value(child_value, child_py_data)
                    value.append(child_value)
        else:
            value = py_data
        return value        