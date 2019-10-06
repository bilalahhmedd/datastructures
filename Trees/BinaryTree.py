# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:26:55 2019

@author: bilal
"""

import queue
from AbstractTree import AbstractTree

class BinaryTree(AbstractTree):
    
    def __init__(self,root=None):
        self.root=root;
        if self.root is not None:
            self.size=1
        else:
            self.size=0
    
    def get_root(self):
        return self.root;
    def set_root(self,root):
        self.root= root;
        
    #to add node into binary tree
    #we will use recursive approach
    # if pnode null make node that pnode
    # else pass to childern node
    
    def _add_node(self,pnode,node):
        if pnode is None:
            if pnode is self.get_root():
                self.set_root(node);
            else:
                self.pnode=node;
        elif (pnode.get_value() > node.get_value()):
            if pnode.get_left_child() is None:
                pnode.set_left_child(node);
                node.set_parent(pnode);
            else:
                self._add_node(pnode.get_left_child(),node);
        else:
            if pnode.get_right_child() is None:
                pnode.set_right_child(node);
                node.set_parent(pnode)
            else:
                self._add_node(pnode.get_right_child(),node);
    # use insert_node to insert node at top of binary tree            
    def add_node(self,node):
        pnode = self.get_root();
        self._add_node(pnode,node);
        self.size = self.size+1;
    def remove_node(self,node_value):
        print("value will be removed"+str(node_value)+"   ");
    def traverse(self,algo="dfs"):
        if(algo == "dfs"):
            self.dfs_trav();
        else:
            print("Invalid algo selected")  
    def get_height(self):
        self.calculate_height(self.get_root());
    def calculate_height(self,node):
        if node is None:
            return 0;
        if node.is_leaf():
            return 0;
        else:
            return (1 + max(self.calculate_height(node.get_left_child()),self.calculate_height(node.get_right_child())))
        
    def get_size(self):
        return self.size;
    
    def is_empty(self):
        return self.get_root() is None
    
#<---------------------------------------------------------count leaf nodes in tree -------------------------------------------->

    def count_leaf_nodes(self,algo='recursion'):
        if(algo == 'recursion'):
            self.count_leafnodes_rec(self.get_root());            
        elif(algo == 'stack'):
            self._count_leafnodes_stack(self.get_root());
    def count_leafnodes_rec(self,node):
        if(node is None):
            return 0;
        elif(node.is_leaf()):
            return 1;
        else:
            return self.count_leafnodes_rec(node.get_left_child()) + self.count_leafnodes_rec(node.get_right_child());
    def _count_leafnodes_stack(self,node):
        pass
        
    
#<---------------------------------------------------------traversal of binary tree -------------------------------------------->    
# depth first traversal using resurive approach
    def dfs_trav(self):
        if self.get_root() is not None:
            self._dfs_trav(self.root);
        else :
            print("Tree is empty")
    def _dfs_trav(self,node):
        if node is not None:
            value = str(node.get_value());
            print(" ---> "+value+" ");
        if node.get_left_child() is not None:
            self._dfs_trav(node.get_left_child());
        if node.get_right_child() is not None:
            self._dfs_trav(node.get_right_child());
        return None;    
    
# breadth first traversal using recursive approach

    # making bfs private as it keeps system busy
    # we will fix it later
    def _bfs_trav(self,size):
        q = queue.Queue(size)
        if self.get_root() is not None:
            q.put(self.get_root());
            while(q.not_empty):
                node = q.get_nowait()
                if node.get_left_child() is not None:
                    q.put_nowait(node.get_left_child());
                if node.get_right_child() is not None:
                    q.put_nowait(node.get_right_child());
                print("--->"+str(node.get_value())+"  ")
        else:
            print("Tree is empty");
# <-------------------------------------------pre order traversal -------------------------->  
# <--------------------process root, left subtree and then right subtree-------------------->
    def preorder_trav_stack(self):
        lst = []
        if self.get_root() is not None:
            lst.append(self.get_root());
            while (len(lst) > 0):
                node = lst.pop();
                val=str(node.get_value());
                print("--->"+val+"   ");
                if(node.get_right_child() is not None):
                    lst.append(node.get_right_child());
                if(node.get_left_child() is not None):
                    lst.append(node.get_left_child());
        else:
            print("Tree is empty")

# <-------------------------------------------in order traversal -------------------------->  
# <--------------------process in sequence of left, root, right subtree-------------------->

    def inorder_trav_rec(self):
        if self.get_root() is None:
            print("Tree is empty")
        else:
            self._inorder_trav_rec(self.get_root());
    
    
    def _inorder_trav_rec(self,node):
        if(node is None):
            return;
        self._inorder_trav_rec(node.get_left_child());
        print("--->"+str(node.get_value())+"  ");
        self._inorder_trav_rec(node.get_right_child());
        
    def postorder_trav_rec(self):
        if self.get_root() is None:
            print("Tree is empty")
        else:
            self._postorder_trav_rec(self.get_root())
            
    def _postorder_trav_rec(self,node):
        if(node is None):
            return
        self._postorder_trav_rec(node.get_left_child());
        self._postorder_trav_rec(node.get_right_child());
        print("--->"+str(node.get_value())+"   ");
# <--------------------------------------------------Extra functions to be used in AVL tree Data Strucutres------------------------------------------------>
    def update_ancestors_height(self,parent,value=1):
        if parent is None:
            return
        else:
            val=parent.get_height()
            parent.set_height(val+value)
            self.update_ancestors_height(parent.get_parent(),value)
    
    def update_ancestors_bf(self,parent,child):
        if parent is None:
            return
        elif parent.get_right_child() is not None and parent.get_right_child() == child:
            parent.set_balance_factor(parent.get_balance_factor()-1)
            self.update_ancestors_bf(parent.get_parent(),parent)
        elif parent.get_left_child() is not None and parent.get_left_child() == child:
            parent.set_balance_factor(parent.get_balance_factor()+1)
            self.update_ancestors_bf(parent.get_parent(),parent)
        
    def search_node(self,node):
        return self._serch_node(self.get_root(),node);
    # search for given node in Tree
    # let's search for given node in tree
    
    def _serch_node(self,snode,node):
        if snode is None:
            return
        elif (snode==node):
            return snode
        elif(snode.get_value() > node.get_value()):
            return self._serch_node(snode.get_left_child(),node)
        else:
            return self._serch_node(snode.get_right_child(),node)
        
    def find_root_path(self,node):
        lst = []
        while (node is not None):
            lst.append(node);
            node = node.get_parent();
        return lst
        
        
            
        
    