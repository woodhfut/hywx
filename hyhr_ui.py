# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

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
###########################################################################
## Class hyhr_UI
###########################################################################

class HYHR_UI ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = hyhr_def.HYHR_TITLE, pos = wx.DefaultPosition, size = wx.Size( 650,750 ), style = wx.SYSTEM_MENU| wx.CLOSE_BOX|wx.CAPTION|wx.TAB_TRAVERSAL | wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		self.SetIcon(hyhr_img.xiaofu.GetIcon())

		self.m_menubar1 = wx.MenuBar( wx.MB_DOCKABLE )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"认证", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"发送日志", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )
		self.m_menu1.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.m_menu1, u"文件" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"联系我们", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menubar1.Append( self.m_menu2, u"帮助" )

		self.SetMenuBar( self.m_menubar1 )

		gbSizer = wx.GridBagSizer(0,0)

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"导入名单：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gbSizer.Add(self.m_staticText8, pos=(0,0), flag=wx.ALL, border=5)

		self.m_namePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"选择名单", u"*.txt", wx.DefaultPosition, wx.Size( 480,-1 ), wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST )
		gbSizer.Add(self.m_namePicker, pos=(0,1), flag=wx.EXPAND|wx.ALL, border=5)

		# m_checkList2Choices = []
		# self.m_checkList2 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,300 ), m_checkList2Choices, 0 )
		# gbSizer.Add(self.m_checkList2, pos=(1,0), span=(3,2), flag=wx.EXPAND|wx.ALL, border=5)

		self.m_namesList = SortedListCtrl(2,{},self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,300 ), style = wx.LC_REPORT )
		self.m_namesList.InsertColumn(0, '姓名', width=300)
		self.m_namesList.InsertColumn(1, '发送结果', width=100)
		gbSizer.Add(self.m_namesList, pos=(1,0), span=(3,2), flag=wx.EXPAND|wx.ALL, border=5)

		# self.m_statusText = wx.StaticText(self, wx.ID_ANY, '注意：\n 1. xx\n 2.xxx\n', wx.DefaultPosition, wx.DefaultSize, 0)
		# gbSizer.Add(self.m_statusText, pos=(1,2), span=(9, 1), flag=wx.EXPAND|wx.ALL, border=5)

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"填写要发送的内容：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gbSizer.Add(self.m_staticText10, pos=(4,0), span=(1, 1), flag=wx.ALL, border=5)

		self.m_richText3 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,140 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gbSizer.Add(self.m_richText3, pos=(5,0), span=(3,2), flag=wx.EXPAND|wx.ALL, border=5)

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"选择要发送的文件：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gbSizer.Add(self.m_staticText9, pos=(9,0), flag=wx.EXPAND|wx.ALL, border=5)

		self.m_fileImgPicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 480,-1 ), wx.FLP_DEFAULT_STYLE |wx.FLP_FILE_MUST_EXIST)
		gbSizer.Add(self.m_fileImgPicker, pos=(9,1), flag=wx.EXPAND|wx.ALL, border=5)

		self.m_send = wx.Button( self, wx.ID_ANY, u"发送", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		gbSizer.Add(self.m_send, pos=(10,0), flag=wx.ALL, border=5 )

		self.SetSizer(gbSizer)
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_MENU, self.OnValidation, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.OnLog, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.OnContactUs, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_menuItem3.GetId() )
		self.m_namePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnNameFileChanged )
		self.m_fileImgPicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileImgChanged )
		self.m_send.Bind( wx.EVT_BUTTON, self.OnSend )
		#self.m_namesList.Bind(  wx.EVT_LIST_COL_CLICK, self.OnListColClick )
		#self.m_richText3.Bind( wx.EVT_TEXT, self.OnMsgText )

		self.names =[]
		self.msg=''
		self.file=''
		if os.path.isfile(hyhr_def.HYHR_KEY_FILE):
			with open(hyhr_def.HYHR_KEY_FILE, 'rb') as f:
				hyhr_key.KEY = pickle.load(f)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose(self, event):
		try:
			with open(hyhr_def.HYHR_KEY_FILE, 'wb') as f:
				pickle.dump(hyhr_key.KEY, f)
		except Exception as ex:
			logger.warning(f'error while close the frame, {ex}')
		event.Skip()

	def OnLog(self, event):
		if os.path.isfile(logName):
			logPath = os.path.join(os.path.abspath(__file__), logName)
			wx.MessageBox(f'发送日志在{logPath}。')
		else:
			wx.MessageBox('发送日志不存在！')
		event.Skip()
	def OnValidation( self, event ):
		keyFrame = hyhr_Registerkey.KeyFrame(self)
		keyFrame.Show()
		event.Skip()

	def sortListCtrlItem(self, item1, item2):
		logger.info(f'{item1}, {item2}')
		return item1 > item2

	def OnContactUs( self, event ):
		event.Skip()

	def OnAbout( self, event ):
		wx.MessageBox('HYHR\n\nxiaofu ver:	0.5.0.0\n')
		event.Skip()

	def OnNameFileChanged( self, event ):
		names = self.m_namePicker.GetPath()
		try:
			with open(names, 'r',encoding='utf-8') as f:
				self.m_namesList.DeleteAllItems()
				self.names.clear()
				for name in f:
					name = name.strip()
					if(len(name)==0):
						continue
					index = self.m_namesList.InsertItem(self.m_namesList.GetItemCount(), name)
					self.m_namesList.SetItem(index, 1, '❌')
					self.m_namesList.SetItemTextColour(index, wx.RED)
					self.m_namesList.SetItemData(index, index)
					self.names.append(name)
					self.m_namesList.itemDataMap[index] = (name, '❌')
			#print(self.names)
		except Exception as ex:
			wx.MessageBox(hyhr_def.HYHR_LOAD_NAME_FAIL)
			logger.error(f'{hyhr_def.HYHR_LOAD_NAME_FAIL}{ex}')
		finally:	
			event.Skip()
		
	def OnFileImgChanged( self, event ):
		self.file=self.m_fileImgPicker.GetPath()
		event.Skip()

	def OnSend( self, event ):
		try:
			self.m_send.Disable()
			if not hyhr_key.Hyhr_key.IsKeyValid(hyhr_key.KEY.Key):
				logger.error(hyhr_def.HYHR_KEY_ERROR)
				wx.MessageBox(hyhr_def.HYHR_KEY_ERROR)
				return
			else:
				logger.info(hyhr_def.HYHR_KEY_VALID)
			#check key exists
			# if not os.path.isfile(key):
			# 	wx.MessageBox('认证码不存在，请先到菜单文件--认证中输入认证码')
			# 	logger.error('认证码不存在')
			# 	return
			# else:
			# 	with open(key, 'r', encoding='utf-8') as k:
			# 		data = k.read()
			# 		key_date = datetime.datetime.strptime(hyhr_encrypt.Decrypt(data.encode()),hyhr_def.HYHR_KEY_FORMAT)
			# 		if hyhr_encrypt.Global_Cur_Date:
			# 			cur_date = datetime.datetime.strptime(hyhr_encrypt.Global_Cur_Date,hyhr_def.HYHR_KEY_FORMAT)
			# 		else:
			# 			cur_date = datetime.datetime.strptime(hyhr_encrypt.GetCurDate(),hyhr_def.HYHR_KEY_FORMAT)
			# 		if cur_date > key_date:
			# 			wx.MessageBox(hyhr_def.HYHR_KEY_EXPIRED)
			# 			logger.error(hyhr_def.HYHR_KEY_EXPIRED)
			# 			return
			# 		else:
			# 			logger.info('认证码有效！')
			self.msg = self.m_richText3.GetValue()
			if len(self.names)==0 or (len(self.msg)==0 and len(self.file)==0):
				wx.MessageBox(hyhr_def.HYHR_NAME_MSG_FILE_EMPTY)
				logger.error(hyhr_def.HYHR_NAME_MSG_FILE_EMPTY)
				return
			
			if not os.path.isfile(wechat):
				wx.MessageBox(hyhr_def.HYHR_WECHAT_NOT_INSTALLED)
				logger.error(hyhr_def.HYHR_WECHAT_NOT_INSTALLED)
				return
			app = Application(backend='uia').start(wechat)
			try:
				dlg = Desktop(backend='uia').window(class_name=wechat_class_name)
				dlg.set_focus()
			except Exception as ex:
				wx.MessageBox(hyhr_def.HYHR_WECHAT_NOT_STARTED)
				logger.error(f'{hyhr_def.HYHR_WECHAT_NOT_STARTED} {ex}')
				return
			wrapper = dlg.wrapper_object()
			wrapper.click_input(coords=(searchbox_x,searchbox_y))

			counter = 0
			for info in self.names:
				name = None
				data = []
				vals =[]
				validData = True
				info = info.strip()
				if not len(info):
					continue
				vals = re.split(r'\s+', info)
				length = len(vals)
				if length >= 1:
					name = vals[0]
				else:
					logger.warning('异常数据，忽略.')
					counter+=1
					continue

				if len(self.msg):
					for i in range(1, length):
						try:
							fee = float(vals[i])
							data.append(fee)
						except Exception as ex:
							logger.warning('异常数值:{}！暂不发送，请核对后重试！'.format(info))
							validData = False
							break

				if not validData:
					counter+=1
					continue
				
				try:
					wrapper.click_input(coords=(searchbox_x,searchbox_y))
					wrapper.type_keys(name)
					time.sleep(1.5)
					wrapper.click_input(coords=(searchbox_x,searchResult_y))
					noFoundDlg = Desktop(backend='uia').window(class_name=wechat_notFound_class_name)
					#time.sleep(0.5)
					if noFoundDlg.exists(timeout=2):
						noFoundDlg.close()
						logger.warning('{} 不存在,请手工确认'.format(name))
						time.sleep(1)
						counter+=1
						continue
					
					if len(self.msg):
						if len(data) == 0:
							dlg.type_keys(self.msg.replace('{','').replace('}',''), with_spaces=True)
						else:
							if '{}' in self.msg:
								if self.msg.count('{}')== len(data):
									dlg.type_keys(self.msg.format(*data), with_spaces=True)
								else:
									logger.warning(f'{name} 数据数目和消息格式不匹配，忽略该条记录！')
									counter+=1
									continue
							else:
								dlg.type_keys(self.msg, with_spaces=True)
						dlg.type_keys('%{s}')
						logger.info('发送消息给{}成功'.format(name))
						

					if len(self.file):
						#try to send file
						#for f in os.listdir(self.file):
						wrapper.click_input(coords=(sendfile_x, sendfile_y))
						#pywinauto.keyboard.send_keys(self.file)
						pywinauto.keyboard.send_keys(self.file)
						pywinauto.keyboard.send_keys('{ENTER 1}')
						dlg.type_keys('%{s}')
						logger.info('发送文件{}给{}成功'.format(self.file,name))

					self.m_namesList.SetItem(counter, 1, '✔')
					self.m_namesList.SetItemTextColour(counter, wx.GREEN)
					self.m_namesList.itemDataMap[counter] = (name, '✔')
					counter+=1

				except Exception as ex:
					#wx.MessageBox('发送错误！{}.'.format(ex))
					logger.warning(f'{hyhr_def.HYHR_SEND_ERROR}{ex}.')
					counter+=1
		except Exception as ex:
			wx.MessageBox(f'{hyhr_def.HYHR_SEND_ERROR}{ex}.')
			logger.error(f'{hyhr_def.HYHR_SEND_ERROR} {ex}.')
		finally:
			self.m_send.Enable()
		event.Skip()



#################Global Variable###########################		
logName = 'SendResult.log'
key = 'key.key'
wechat = r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'
wechat_class_name = 'WeChatMainWndForPC'
wechat_notFound_class_name = 'FTSMsgSearchWnd'
searchbox_x = 120
searchbox_y = 50
searchResult_y = 120
sendfile_x = 470
sendfile_y = 590

##################Logging config ###########################
logger = logging.getLogger()
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler(logName, mode='w', encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#############
#get cur date to save load time when submit.
def SetCurDate():
	hyhr_encrypt.Global_Cur_Date = hyhr_encrypt.GetCurDate()
	logger.info(f'cur date is {hyhr_encrypt.Global_Cur_Date}')

if __name__ == '__main__':
	logger.info('开始...')
	t = threading.Thread(target=SetCurDate).start()
	
	app = wx.App()
	frame = HYHR_UI(None)
	frame.Show()
	app.MainLoop()
	logger.info('退出...')