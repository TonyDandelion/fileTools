# coding: utf-8
import os, os.path, shutil
import numpy as np
import random
import re
s = os.sep

'''
Author: Yan Weiran
Date: 2018-10-18
Description: Python tools function
'''

'''
将文件夹下的文件按照前缀分类的文件
argus: process_folder_path: 待处理文件夹的路径 ./test
       start: 开始文件标号 1
       stop: 结束文件标号 4 
       表示处理./test文件夹下1 2 3 4文件夹中的图片文件
return: none
'''
def YWR_seprateFiles(identity):
    for index in range(start, stop+1):
        depth_count = color_count = ir_count = 0

        all_files = []
        # 先处理sdk采集的数据 一个文件夹一个文件夹的处理
        for root, sub_dirs, files in os.walk(process_folder_path):
            all_files = files + all_files

        print len(all_files)

        if not os.path.exists(process_folder_path + 'color'):
            os.mkdir(process_folder_path + 'color')

        if not os.path.exists(process_folder_path + 'ir'):
            os.mkdir(process_folder_path + 'ir')

        if not os.path.exists(process_folder_path + 'depth'):
            os.mkdir(process_folder_path + 'depth')

        for single_file in all_files:
            prefix = single_file.split("_")[0]
            if prefix == "color":
                color_count = color_count + 1                
                shutil.move(process_folder_path + single_file, process_folder_path + "color/" + single_file)
            if prefix == "depth":
                depth_count = depth_count + 1
                shutil.move(process_folder_path + single_file, process_folder_path + "depth/" + single_file)
            if prefix == "ir":
                ir_count = ir_count + 1
                shutil.move(process_folder_path + single_file, process_folder_path + "ir/" + single_file)

        print "the number of color pictures is {}.".format(color_count)
        print "the number of depth pictures is {}.".format(depth_count)
        print "the number of id pictures is {}.".format(ir_count)


'''
在指定范围生成指定数量的不重复的随机数的函数
:parame range_start: 指定范围开始
        range_stop: 指定范围结束
        count: 指定数量
:return result: 指定数量不重复随机数的list
'''
def YWR_generateRandom(range_start, range_stop, count):
    result = []
    while len(result)!=count:
        result.append(random.randint(range_start, range_stop))
        result = list(set(result))
    return result


'''
扫描当前文件夹下指定后缀postfix的文件或指定前缀prefix的文件
'''
def YWR_scanFiles(directory, prefix=None, postfix=None):
    files_list=[]
    
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root,special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root,special_file))
            else:
                files_list.append(os.path.join(root,special_file))
                          
    return files_list


'''
检测当前文件夹下面有多少文件 多少identities的函数 具体判断图片属于哪一个identity的方法有异
:parame file_root: 文件的路径
:return files: 以dict形式整理好的所有文件
'''
def YWR_showFiles(file_root):
    identities = []

    all_files = os.listdir(file_root)
    for i,v in enumerate(all_files):
        identities.append(v.split('_')[0])  # 注意修改具体判断图片属于哪一个identity的方法

    print "identities"    
    identities = list(set(identities))
    print len(identities)
    print "files"
    print len(all_files)
    print "*" * 50
    # raw_input()

    # 组织数据
    structure = {}
    count = 0
    for single_file in all_files:
        current_id = single_file.split('_')[0]  # 注意修改具体判断图片属于哪一个identity的方法
        if structure.has_key(current_id):
            structure[current_id].append(single_file)
        else:
            structure[current_id] = [single_file]
        count = count + 1

    print "structure"
    print len(structure)
    print "*" * 50

    return structure

