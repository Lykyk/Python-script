# -*- coding:utf-8 -*-
#　转换文件编码（linux版）
# 测试环境：Python3、deepin

import os

# 转换文件编码
def convert_file_encoding(source_file_path, source_encoding, target_file_path, target_encoding):
    lines = open(source_file_path, encoding=source_encoding).readlines()  # 打开文件，读入每一行
    print(source_file_path, "->" ,target_file_path)
    fp = open(target_file_path, 'w', encoding=target_encoding)  # 打开要写的文件

    for line in lines:  # 写入文件
        fp.write(line)

    fp.close()  # 关闭文件


#　转换目录下文件的编码
def convert_files_encoding(dir_path, new_dir_path, source_encoding, target_encoding, target_filename_extension):
    filelist = os.listdir(dir_path)  # 该文件夹下所有的文件（包括文件夹）
    for filename in filelist:  # 遍历所有文件
        file_path = os.path.join(dir_path, filename)  # 原来的文件路径
        if os.path.isdir(file_path):  # 如果是文件夹则跳过
            continue
        filename_extension = os.path.splitext(filename)[1]  # 获取文件扩展名
        if filename_extension != target_filename_extension:    # 只修改扩展名为 target_filename_extension 的文件，避免读取图片等二进制文件而导致的出错
            continue
        new_file_path = os.path.join(new_dir_path, filename)    # 新文件路径
        convert_file_encoding(file_path, source_encoding, new_file_path, target_encoding)    # 转换文件编码



if __name__ == '__main__':
    target_filename_extension=".csv"    #要转码文件的扩展名
    source_encoding='gbk'   #原来的编码
    target_encoding='utf-8' #要转换成的编码
    print("将", target_filename_extension, "文件编码从", source_encoding, "转换为", target_encoding)
    dir_path = input("输入源文件夹路径：")
    new_dir_path = input("输入新文件夹路径：") 

    convert_files_encoding(dir_path, new_dir_path, source_encoding, target_encoding, target_filename_extension)
