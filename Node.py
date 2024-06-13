"""
Node class has three member variables: 
    value   value at the Node
    right   right Node
    left    left Node

Member functions are just setters and getters
for each variable

"""

class Node:
    def __init__(this, value, right, left):
        this.value = value
        this.right = right
        this.left = left

    def setValue(this,value):
        this.value = value

    def setRight(this,right):
        this.right = right

    def setLeft(this,left):
        this.left = left

    def getValue(this):
        return this.value;

    def getRight(this):
        return this.right;

    def getLeft(this):
        return this.left;
