#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
import json
class StringUtil:
    
    @staticmethod
    def emptyIfNone(input_str):
        if input_str is None:
            input_str=""
        return input_str   