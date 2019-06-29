from pywinauto.application import Application
from pywinauto import Desktop
import time
import os
import re
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))

msgFile = os.path.join(root_dir, '信息.txt')
namesFile = os.path.join(root_dir, '名单.txt')
failedNamesFile = os.path.join(root_dir, '发送失败人员名单.txt')

#app = Application(backend='uia').start(r'C:\Program Files\WindowsApps\TencentWeChatLimited.forWindows10_2.6.3.0_x86__sdtnhv12zgd7a\WeChatStore\WeChatStore.exe')
app = Application(backend='uia').start(r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe')

dlg = Desktop(backend='uia').window(title='WeChat', class_name='WeChatMainWndForPC')
dlg.set_focus()
wrapper = dlg.wrapper_object()
width =100
height = 30
retry = 5

while retry> 0:
    wrapper.click_input(coords=(width,height))
    if dlg['3'].exists(timeout=2):
        break
    else:
        retry-=1
        width+=10
        height+=10
message = None
with open(msgFile, 'r', encoding='utf-8') as msg:
    message = msg.read()
    print(message)

if not len(message):
    print('消息为空，退出！')
    sys.exit()

failed= []
scount =0
with open(namesFile, 'r', encoding='utf-8') as f:
    for info in f:
        name = None
        data = []
        vals =[]
        validData = True
        info = info.strip()
        if not len(info):
            continue
        vals = re.split(r'\s+', info)
        length = len(vals)
        if length >= 2:
            name = vals[0]
            for i in range(1, length):
                try:
                    fee = float(vals[i])
                    data.append(fee)
                except Exception as ex:
                    print('异常数值:{}！暂不发送，请核对后重试！'.format(info))
                    failed.append(name)
                    validData = False
                    break
        elif length ==1:
            name = vals[0]
        else:
            print('异常数据，忽略.')
            continue
        
        if not validData:
            continue
        try:
            wrapper.click_input(coords=(width,height))
            #time.sleep(0.5)
            if dlg['3'].exists(timeout=2):
                dlg['3'].type_keys(name)
                #dlg['3'].type_keys('{ENTER 1}')
                time.sleep(0.5)
                wrapper.click_input(coords=(width,height+70))
                noFoundDlg = Desktop(backend='uia').window(title='WeChat', class_name='FTSMsgSearchWnd')
                #time.sleep(0.5)
                if noFoundDlg.exists(timeout=2):
                    noFoundDlg.close()
                    failed.append(name)
                    print('{} 不存在,请手工确认'.format(name))
                    time.sleep(1)
                    continue
                
                if len(data) == 0:
                    dlg.type_keys(message, with_spaces=True)
                else:
                    if '{}' in message:
                        dlg.type_keys(message.format(*data), with_spaces=True)
                    else:
                        dlg.type_keys(message, with_spaces=True)
                dlg.type_keys('%{s}')
                print('发送消息给{}成功'.format(name))
                scount+=1
            else:
                print('未发现搜索框，出错啦.')
                failed.append(name)
                
            time.sleep(1)
        except Exception as ex:
            failed.append(name)
            print('发送消息给{}失败，手工重发.err={}'.format(name, ex))

print('总共发送成功{}人.'.format(scount))
if len(failed) > 0:
    with open(failedNamesFile,'w',encoding='utf-8') as r:
        r.write('总共发送成功{}人.\n'.format(scount))
        print('以下{}人没有发送成功，请核对总人数，并重新发送:'.format(len(failed)))
        r.write('以下{}人没有发送成功，请核对总人数，并重新发送:\r\n'.format(len(failed)))
    
        print('\n'.join(failed))
        r.writelines('\n'.join(failed))

else:
    if os.path.exists(failedNamesFile):
        os.remove(failedNamesFile)