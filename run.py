# -*- coding: UTF-8 -*-
import os
import time

def openADBP():
    print('运行前提示：本工具仅限Windows NT 10.0+ 使用，如果版本不对可能会造成程序崩溃！')
    time.sleep(2)
    print('输入 "Y"或"y"或"yes"或"YES"继续')
    a=input()
    if a == 'yes' or a == 'y' or a == 'YES' or a == 'Y':
        print('欢迎使用Android Debug Bridge on Python(ADBP)')
        print('&#65;&#68;&#66;&#80;&#32;&#98;&#121;&#32;&#120;&#105;&#97;&#111;&#110;&#105;&#97;&#111;')
        print('使用此应用即你同意我们的eula：')
        print('1) 法律相关')
        print('---如使用者此应用涉及了法律风险，与作者无关(包括但不限于 安装违法违规软件、修改不被允许的系统文件、所读取文件泄密 等)')
        print('1.1) 源代码相关')
        print('-----请不要倒卖本程序，如有此情况，作者有权提出法律诉讼解决')
        print('-----欢迎为本应用提出iessue，但是作者有权对不限于 无效、刷屏、垃圾广告 进行举报删除')
        print('-----您可以对本应用进行修改，但是请不要把源代码或者修改后的程序商用')
        print('-----请不要对无关人员发送内部版本的本作品，作者有权追溯发布者与接收人')
        print('1.2) 您的隐私：')
        print('-----作者并不能(也没办法)读取您的信息，您享有您的设备中(除分享本软件的内部或保密信息)的所有权限！')
        print('以上为本内部版本的所有eula')
        print('更新于23/02/06 12:20 \n 输入 y 继续')
    else:
        print('注意：这会杀死所有adb进程，是否继续？')
        os.system("pause")
        os.system('taskkill /f /t /im adb.exe')
        os.system('taskkill /f /t /im adbd.exe')
openADBP()
ooberead = open('firstrun.txt','r')
oobe = ooberead.read()
ooberead.close()
if oobe == '0':
    os.system('cd ' + input('请输入adb所在位置，一般为文件夹内有adb.exe的地方  '))
    while True:
        print('\n\n\n\n')
        print('0 ==== 查看已连接设备')
        print('1 ==== 安装程序')
        print('2 ==== 删除程序')
        print('3 ==== 打开设置(默认包名)')
        print('4 ==== 重启到')
        print('5 ==== 推送文件')
        print('6 ==== 类原生网络修复')
        print('f ==== 启动Fastboot脚本')
        adbshell = input()
        if adbshell == '0':
            print('以下为adb输出的设备列表: ')
            print('----------')
            os.system('adb devices')
            print('----------')
        elif adbshell == '1':
            packagename = input('请输入文件路径，拖进来也行，记得删掉左右的(双)引号\n')
            packageinstall = 'adb install '+packagename
            #要查看命令那就取消下面这行的注释
            #print(packageinstall)
            os.system(packageinstall)
            print('完成')
        elif adbshell == '2':
            packagename = input('请输入包名\n')
            packageunstall = 'adb shell pm uninstall -k --user 0 '+packagename
            os.system(packageunstall)
            print('完成')
        elif adbshell == '3':
            os.system('adb shell am start com.android.settings')
            print('完成')
        elif adbshell == '4':
            print('\n\n重启到...?')
            print('1=fastboot  2=recovery  3=brom  4=system 其他可直接输入')
            rebootsetting = input()
            if rebootsetting == '1':
                os.system('adb reboot fastboot')
            elif rebootsetting == '2':
                os.system('adb reboot recovery')
            elif rebootsetting == '3':
                os.system('adb reboot brom')
            elif rebootsetting == '4':
                os.system('adb reboot')
            else:
                os.system('adb reboot '+rebootsetting)
        elif adbshell == '5':
            print('这会将文件推送到手机的/sdcard 目录')
            os.system('adb push '+input()+' '+'/sdcard')
        elif adbshell == '6':
            print('这会将您的手机默认204服务器改为MIUI服务器（https://connect.rom.miui.com/generate_204），确认吗？')
            print('input "Y" to continue or other to pause.')
            if input() == 'Y':
                os.system('settings delete global captive_portal_mode && settings put global captive_portal_mode 0 && settings delete global captive_portal_https_url && settings delete global captive_portal_http_url')
                os.system('settings put global captive_portal_https_url https://connect.rom.miui.com/generate_204 && settings put global captive_portal_http_url http://connect.rom.miui.com/generate_204')
            else:
                pass
        




else:
    print('您需要同意 Google LLC 的eula才可使用此软件：')
    while True:
        print('使用r阅读，i同意，其他退出')
        geulai = input()
        if geulai == 'r':
            geula = open('NOTICE.txt','r',encoding='ANSI',errors='ignore')
            geularead = geula.read()
            geula.close()
            print(geularead)
        elif geulai == 'i' or geulai == 'y':
            geulaw = open('firstrun.txt','w')
            geulaw.write('0')
            geulaw.close()
            print('重新运行软件后即可使用')
            os.system('pause')
            break
        else:
            os.system('pause')
            break