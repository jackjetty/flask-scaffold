import logging
import time 
import os
from starter import scheduler,logger
from flask import current_app
def testTask():
    with  current_app._get_current_object().app_context() if   scheduler.app is None else scheduler.app.app_context():
        logger.info("test job is start")


