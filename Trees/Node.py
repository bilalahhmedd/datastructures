# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:10:40 2019

@author: bilal
"""

class Node:
    
    # constructor of node
    def __init__ (self,value=None,parent=None, left_child = None, right_child=None,depth=0,height=0,bal_factor=0):
        self.parent = parent;
        self.left_child = left_child;
        self.right_child = right_child;
        self.value = value;
        self.depth = depth;
        self.height = height;
        self.balance_factor = bal_factor
    # setters getters for value of Node 
    def get_value(self):
        return self.value
    def set_value(self,value):
        self.value=value
    # setters and getter for parent
    def get_parent(self): 
        return self.parent;
    def set_parent(self,parent):
        self.parent = parent;
    
    # setters and getter for left_child and right_child
    
    def set_left_child(self,left_child): 
        self.left_child = left_child;
    def get_left_child(self): 
        return self.left_child;
    def set_right_child(self,right_child): 
        self.right_child=right_child;
    def get_right_child(self): return self.right_child;
    
    # to check if node has child nodes or parent node
    def has_left_child(self): return self.get_left_child() is not None;
    def has_right_child(self): return self.get_right_child() is not None;
    def has_parent(self): return self.get_parent() is not None;
    
    # to check if node is leaf
    def is_leaf(self):
        return ((self.get_left_child() is None) and (self.get_right_child() is None))
    # setters getter for depth
    def set_depth(self,depth):
        self.depth = depth;
    
    def get_depth(self):
        return self.depth;
    # setter getters for height
    def set_height(self,height):
        self.height= height;
    def get_height(self):
        return self.height;
    
    # setter getter for balance factor
    
    def set_balance_factor(self,bal_factor):
        self.balance_factor=bal_factor;
    def get_balance_factor(self):
        return self.balance_factor;
    def calculate_balance_factor(self):
        if self.is_leaf():
            self.balance_factor=0;
        elif self.get_left_child() is not None and self.get_right_child() is not None:
            return (self.get_left_child().get_height() - self.get_right_child().get_height())
        elif self.get_left_child() is not None:
            return self.get_left_child().get_height();
        else:
            return (0 - self.get_right_child().get_heihgt());  
    def calculate_height(self):
        if self.is_leaf():
            return 0
        elif self.get_left_child() is not None and self.get_right_child() is not None:
            return 1+max(self.get_left_child().calculate_height(),self.get_right_child().calculate_height())
        elif self.get_left_child() is None:
            return 1 + self.get_right_child().calculate_height()
        else:
            return 1 + self.get_left_child().calculate_height()
        
        
    #     
    # let's over load some operators in Node
    def __add__(self,other):
        return Node(self.get_value()+other.get_value())
    def __eq__(self,other):
        return (self.get_value() == other.get_value())
    def __gt__(self,other):
        return self.get_value() > other.get_value()
    def __st__(self,other):
        return self.get_value() < other.get_value()
    