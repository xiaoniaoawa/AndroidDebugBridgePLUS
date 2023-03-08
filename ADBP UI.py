# -*- coding: UTF-8 -*-
import os
import time
import sys
import threading
import webbrowser

import tkinter as tk
import tkinter.ttk as ttk
import tttk
import tkinter.messagebox as msgbox
import tkinter.filedialog as filebox

win=tk.Tk()
win.title('ADBP UI')
win.minsize(300,500)
win.withdraw()

def openADBP():
    msgbox.showwarning('使用前警告','程序可能在早于Windows 10的系统上会出现兼容性问题，\n该问题可能导致程序崩溃')
    print('运行前提示：本工具仅限Windows NT 10.0+ 使用，如果版本不对可能会造成程序崩溃！')

def show_eula():
    acc_lst=[]
    acc_lst.append(bool(msgbox.askyesno('ADBP EULA','以下内容为ADBP的EULA\n\n'+
                    '欢迎使用Android Debug Bridge on Python(ADBP)\n\n使用此应用即你同意我们的eula：\n1) 法律相关\n'+
                    '---如使用者此应用涉及了法律风险，与作者无关(包括但不限于 安装违法违规软件、修改不被允许的系统文件、所读取文件泄密 等)\n'+
                    '1.1) 源代码相关\n-----请不要倒卖本程序，如有此情况，作者有权提出法律诉讼解决\n'+
                    '-----欢迎为本应用提出issue，但是作者有权对不限于 无效、刷屏、垃圾广告 进行举报删除\n'+
                    '-----您可以对本应用进行修改，但是请不要把源代码或者修改后的程序发给他人\n'+
                    '-----您可以对本应用进行修改，但是请不要把源代码或者修改后的程序发给他人\n'+
                    '1.2) 您的隐私：\n-----作者并不能(也没办法)读取您的信息，您享有您的设备中(除分享本软件)的所有权限\n\n'+
                    '以上为本内部版本的所有eula\n更新于23/02/06 12:20\n'+'\n您同意吗？')))
    acc_lst.append(bool(msgbox.askyesno('ADBP UI 使用与修改许可','以下内容为ADBP UI部分的使用与修改许可\n'+
                                        '1. 本程序UI部分依次遵循 MPL 2.0 开源许可及 不要做个屌人 开源许可\n'+
                                        '2. 本程序产生的任何法律问题作者皆不负责\n'+
                                        '3. 本程序UI部分的代码版权 和最终解释权归 真_人工智障 所有\n'+
                                        '4. 原作者可以将自己列入贡献者，并有权通过法律途径维护本作品的权利\n'+
                                        '5. 本许可非最终版本，可能随时更改\n'+
                                        '\n您同意吗？')))
    acc_lst.append(bool(msgbox.askyesno('ADB使用许可','您还需要了解并同意ADB的使用许可\n'+'\n您同意吗？')))
    return acc_lst

def refresh_device_lst():
    global device_lst,now_display_txt
    while True:
        result=os.popen('adb devices')
        resa=result.read().replace('List of devices attached','已连接如下设备：')
        result=os.popen('adb shell wm size')
        resb=result.read().replace('x',' × ')
        result=os.popen('adb shell wm density')
        resc=result.read()
        if resb=='':
            resb='未连接安卓设备'
            resc='无法加载'
        #os.system('cls')
        #print('已连接如下设备：')
        #print(res)
        device_lst['text']=resa
        now_display_txt['text']=str(resb)+'   DPI '+str(resc)
        time.sleep(0.3)

def reboot(choice):
    if choice=='系统':
        param=''
    elif choice=='Recovery':
        param=' recovery'
    elif choice=='Fastboot':
        param=' fastboot'
    elif choice=='BROM':
        param=' brom'
    print('重启到'+choice+'（'+param+'）')
    os.system('adb reboot'+param)

# 读取是否为首次运行
ooberead = open('firstrun.txt','r')
oobe = ooberead.read()
ooberead.close()

openADBP()

if oobe == '0':
    if not bool(os.path.exists("./adb.exe")):
        adbpath=filebox.askdirectory(title='请选择ADB所在位置')
        if adbpath=='' or adbpath==None:
            msgbox.showinfo('提醒','请正确选择ADB路径，点击确定将退出程序')
            exit()
        os.system('cd ' + filebox.askdirectory(title='请选择ADB所在位置'))
else:
    if show_eula()!=[True,True,True]:
        exit()
    geulaw = open('firstrun.txt','w')
    geulaw.write('0')
    geulaw.close()
    os.system('start '+sys.argv[0])
    exit()


# 界面部分
# 窗口显示
win.deiconify()
#多标签
nb=ttk.Notebook(win)


#设备
pta=tk.Frame(nb)
nb.add(pta,text='设备')

connect_pt=ttk.LabelFrame(pta,text='无线ADB')

tk.Label(connect_pt,text='部分设备支持无线ADB\n可以由处在同一局域网下的计算机无线连接').pack(fill=tk.X)

ip_enter=tttk.TipEnter(connect_pt,text='设备IP地址')
ip_enter.pack(fill=tk.X,padx=15,pady=5)

port_enter=tttk.TipEnter(connect_pt,text='ADB端口')
port_enter.pack(fill=tk.X,padx=15,pady=5)

ttk.Button(connect_pt,text='无线连接',command=lambda:os.system('adb connect '+ip_enter.get()+':'+port_enter.get())).pack(padx=15,pady=5)

tcpip_pt=ttk.LabelFrame(connect_pt,text='设置无线端口')

tk.Label(tcpip_pt,text='您可以在不支持无线ADB的设备上设置无线端口\n设备重启前可以使用局域网ADB').pack(fill=tk.X)

tcpip_enter=tttk.TipEnter(tcpip_pt,text='无线端口',command=lambda:print('尚未就绪'),btntxt='设置')
tcpip_enter.command=lambda:os.system('adb tcpip '+tcpip_enter.get())
tcpip_enter.refresh()
tcpip_enter.pack(fill=tk.X,padx=15,pady=5)

tcpip_pt.pack(fill=tk.X,padx=5,pady=5)

connect_pt.pack(side=tk.BOTTOM,fill=tk.X,padx=5,pady=5)

device_lst=tk.Label(pta,text='尚未加载', justify="left", anchor="w")
device_lst.pack(fill=tk.X)
refresh_devices_t=threading.Thread(target=refresh_device_lst)
refresh_devices_t.start()


#应用管理
ptb=tk.Frame(nb)
nb.add(ptb,text='应用管理')

tk.Label(ptb,text='').pack()

package_enter=tttk.TipEnter(ptb,text='应用包名')
package_enter.pack(fill=tk.X,padx=15,pady=5)

tttk.BtnRow(ptb,content={'卸载':lambda:os.system('adb shell pm uninstall -k --user 0 '+package_enter.get()),
                         '启动':lambda:os.system('adb shell am start '+package_enter.get()),
                         '在酷安查看':lambda:webbrowser.open("https://www.coolapk.com/apk/"+package_enter.get())}).pack(padx=15,pady=5)
tttk.BtnRow(ptb,content={'禁用':lambda:os.system('adb shell pm disable-user '+package_enter.get()),
                         '启用':lambda:os.system('adb shell pm enable '+package_enter.get())}).pack(padx=15,pady=5)

ttk.Button(ptb,text='安装APK',command=lambda:os.system('adb install '+filebox.askopenfilename(title='请选择安装包',filetypes=[('安卓安装包','.apk')]))).pack(pady=5)


#电源
ptc=tk.Frame(nb)
nb.add(ptc,text='电源')

tk.Label(ptc,text='').pack()
ttk.Button(ptc,text='关机',command=lambda:os.system('adb shell reboot -p')).pack(pady=15)

rbrow=tk.Frame(ptc)
rbchoose=ttk.Combobox(rbrow,value=['系统','Recovery','Fastboot','BROM'])
ttk.Button(rbrow,text='重启到',command=lambda:reboot(rbchoose.get())).pack(side=tk.LEFT)
rbchoose.pack(side=tk.RIGHT,fill=tk.X,expand=True)
rbrow.pack(fill=tk.X,padx=15)


#文件推送
ptd=tk.Frame(nb)
nb.add(ptd,text='文件推送')

path_enter=tttk.TipEnter(ptd,text='推送至')
path_enter.enter.insert(tk.END,'/sdcard')
path_enter.pack(fill=tk.X)

ttk.Button(ptd,text='推送',command=lambda:os.system('adb push '+filebox.askopenfilename(title='选择要推送的文件')+' '+path_enter.get())).pack(pady=15)


#界面调整
ptd=ttk.Notebook(nb)
nb.add(ptd,text='界面调整')


##显示
ptda=tk.Frame(nb)
ptd.add(ptda,text='显示')


now_display_pt=ttk.LabelFrame(ptda,text='当前设定')
now_display_pt.pack(fill=tk.X,padx=5,pady=5)
now_display_txt=tk.Label(now_display_pt,text='尚未加载')
now_display_txt.pack(fill=tk.X,padx=15,pady=5)


nb.pack(fill=tk.BOTH,expand=True)
win.mainloop()

#5Zyo5oiR5oSP6K+G5Yiw6Ieq5bex57uI5bCG5aSx5Y675LiA5YiH5pe277yM5rOq5bey5LiN55+l5L2V5pe25ruR5Ye655y86KeS
