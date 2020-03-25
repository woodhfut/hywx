# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# #key = 'this is my key'
# print(f'key : {key}')

# f = Fernet(key)

# msg = 'this is a secret message'

# token = f.encrypt(msg.encode())

# print(f'token: {token}')

# demsg = f.decrypt(token)

# print(demsg.decode())


import base64
import datetime
import requests
import logging
from cryptography.fernet import Fernet

worldTimeUrl = 'http://worldtimeapi.org/api/timezone/'
area = 'Asia/Shanghai'
salt = 'hyhr'
key='ThisismysecrectkeyIwillnottellyo'

logger = logging.getLogger(__name__)

Global_Cur_Date = None

def GetCurDate():
    try:
        url = worldTimeUrl + area
        ret = requests.get(url, timeout=5)
        jsn = ret.json()
        sdt = jsn['datetime'][0:10]
        return sdt

    except Exception as ex:
        logger.warning(f'Failed to get current time. {ex}')
        return str(datetime.date.today())


def Encrypt(msg=None):
    cipher_key = base64.b64encode(key.encode())
    cipher = Fernet(cipher_key)
    if msg:
        return cipher.encrypt(msg.encode()).decode()
    else:
        return cipher.encrypt(GetCurDate().encode()).decode()

def Decrypt(msg):
    cipher_key = base64.b64encode(key.encode())
    cipher = Fernet(cipher_key)
    return cipher.decrypt(msg).decode()

if __name__== '__main__':
    ed = Encrypt('2020-08-25')
    print(ed)
    print(Decrypt(ed.encode()))
    #print(GetCurDate())