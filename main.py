from hyhr_ui import HYHR_UI, logger, SetCurDate
import wx
import wx.xrc
import wx.richtext
#import hyhr_utils as utils
import re
from pywinauto.application import Application
from pywinauto import Desktop
import pywinauto.keyboard
import time
import os
import sys
import logging
import hyhr_encrypt
import datetime
import hyhr_Registerkey
import threading
import hyhr_def
from hyhr_sortedListCtrl import SortedListCtrl
import hyhr_img
import hyhr_key
import pickle
import requests
import cryptography.fernet
from wx.lib.embeddedimage import PyEmbeddedImage
if __name__ == '__main__':

    logger.info('开始...')
    t = threading.Thread(target=SetCurDate).start()

    app = wx.App()
    frame = HYHR_UI(None)
    frame.Show()
    app.MainLoop()
    logger.info('退出...')