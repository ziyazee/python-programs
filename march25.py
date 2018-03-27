# # Python program to check if a binary tree is bst or not
#
# INT_MAX = 4294967296
# INT_MIN = -4294967296
#
#
# # A binary tree node
# class Node:
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# # Returns true if the given tree is a binary search tree
# # (efficient version)
# def isBST(node):
#     return (isBSTUtil(node, INT_MIN, INT_MAX,5))
#
#
# # Retusn true if the given tree is a BST and its values
# # >= min and <= max
# def isBSTUtil(node, mini, maxi,k):
#     # An empty tree is BST
#     if node is None:
#         return True
#     # if(k==3):
#     #     print()
#
#     # False if this node violates min/max constraint
#     print(k,":",node.data," =>",mini,"=",maxi)
#     if node.data < mini or node.data > maxi:
#         return False
#
#     # Otherwise check the subtrees recursively
#     # tightening the min or max constraint
#     return (isBSTUtil(node.left, mini, node.data - 1,4) and
#             isBSTUtil(node.right, node.data + 1, maxi,3))
#
#
# # Driver program to test above function
# root = Node(4)
# root.left = Node(1)
# root.right = Node(6)
# root.right.left = Node(5)
# root.right.right = Node(7)
# root.left.left = Node(0)
# root.left.right = Node(3)
#
# if (isBST(root)):
#     print("Is BST")
# else:
#     print("Not a BST")
#
# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
index=0
g=-1
k=0
aa=0
bb=0

n=[0,7,1,4,0,3,6,3]
for i in range(len(n)):
    if(bb<aa):

        bb+=n[g]
        print(i, ":bb", bb)
        g-=1

    else:
        aa+=n[k];
        print(i, ":aa=", aa)
        k+=1
        index += 1
#print(aa)
#print(bb)
if(aa!=bb):
    exit(0)

a=[]
b=[]
for i in range(len(n)):
    if(i<index):
        print("came",i)
        a.append(n[i])
    else:
        b.append(n[i])
print(a)
print(b)
for i in a:
    print(i, end=" ")
# print(index)
# for i in range(index):
#     a.append(n[i])
#
# print(a)
# index+=1
# print(index)
# for index in range(len(n)):
#     print(index)
#     b.append(n[index])
# print(b)