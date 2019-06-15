from wxpy import *
import time
import os
from random import randint
import sys
import re

bot = Bot(cache_path=True)
bot.enable_puid('hyhr_wxpy_puid.pkl')

message = None
baseroot = os.path.dirname(os.path.abspath(__file__))
imgs = [f for f in os.listdir(baseroot) if os.path.isfile(os.path.join(baseroot, f)) and (f.lower().endswith('.png') or f.lower().endswith('.jpg'))]

with open( os.path.join(baseroot,'信息.txt'), 'r', encoding='utf-8') as msg:
    message = msg.read()
    
failed = []
scount = 0

with open(os.path.join(baseroot,'名单.txt'),'r', encoding='utf-8') as f:
    for info in f:
        name = None
        fee = None
        vals =[]
        info = info.strip()
        if not len(info):
            continue
        vals = re.split(r'\s+', info)
        length = len(vals)
        if length == 2:
            name = vals[0]
            try:
                fee = float(vals[1])
            except Exception as ex:
                fee=None
                print('{}：输入的费用值为{}不是数值！暂不发送，请核对后重试！'.format(name, vals[1]))
                failed.append(name)
                continue
        elif length ==1:
            name = vals[0]
        else:
            print('异常数据，忽略.')
            continue
        try:
            print('准备发给 {}'.format(name))
            friends = bot.friends().search(name)
            found = False
            for friend in friends:
                #print(friend.name)
                if friend.name == name:
                    if message:
                        if not fee:
                            friend.send(message)
                        else:
                            if '{}' in message or '{ }' in message:
                                friend.send(message.format(fee))
                            else:
                                print('消息格式不正确，请确保需要填写费用的位置设置为{}， 退出！')
                                sys.exit()
                        print('成功发消息给{}'.format(name))
                    for f in imgs:
                        friend.send_image(os.path.join(baseroot, f))
                        print('成功发图片{}给{}'.format(f,name))
                    
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

failedlstPath = os.path.join(baseroot,'发送失败人员名单.txt')
print('总共发送成功{}人.'.format(scount))
if len(failed) > 0:
    with open(failedlstPath,'w',encoding='utf-8') as r:
        r.write('总共发送成功{}人.\n'.format(scount))
        print('以下{}人没有发送成功，请核对总人数，并重新发送:'.format(len(failed)))
        r.write('以下{}人没有发送成功，请核对总人数，并重新发送:\r\n'.format(len(failed)))
    
        print('\n'.join(failed))
        r.writelines('\n'.join(failed))

else:
    if os.path.exists(failedlstPath):
        os.remove(failedlstPath)
#bot.logout()