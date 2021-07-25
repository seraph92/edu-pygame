__author__ = "seraph92@gmail.com"
# Logging Module

import sys
import os
import logging

LOG = logging.getLogger()
#LOG.setLevel(logging.DEBUG)
LOG.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
LOG.addHandler(stream_handler)

def getCurFuncInfo(depth):
    # sys._getframe().f_lineno
    fileName = os.path.basename(sys._getframe(depth).f_code.co_filename)
    funcName = sys._getframe(depth).f_code.co_name
    lineNum = sys._getframe(depth).f_lineno
    return ( fileName, funcName, lineNum )

def DEBUG(msg):
    #LOG.debug("[" + getCurFuncInfo(2) + "] " + msg)
    LOG.debug("[%s:%s:%d] "%getCurFuncInfo(2) + str(msg))

def ERROR(msg):
    LOG.error("[%s:%s:%d] "%getCurFuncInfo(2) + str(msg))

def INFO(msg):
    LOG.info("[%s:%s:%d] "%getCurFuncInfo(2) + str(msg))

# log file handler
#file_handler = logging.FileHandler('my.log')
#file_handler.setFormatter(formatter)
#LOG.addHandler(file_handler)