from pywinauto.application import Application
from pywinauto import Desktop
import time
import os
import re
import sys

class Result:
    def __init__(self, bmsg = False, bfile = False):
        self.bMsg = bmsg
        self.bFile = bfile
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.bMsg}, {self.bFile})'

root_dir = os.path.dirname(os.path.abspath(__file__))

msgFile = os.path.join(root_dir, '信息.txt')
namesFile = os.path.join(root_dir, '名单.txt')
failedNamesFile = os.path.join(root_dir, '发送失败人员名单.txt')
filesRootPath = os.path.join(root_dir, '文件')
bNeedSendFile = os.path.exists(filesRootPath) and len(os.listdir(filesRootPath))
bNeedSendMsg = os.path.isfile(msgFile) and os.stat(msgFile).st_size

assert os.path.isfile(namesFile),'名单不存在'
assert bNeedSendMsg or bNeedSendFile, '信息文件不存或者没有要发送的文件'

#app = Application(backend='uia').start(r'C:\Program Files\WindowsApps\TencentWeChatLimited.forWindows10_2.6.3.0_x86__sdtnhv12zgd7a\WeChatStore\WeChatStore.exe')
app = Application(backend='uia').start(r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe')
try:
    dlg = Desktop(backend='uia').window(class_name='WeChatMainWndForPC')
    dlg.set_focus()
except:
    print('未能发现桌面版微信，退出！')
    sys.exit()
wrapper = dlg.wrapper_object()

#try to locate the search textbox
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

if not dlg['3'].exists(timeout=2):
    print('没找到搜索框，退出！')
    sys.exit()


#going to send.
message = None
if bNeedSendMsg:
    with open(msgFile, 'r', encoding='utf-8') as msg:
        message = msg.read()

stat ={}
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
        elif length ==1:
            name = vals[0]
        else:
            print('异常数据，忽略.')
            continue
        
        stat[name] = Result(not bNeedSendMsg, not bNeedSendFile)
        #only if need send message, we need parse the detail values after name, or just name is enough.
        if bNeedSendMsg:
            for i in range(1, length):
                try:
                    fee = float(vals[i])
                    data.append(fee)
                except Exception as ex:
                    print('异常数值:{}！暂不发送，请核对后重试！'.format(info))
                    validData = False
                    break

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
                noFoundDlg = Desktop(backend='uia').window(class_name='FTSMsgSearchWnd')
                #time.sleep(0.5)
                if noFoundDlg.exists(timeout=2):
                    noFoundDlg.close()
                    print('{} 不存在,请手工确认'.format(name))
                    time.sleep(1)
                    continue
                
                if bNeedSendMsg:
                    if len(data) == 0:
                        dlg.type_keys(message.replace('{','').replace('}',''), with_spaces=True)
                    else:
                        if '{}' in message:
                            dlg.type_keys(message.format(*data), with_spaces=True)
                        else:
                            dlg.type_keys(message, with_spaces=True)
                    dlg.type_keys('%{s}')
                    print('发送消息给{}成功'.format(name))
                    stat[name].bMsg = True

                if bNeedSendFile:
                    #try to send file
                    for f in os.listdir(filesRootPath):
                        wrapper.click_input(coords=(width+285, height+525))
                        if dlg['open'].exists(timeout=2):
                            #print('good to find open dialog.')
                            dlg['open'].type_keys('%{n}')
                            time.sleep(0.1)
                            dlg['open'].type_keys(os.path.join(filesRootPath, f))
                            time.sleep(0.5)
                            dlg['open'].type_keys('{ENTER 1}')

                            dlg.type_keys('%{s}')
                            print('发送文件:{}给{}成功'.format(f, name))
                    
                    stat[name].bFile = True
                
            else:
                print('未发现搜索框，出错啦.')
                
            time.sleep(1)
        except Exception as ex:
            print('发送消息给{}失败，手工重发.err={}'.format(name, ex))


#statistic
if __debug__:
    print(stat)

success = list(filter(lambda x: x[1].bMsg and x[1].bFile, stat.items()))
failed = list(filter(lambda x: not x[1].bMsg or not x[1].bFile, stat.items()))
print('总共发送成功{}人.'.format(len(success)))
if len(failed) > 0:
    with open(failedNamesFile,'w',encoding='utf-8') as r:
        r.write('总共发送成功{}人.\n'.format(len(success)))
        print('以下{}人没有发送成功，请核对总人数，并重新发送:'.format(len(failed)))
        r.write('以下{}人没有发送成功，请核对总人数，并重新发送:\r\n'.format(len(failed)))
    
        print('\n'.join(map(lambda x: x[0], failed)))
        r.writelines('\n'.join(map(lambda x: x[0], failed)))

else:
    if os.path.exists(failedNamesFile):
        os.remove(failedNamesFile)