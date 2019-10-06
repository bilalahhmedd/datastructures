# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 19:09:43 2019

@author: bilal
"""

from Node import Node;
from BinaryTree import BinaryTree;
from AVLTree import AVLTree;




avl1 = AVLTree(Node(43));
avl1.insert_node(Node(9));
avl1.insert_node(Node(-1));
avl1.insert_node(Node(99))
avl1.insert_node(Node(-10))

avl1.insert_node(Node(-7))



avl1.insert_node(Node(-12))
avl1.insert_node(Node(-8))


avl1.traverse()


