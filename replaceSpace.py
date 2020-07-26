# LeetCode
# replaceSpace 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

def replaceSpace(oldStr:str):
    new = ''
    for each in oldStr:
        if each == ' ':
            new += '%20'
        else:
            new += each
    print(new)


replaceSpace('We are happy')