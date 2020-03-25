# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import hyhr_def
import logging
import hyhr_encrypt
import datetime
import hyhr_img
import hyhr_key
###########################################################################
## Class MyFrame2
###########################################################################
logger = logging.getLogger(__name__)

class KeyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = hyhr_def.HYHR_TITLE, pos = wx.DefaultPosition, size = wx.Size( 548,300 ), style =  wx.SYSTEM_MENU| wx.CLOSE_BOX|wx.CAPTION|wx.TAB_TRAVERSAL | wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.SetIcon(hyhr_img.xiaofu.Icon)
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, '', wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gbSizer4.Add( self.m_staticText13, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )
		
		validDate = hyhr_key.Hyhr_key.GetKeyValidDate(hyhr_key.KEY.Key)
		if validDate:
			self.m_staticText13.SetLabel(hyhr_def.HYHR_KEY_VALID_DATE+validDate)

		# if os.path.isfile(hyhr_def.HYHR_KEY_FILE):
		# 	try:
		# 		with open(hyhr_def.HYHR_KEY_FILE, 'r') as f:
		# 			data = f.read()
		# 			key_date = datetime.datetime.strptime(hyhr_encrypt.Decrypt(data.encode()),'%Y-%m-%d')
		# 			self.m_staticText13.SetLabel(hyhr_def.HYHR_KEY_VALID_DATE+ str(key_date)[0:10])
		# 			logger.info(f'current key valid {str(key_date)[0:10]}')
					
		# 	except Exception as ex:
		# 		logger.error(f'Exception in when check existing key. {ex}')

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, hyhr_def.HYHR_ENTER_KEY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gbSizer4.Add( self.m_staticText12, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer4.Add( self.m_textCtrl31, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, hyhr_def.HYHR_CONFIRM, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_button2, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnValidate )

	def __del__( self ):
		pass

	def OnValidate( self, event ):
		key = self.m_textCtrl31.GetValue().strip()
		
		if len(key):
			try:
				self.m_button2.Disable()
				if hyhr_key.Hyhr_key.IsKeyValid(key.encode()):
					hyhr_key.KEY.Key = key.encode()
					validDate = hyhr_key.Hyhr_key.GetKeyValidDate(hyhr_key.KEY.Key)
					self.m_staticText13.SetLabel(hyhr_def.HYHR_KEY_VALID_DATE + validDate)
					wx.MessageBox(f'{hyhr_def.HYHR_KEY_VALID_DATE}{validDate}')
				else:
					wx.MessageBox(hyhr_def.HYHR_KEY_ERROR)
					logger.error(hyhr_def.HYHR_KEY_ERROR)
				# dec_key = hyhr_encrypt.Decrypt(key.encode())
				# key_date = datetime.datetime.strptime(dec_key,'%Y-%m-%d')
				# logger.info(f'pre date {key_date}')
				# if hyhr_encrypt.Global_Cur_Date:
				# 	cur_date = datetime.datetime.strptime(hyhr_encrypt.Global_Cur_Date, '%Y-%m-%d')
				# else:
				# 	cur_date = datetime.datetime.strptime(hyhr_encrypt.GetCurDate(logger), '%Y-%m-%d')
				# logger.info(f'date now {str(cur_date)[0:10]}')
				# if key_date<cur_date:
				# 	wx.MessageBox(hyhr_def.HYHR_KEY_ERROR)
				# 	logger.error(hyhr_def.HYHR_KEY_ERROR)
				# 	return
				# if os.path.isfile(hyhr_def.HYHR_KEY_FILE):
				# 	with open(hyhr_def.HYHR_KEY_FILE,'r') as f:
				# 		pre_key = hyhr_encrypt.Decrypt(f.read().encode())
				# 		pre_date = datetime.datetime.strptime(pre_key,'%Y-%m-%d')
				# 		if pre_date > key_date:
				# 			return
				# with open(hyhr_def.HYHR_KEY_FILE, 'w') as f:
				# 	f.write(key)
				# wx.MessageBox(f'{hyhr_def.HYHR_KEY_VALID_DATE}{str(key_date)[0:10]}')
				# self.m_staticText13.SetLabel(hyhr_def.HYHR_KEY_VALID_DATE+ str(key_date)[0:10])
			except Exception as ex:
				logger.error(ex)
				wx.MessageBox(hyhr_def.HYHR_KEY_ERROR)
				logger.error(hyhr_def.HYHR_KEY_ERROR)
			finally:
				
				self.m_button2.Enable()
				#self.Close()
		else:
			wx.MessageBox(hyhr_def.HYHR_EMPTY_VALIDATION_KEY)
			logger.error(hyhr_def.HYHR_EMPTY_VALIDATION_KEY)