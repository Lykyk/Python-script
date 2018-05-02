# -*- coding:utf-8 -*-
import os
import re
import shutil

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False


'''添加前缀
path    文件夹路径
prefix  要添加的前缀
'''
def addPrefix(path, prefix):
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        Olddir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        filename = os.path.splitext(files)[0]  # 文件名
        filetype = os.path.splitext(files)[1]  # 文件扩展名
        newfiles = prefix + filename + filetype  # 新文件名
        Newdir = os.path.join(path, newfiles)  # 新的文件路径
        print(files + "  --> " + newfiles)
        os.rename(Olddir, Newdir)  # 重命名
    print("给文件名添加前缀完成")


def add_prefix(file_path, new_file_path, prefix):
    lines = open(file_path, encoding='gb2312').readlines()  #打开文件，读入每一行
    print(new_file_path)
    fp = open(new_file_path, 'w', encoding='gb2312')  #打开要写的文件

    for line in lines:
        line_matches = re.findall(r'\w*\.php', line, re.M)  #正则表达式提取 *.php 文件名的字符串
        if line_matches: #空的 list 相当于 false
            line_matches = set(line_matches)    #list 除去重复元素，防止一行中出现重复元素时多次用 replace 替换
            for match in line_matches:  #提取到 *.php 文件名字符串
                line = line.replace(match, prefix + match)    #添加前缀,构造新的行字符串。replace 可将字符串里所有的 match 替换成 prefix + match
        fp.write(line)

    fp.close()  # 关闭文件


def add_prefix_files(dir_path, new_dir_path, prefix):
    filelist = os.listdir(dir_path)  # 该文件夹下所有的文件（包括文件夹）
    for filename in filelist:  # 遍历所有文件
        file_path = os.path.join(dir_path, filename)  # 原来的文件路径
        if os.path.isdir(file_path):  # 如果是文件夹则跳过
            continue
        new_file_path = os.path.join(new_dir_path, filename)    #新文件路径
        add_prefix(file_path, new_file_path, prefix)    #调用函数对文件内容操作


'''程序主逻辑'''
if __name__ == "__main__":

    '''确定原代码目录与生成代码目录'''
    source_dir = input(r"输入原代码文件夹路径(例如:C:\shop):")
    prefix = input("输入要添加的前缀(例如:XXX):")
    if source_dir[-1] != "\\":  #补加斜杠
        source_dir += "\\"
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(source_dir),"..")) #获取父目录
    target_dir = parent_dir + "\\" + prefix + "shop"
    select = input("将生成代码到目录 " + target_dir + "\n确定使用此目录继续请输入 1 \n使用自定义目录请输入 2 \n输入其他则退出:")
    if select == "1":  #等待用户确定继续操作
        pass
    elif select == "2":
        target_dir = input(r"输入生成代码文件夹路径(例如:C:\shop):")
    else:
        exit()

    '''复制不需要修改的文件'''
    shutil.copytree(source_dir, target_dir, ignore=shutil.ignore_patterns('*.php')) #复制文件夹，但忽略 *.php 文件，避免多余的复制
    conn_file_path = r"\conn\conn.php"
    shutil.copyfile(source_dir + conn_file_path, target_dir + conn_file_path) #复制 \conn\conn.php 文件
    conn_file_path = r"\admin\conn\conn.php"
    shutil.copyfile(source_dir + conn_file_path, target_dir + conn_file_path) #复制 \admin\conn\conn.php 文件
    print("\n复制文件完成\n")
    
    '''写入修改过的 php 文件'''
    mkdir(target_dir) #如不存在目标文件夹，则新建文件夹
    add_prefix_files(source_dir, target_dir, prefix)    #调用函数对目录下文件操作
    admin_dir_path = r"\admin"
    mkdir(target_dir + admin_dir_path) #如不存在目标文件夹，则新建文件夹
    add_prefix_files(source_dir + admin_dir_path, target_dir, prefix)
    print("\n修改 php 文件完成\n")

    '''修改文件名'''
    addPrefix(target_dir, prefix)
    addPrefix(target_dir + r"\conn", prefix)
    addPrefix(target_dir + r"\admin", prefix)
    addPrefix(target_dir + r"\admin\conn", prefix)
    print("\n修改文件名完成\n")

    print("\no(*￣▽￣*)ブ (゜-゜)つロ 干杯 ~ 所有文件已成功生成\n")
    os.system("pause")
