# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:47:28 2019

@author: bilal
"""

# we need to give abstract definition of tree
# out abstract tree will contain following functions
# add_node, remove_node, search_node, 
# traverse_node
# get depth
# get height
# is empty
# 
from abc import ABC, abstractmethod
class AbstractTree(ABC):

    def __init__(self,root=None):
        pass
    @abstractmethod
    def get_root(self):
        pass
    @abstractmethod
    def set_root(self):
        pass
    @abstractmethod
    def is_empty(self):
        pass
    @abstractmethod
    def add_node(self,node):
        pass
    @abstractmethod
    def remove_node(self,node_value):
        pass
    @abstractmethod
    def traverse(self,algo=None):
        pass
    @abstractmethod
    def get_size(self):
        pass
    @abstractmethod
    def get_height(self):
        pass