# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/python3

class BindTreeNode():
    def __init__(self,data,right,left):
        self.data = data
        self.right = right
        self.left = left

class BindTree():
    def __init__(self):
        self.root = None
    
    def markTree(self,data,left,right):
        pass