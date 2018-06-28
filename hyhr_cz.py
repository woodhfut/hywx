from wxpy import *
import time
import os
from random import randint

bot = Bot(cache_path=True)
bot.enable_puid('hyhr_wxpy_puid.pkl')

message = ''
with open('信息.txt', 'r', encoding='utf-8') as msg:
    message = msg.read()

failed = []
#friend = bot.friends().search('Qiang')[0]
with open('名单.txt','r', encoding='utf-8') as f:
    for name in f:
        try:
            print('准备发给 {}'.format(name))
            friend = bot.friends().search(name)[0]
            friend.send(message.format(name))
            print('成功发消息给{}'.format(name))
        except Exception as ex:
            print('发消息给{}失败了，稍后自己重新发一下...'.format(name))
            print(ex)
            failed.append(name)
        time.sleep(randint(0,3))
#friend.send('hello from wxpy...')

failedlstPath = r'E:\寰宇\催帐\发送失败人员名单.txt'
if len(failed) > 0:
    with open(failedlstPath,'w',encoding='utf-8') as r:
        print('以下{}人没有发送成功，请重新发送:'.format(len(failed)))
        r.write('以下{}人没有发送成功，请重新发送:\r\n'.format(len(failed)))
        for n in failed:
            print('\t{}'.format(n), end='  ')
            r.write('{}'.format(n))
else:
    if os.path.exists(failedlstPath):
        os.remove(failedlstPath)
#bot.logout()