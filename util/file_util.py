#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import logging
import json
import decimal
from util import DictUtil
class FileUtil:

    @staticmethod
    def getFiles(input_dir):
        dir_files = os.listdir(input_dir)  
        files=[]
        for sub_dir in dir_files:       
            sub_dir = os.path.join(input_dir,sub_dir)   
            if not os.path.isdir(sub_dir):     
                files.append(sub_dir) 
        return files  


    @staticmethod
    def file_extension(tmpfilename): 
        return os.path.splitext(tmpfilename)[1][1:]      

    @staticmethod
    def file_name(tmpfilename):
        #return os.path.basename(tmpfilename)  
        return os.path.splitext(tmpfilename)[0]     


    @staticmethod
    def rename_dir_files(input_dir,dst_extension):
        for file in FileUtil.getFiles( input_dir):
            if FileUtil.file_extension(file) != dst_extension:
                #logging.info("files:%s",)
                dst_file=FileUtil.file_name(file)+"."+dst_extension 
                os.rename(file, dst_file)        