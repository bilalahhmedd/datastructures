# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:57:08 2019

@author: bilal
"""
from Node import Node
from AbstractTree import AbstractTree;
from BinaryTree import BinaryTree;

class AVLTree(BinaryTree):
    
    def __init__(self,root=None):
        self.root=root;
        if(self.root is None):
            self.size=0
        else:
            self.size=1
    
    def insert_node(self,node):
        self._insrt_node(self.get_root(),node)
    
    def _insrt_node(self,pnode,node):
        if pnode is None:
            if pnode is self.get_root():
                self.set_root(node);
            else:
                self.pnode=node;
        elif (pnode.get_value() > node.get_value()):
            # to be added here
            if pnode.is_leaf():
                pnode.set_left_child(node);
                node.set_parent(pnode);
                # update ancesters of this new child node
                # update heights of all ancestors
                # updae balance_factor of all ancestors
                self.update_ancestors_height(pnode)
                self.update_ancestors_bf(pnode,node)
                
                
                
                
            elif pnode.get_left_child() is None:
                # adding node does not effect height of ancestors
                pnode.set_left_child(node);
                node.set_parent(pnode);
                # but it affects balance factor of parent node
                # so update balance factor of parent node
                pnode.set_balance_factor(pnode.get_balance_factor()+1)
            else:
                self._insrt_node(pnode.get_left_child(),node);
        else:
            if pnode.is_leaf():
                pnode.set_right_child(node);
                node.set_parent(pnode);
                # update ancesters of this new child node
                # update heights of all ancestors
                # updae balance_factor of all ancestors
                self.update_ancestors_height(pnode)
                self.update_ancestors_bf(pnode,node)
                
                # now trace all ancestors upto root and see if any node is unbalanced
                # if node is unbalanced then make it balanced
            elif pnode.get_right_child() is None:
                pnode.set_right_child(node);
                node.set_parent(pnode)
                # update balane factor of pnode
                pnode.set_balance_factor(pnode.get_balance_factor()-1)
            else:
                self._insrt_node(pnode.get_right_child(),node);
                # recursively call _insert method on same node again
                
            
            
    def balance_tree(self):
        # write code to self balance tree 
        # we can balance tree at time of insertion node into tree
        # or we can 
        pass
    def left_rotate(self):
        
        pass
    
    def right_rotate(self):
        pass