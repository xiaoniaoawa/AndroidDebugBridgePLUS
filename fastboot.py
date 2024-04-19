import os
def flash(part, image):
    if part == '' or image == '':
        print('无效的分区或文件')
    else:
        print('即将使用 fastboot flash 方法刷入 '+image+' 到 '+part+' 分区')
        print('这将会使用 '+ os.path.getsize() / 1073741824 + 'GiB 的空间，请确保 '+part+'分区的空间足够')
        print('继续？[N/y]')
        awnser = input
        if awnser == 'Y' or awnser == 'y':
            print('')
            os.system('fastboot devices')
            os.system('fastboot flash ' + part + ' ' + image)
            print('操作执行完成，请检查log')
            os.system('pause')
        else:
            pass
        return 0

def devices():
    print("列出了所有设备：")
    os.system('adb devices')
    os.system('fastboot devices')
    return 0
    
