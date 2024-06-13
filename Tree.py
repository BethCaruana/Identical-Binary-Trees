"""
Tree class has three member variables:
    root    holds the root Node of the tree

    stack   used to hold traversed nodes
    
    queue   aids in adding new nodes

There are three methods:
    push_root()             pushes the root node to the stack
    
    insertNode(text)        inserts new nodes into the tree by level

    preOrder()              performs pre-order traversal

    comparison(tree1,tree2) takes two trees, uses coroutines to stop
                            pre-order traversal after each element
                            and evaluates for equivalence
                            
    build_tree(file_name)   take a file name and parses information
                            into nodes of a tree
"""

#import Node class
from Node import Node

#import queue
import queue

class Tree:
    #initializing constructor
    def __init__(this):
        this.root = None
        this.read_stack = []
        this.queue = queue.Queue()

    #pushes root to stack
    def push_root(this):
        this.read_stack.append(this.root)


    #insert new node into the tree
    def insertNode(this,text):
        #if root empty, assign node
        if this.root == None:
            this.root = Node(text,None,None)
            #put a root for left and right node assignment
            this.queue.put(this.root)
            this.queue.put(this.root)
        else:
           #while queue is not empty
            while not this.queue.empty():
                #pop top node
                temp = this.queue.get()
                #if left node is empty
                if temp.getLeft() == None:
                    #insert new node in left
                    temp.left = Node(text,None,None)
                    #put left node on queue for left and right assignment
                    this.queue.put(temp.left)
                    this.queue.put(temp.left)
                    break
                #if right node is empty
                if temp.getRight() == None:
                    #insert new node in right
                    temp.right = Node(text,None,None)
                    #put right node on queue for left and right assignment
                    this.queue.put(temp.right)
                    this.queue.put(temp.right)
                    break
                    
    #pre-order evaluates parent node first, left node second, then right node
    def preOrder(this):
        #check if stack is not empty
        if len(this.read_stack) != 0:
            #pop top element
            node = this.read_stack.pop()
            #check if left node is None
            if node.left != None:
                #if Node is present, add to stack
                this.read_stack.append(node.left)
            #check if right node is None
            if node.right != None:
                #if Node is present, add to stack
                this.read_stack.append(node.right)
            #returns node value to the next() function in comparison()
            yield node.getValue()
        #if stack is empty yield None
        else:
            yield None
            
    #checks for equivalent values in two trees
    def comparison(this,tree1,tree2):
        #set boolean to true
        same = True
        #while loop stops when values are not equivalent
        #or both values are None
        while same:
            #create coroutines for each tree traversal
            tree_one = tree1.preOrder()
            tree_two = tree2.preOrder()
            #store node values recieved from yield in preOrder()
            value1 = next(tree_one)
            value2 = next(tree_two)
            #if values are equal continue while loop
            if(value1==value2):
                same = True
                #if traversals of both trees are done stop loop
                if(value1==None):
                    print("They're equivalent")
                    same = False
            #if values are not the same stop loop
            else:
                print("%s is not equal to %s" % (value1,value2))
                print("They're not equal")
                same = False

    #reads file and inserts node based on each line
    def build_tree(this,file_name):
        with open(file_name, 'r') as file:
            for line in file:
                this.insertNode(line)


if __name__ == "__main__":

#create two trees
   tree1 = Tree()
   tree2 = Tree()

#build the trees from the files
   tree1.build_tree("tree1_example.txt")
   tree2.build_tree("tree2_example.txt")

#push root to the preOrder stack
   tree1.push_root()
   tree2.push_root()

#compare the trees
   tree1.comparison(tree1,tree2)
