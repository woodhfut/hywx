from wxpy import *
import time
import os
from random import randint
import sys


bot = Bot(cache_path=True)
bot.enable_puid('hyhr_wxpy_puid.pkl')

message = ''
with open(r'd:\Project\Python\test\信息.txt', 'r', encoding='utf-8') as msg:
    message = msg.read()

failed = []
scount = 0

with open(r'd:\Project\Python\test\名单.txt','r', encoding='utf-8') as f:
    for name in f:
        name = name.strip()
        if not len(name):
            continue
        try:
            print('准备发给 {}'.format(name))
            friends = bot.friends().search(name)
            found = False
            for friend in friends:
                #print(friend.name)
                if friend.nick_name == name or friend.name == name:
                    friend.send(message.format(name))
                    print('成功发消息给{}'.format(name))
                    found = True
                    scount += 1
                    break
            if not found:
                print('没到找{},自己手工确认一下！'.format(name))
                failed.append(name)               
        except Exception as ex:
            print('发消息给{}失败了，稍后自己重新发一下...'.format(name))
            print('失败信息：{}'.format(ex))
            failed.append(name)
        time.sleep(randint(0,3))

failedlstPath = r'E:\寰宇\催帐\发送失败人员名单.txt'
print('总共发送成功{}人.'.format(scount))
if len(failed) > 0:
    with open(failedlstPath,'w',encoding='utf-8') as r:
        r.write('总共发送成功{}人.'.format(scount))
        print('以下{}人没有发送成功，请核对总人数，并重新发送:'.format(len(failed)))
        r.write('以下{}人没有发送成功，请核对总人数，并重新发送:\r\n'.format(len(failed)))
        for n in failed:
            print('\t{}'.format(n), end='  ')
            r.write('{}'.format(n))
else:
    if os.path.exists(failedlstPath):
        os.remove(failedlstPath)
#bot.logout()