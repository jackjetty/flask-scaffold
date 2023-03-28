#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
import json
class DictUtil:
    
    @staticmethod
    def remove_None_value_elements(input_dict):
        """
        remove the element(key/value) from dict if the value is None
        :param input_dict:
        :return: new dict
        """
        if type(input_dict) is not dict:
            return None
        result = {}
        for key in input_dict:
            tmp = {}
            if input_dict[key] is not None:
                if type(input_dict[key]).__name__ == 'dict':
                    tmp.update({key: DictUtil.remove_None_value_elements(input_dict[key])})
                else:
                    tmp.update({key: input_dict[key]})
            result.update(tmp)
        return result