import base64
import hyhr_encrypt
import datetime
import logging
from hyhr_def import HYHR_KEY_FORMAT

logger = logging.getLogger(__name__)

class Hyhr_key:
    
    def __init__(self, data):
        self.data = data
    
    @property
    def Key(self):
        return self.data
    

    @Key.setter
    def Key(self, data):
        if self._isKeyBetter(data):
            self.data = data

    def _isKeyBetter(self, key):
        try:
            k = hyhr_encrypt.Decrypt(key)
            k_date = datetime.datetime.strptime(k,HYHR_KEY_FORMAT)

            pre = hyhr_encrypt.Decrypt(self.data)
            pre_date = datetime.datetime.strptime(pre, HYHR_KEY_FORMAT)

            return k_date >= pre_date
        except Exception as ex:
            logger.error(ex)
            return False
            
    @classmethod
    def GetKeyValidDate(cls, key):
        try:
            k = hyhr_encrypt.Decrypt(key)
            return k[0:10]
        except:
            logger.warning(f'Failed to Get key valid date. {key}')
            return None

    @classmethod
    def IsKeyValid(cls,key):
        try:
            k = hyhr_encrypt.Decrypt(key)
            k_date = datetime.datetime.strptime(k,HYHR_KEY_FORMAT)

            cur = hyhr_encrypt.Global_Cur_Date if hyhr_encrypt.Global_Cur_Date else hyhr_encrypt.GetCurDate()
            cur_date = datetime.datetime.strptime(cur, HYHR_KEY_FORMAT)

            return k_date >= cur_date
            # if k_date < cur_date:
            #     return False
            # else:
            #     # pre = hyhr_encrypt.Decrypt(KEY.Key)
            #     # pre_date = datetime.datetime.strptime(pre, HYHR_KEY_FORMAT)
            #     # if k_date <= pre_date:
            #     #     return False
            #     # else:
            #     #     return True
            #     return True
        except Exception as ex:
            logger.error(ex)
            return False

KEY = Hyhr_key(b'gAAAAABeewT21aCGUl7l2el_Vlem2C7LCB0IAsA-iKlLqyOzkiyZ8VaibZi3PAM9Y0eJVDFkv2vGka6eUINITtb3VObwn6kDDg==')