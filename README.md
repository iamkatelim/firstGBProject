# EKT 221 DATA STRUCTURE AND ALGORITHM

**ASSIGNMENT 2**


## Introductions
**MEMBERS** =
 - LIM MAY YANN 171020907 <br />
 
**PROGRAM** = RK20 - COMPUTER ENGINEERING<br />
**LANGUAGE = PYTHON 2.7.13<br />**





## Installation Python in Windows: 

	*Setting the PATH variable
	*After you have the program operating correctly, then you can execute it by double-clicking on the program's icon.
	
	*Open a command window
	
	*type 'python'
	
	*If you see
		"Python 2.4.3 (#1, May 18 2006, 07:40:45) 
		Type "help", "copyright", "credits" or "license" for more information.
		>>>" 
	Then your computer is ready to use Python 
	
	*If you see the message
		"'python' is not recognized as an internal or external command, operable program or batch file."

	 Set Python(e.g., C:\Python24) to your system PATH that folder name is the path to Python.

## Running the test

	*To run .py file in command prompt

	*Navigate to where your python file is, using the commands 'cd' (change directory) and 'dir' (to show files in the directory, to verify your head).

	*Type 'python first.py' to execute and run.


## Functionality

### Create default node

A tree node contains three attributes which is:
•	Left node
•	Right node
•	Node’s data



* To create the first and top node ‘4’, use code below. When you create a node, both left and right node equal to None.		 


* To create the child of the node, use code below. The left link points to a BST for items with smaller keys, and the right link points to a BST for items with larger keys.
  
 
### Inorder traversal

* In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal s reversed can be used.

* Method: Left -> Root -> Right


### Preorder traversal

* Preorder traversal is used to create a copy of the tree. Preorder traversal is also used to get prefix expression on of an expression tree.

* Method: Root -> Left ->Right



### Postorder traversal

* Postorder traversal is used to delete the tree. Please see the question for deletion of tree for details. Postorder traversal is also useful to get the postfix expression of an expression tree.

* Method: Left ->Right -> Root


### Search largest node

* The left link points to a BST for items with smaller keys, and the right link points to a BST for items with larger keys. To find the largest node in binary search tree, traverse the node from root to right recursively until right is NULL. The node whose right is NULL is the node with maximum value.:


### Search smallest node

* The left link points to a BST for items with smaller keys, and the right link points to a BST for items with larger keys. To find the smallest node in binary search tree, traverse the node from root to left recursively until left is NULL. The node whose left is NULL is the node with minimum value.


 
### Delete node

There are 3 cases that need to be considered while deleting a node from Binary Search Tree.
 
1.	Node to delete has no children that is no left child and no right child present. 
 Case 1 in below image. 
2.	Node to delete has only one child either left child or right child present. Case 2 in below image.
3.	 Node to delete has both child that is left child and right child present. Case 3 in below image.
 
Case 1:
 For case 1, it is very much straightforward, 

1.	Search for the node that need to be deleted.
2.	 Node to be deleted is either on left side or on right side of its parent node.
3.	If node to be deleted is on left side of its parent node then mark Left side of parent node to null.
 Eg: parent.setLeft(null);
4.	If node to be deleted is on right side of its parent node then mark Right side of parent node 
 to null. Eg: parent.setRight(null);
 


Case 2:
 For case 2, it is very much straightforward, 
1.	Search for the node that need to be deleted.
2.	Node to be deleted is either on left side or on right side of its parent node.
3.	Node to be deleted has only child present that can be on left side or right side.
4.	If node to be deleted has left child present, 
 then directly connect its parent node to left child node of node to be deleted. 
 Eg: parent.setLeft(child.getLeft());
5.	If node to be deleted has right child present, 
 then directly connect its parent node to right child node of node to be deleted. 
 Eg: parent.setRight(child.getRight());
6.	In this way node to be deleted will be removed from the Tree and parent node 
 will be directly connected to child node of node to be deleted.
 
Case 3:
 For case 3, it is little bit tricky
1.	Search for the node that need to be deleted. 
2.	Now, instead of deleting the node, we will replace the data of node to be deleted 
 with the data that will be best fit in that place.
3.	Which data will be best fit? Search the data from the sub tree of node to be deleted and 
 find the node whose data when placed at the place of node to be deleted will 
 keep the Binary Search Tree property(key in each node must be greater 
 than all keys stored in the left sub-tree, and smaller than all keys in right sub-tree) intact.

4.	Find minimum element from the right sub tree of node to be deleted or 
 find maximum element from the left sub tree of node to be deleted and
 copy that Node data to the data of node to be deleted.
5.	Delete the node which we found the best fit in step 5.



### Size of tree

Size of a tree is the number of elements present in the tree. The function recursively calculates the size of a tree. It works as follows:
•	Size of a tree = Size of left subtree + 1 + Size of right subtree.

 



### Delete tree

To delete tree, for loop is used to check is the tree is empty. If the tree is not empty, deleteNode() function is perform until the tree is empty.

 

