class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

            # A utility function to do inorder tree traversal


# Inorder traversal
# Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Preorder traversal
# Root -> Left ->Right
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        inorder(root.right)


# Postorder traversal
# Left ->Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


# depth of tree
def minDepth(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    if root is None:
        return 0

    # Base Case : Leaf node.This acoounts for height = 1
    if root.left is None and root.right is None:
        return 1

    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return minDepth(root.right) + 1

    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1


# Computes the number of nodes in tree
def size(node):
    if node is None:
        return 0
    else:
        return size(node.left) + 1 + size(node.right)


def minValue(node):
    current = node

    # loop down to find the lefmost leaf
    while current.left is not None:
        current = current.left

    return current.val


def maxValue(node):
    current = node

    # loop down to find the lefmost leaf
    while current.right is not None:
        current = current.right

    return current.val


def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

        # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)

        # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif key > root.val:
        root.right = deleteNode(root.right, key)

        # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

            # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValue(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp)

    return root


# import os


def main(operation, data):
    print("\n\n--------------------------------------------------------------\n")
    r = Node(50)
    insert(r, Node(30))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(70))
    insert(r, Node(60))
    insert(r, Node(80))

    if data is not None:
        if operation == 'insert':
            print("%d Inserted" % data)
            inserted_node.append(data)
            inserted_node2 = map(str, inserted_node)
            for _ in inserted_node2:
                inserted_node3 = int(_)
                insert(r, Node(inserted_node3))
        elif operation == 'delete':
            print("%d Deleted" % data)
            deleted_node.append(data)
            deleted_node2 = map(str, deleted_node)
            for _ in deleted_node2:
                deleted_node3 = int(_)
                deleteNode(r, deleted_node3)
    elif data == 0:
        return

    # Print inoder traversal of the BST
    print("Inorder traversal of binary tree is: ")
    import time

    start = time.clock() * 1000
    inorder(r)
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    print("Preorder traversal of binary tree is: ")
    start = time.clock() * 1000
    preorder(r)
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    print("Postorder traversal of binary tree is: ")
    start = time.clock() * 1000
    postorder(r)
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    start = time.clock() * 1000
    print("\nSmallest value in Binary Search Tree is = %d" % (minValue(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    start = time.clock() * 1000
    print("\nLargest value in Binary Search Tree is = %d" % (maxValue(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n' % (end - start))

    start = time.clock() * 1000
    print("\nDepth of tree is %d" % (minDepth(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n' % (end - start))

    start = time.clock() * 1000
    print("\nSize of the tree is %d" % (size(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n' % (end - start))

    decision1 = input("\nOperations =\n1. Insert Node\n2. Delete Node\n3. Delete tree\n\nTesting = \n4. 10 Nodes\n5. "
                      "20 Nodes\n6. 30 Nodes\n\n7. Exit\nDecision = ")
    if decision1 == 1:
        insert_node1 = input("Enter node number = ")
        main('insert', insert_node1)
    elif decision1 == 2:
        delete_node1 = input("Enter node number = ")
        main('delete', delete_node1)
    elif decision1 == 3:
        if r is not None:
            for _ in inserted_node:
                deleteNode(r, _)
                print("deleting %d" % _)
        else:
            print("Tree deleted")
    elif decision1 == 4:
        testing_nodes(10)
    elif decision1 == 5:
        testing_nodes(20)
    elif decision1 == 6:
        testing_nodes(30)
    elif decision1 == 7:
        import sys
        sys.exit()


def testing_nodes(total):
    import random
    r = None
    x = 0
    for x in range(total):
        x += 1
        number = random.randint(1, 101)
        random_node.append(number)
        if x == 1:
            r = Node(number)
        else:
            insert(r, Node(number))

    print("Inorder traversal of binary tree is: ")
    import time

    start = time.clock() * 1000
    inorder(r)
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    print("Preorder traversal of binary tree is: ")
    start = time.clock() * 1000
    preorder(r)
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    print("Postorder traversal of binary tree is: ")
    start = time.clock() * 1000
    postorder(r)
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    start = time.clock() * 1000
    print("\nSmallest value in Binary Search Tree is = %d" % (minValue(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n\n' % (end - start))

    start = time.clock() * 1000
    print("\nLargest value in Binary Search Tree is = %d" % (maxValue(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n' % (end - start))

    start = time.clock() * 1000
    print("\nDepth of tree is %d" % (minDepth(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n' % (end - start))

    start = time.clock() * 1000
    print("\nSize of the tree is %d" % (size(r)))
    end = time.clock() * 1000
    print('time taken = %.6f ms\n' % (end - start))

    if total == 10:
        decision_random = input("\n1. 20 Nodes\n2. 30 Nodes\n3. Delete tree\n4. Back to main menu\nDecision = ")
        if decision_random == 1:
            testing_nodes(20)
        elif decision_random == 2:
            testing_nodes(30)
        elif decision_random == 3:
            start = time.clock() * 1000
            if r is not None:
                for _ in random_node:
                    deleteNode(r, _)
                    print("deleting %d" % _)
            end = time.clock() * 1000
            print('time taken = %.6f ms\n' % (end - start))
            main('none', 0)
        elif decision_random == 4:
            main('none', 0)
    elif total == 20:
        decision_random = input("\n1. 20 Nodes\n2. 30 Nodes\n3. Delete tree\n4. Back to main menu\nDecision = ")
        if decision_random == 1:
            testing_nodes(10)
        elif decision_random == 2:
            testing_nodes(30)
        elif decision_random == 3:
            start = time.clock() * 1000
            if r is not None:
                for _ in random_node:
                    deleteNode(r, _)
                    print("deleting %d" % _)
            end = time.clock() * 1000
            print('time taken = %.6f ms\n' % (end - start))
            main('none', 0)
        elif decision_random == 4:
            main('none', 0)
    elif total == 30:
        decision_random = input("\n1. 20 Nodes\n2. 30 Nodes\n3. Delete tree\n4. Back to main menu\nDecision = ")
        if decision_random == 1:
            testing_nodes(10)
        elif decision_random == 2:
            testing_nodes(20)
        elif decision_random == 3:
            start = time.clock() * 1000
            if r is not None:
                for _ in random_node:
                    deleteNode(r, _)
                    print("deleting %d" % _)
            end = time.clock() * 1000
            print('time taken = %.6f ms\n' % (end - start))
            main('none', 0)
        elif decision_random == 4:
            main('none', 0)


print("--------------------------------------------------------------\n")
print("LIM MAY YANN 171020907\nLEE RON SHENG 171020905\n")
print("Program = RK20 - Computer Engineering")
print("--------------------------------------------------------------\n\n\n")

# list for inserted node
deleted_node = []
inserted_node = []
random_node = []
main('none', 0)
