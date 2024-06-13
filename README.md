# Coroutines

# How to run the program
Type python3 Tree.py in the command line. 

# How to add your own tree to test
In a separate .txt file you will put the strings you want in your tree on separate lines. The order you place them in determines where they go in the tree.
Each tree will have its own file. The node insertion is level based.

```
Ex:
house     (root)
dog       (root.left)
pool      (root.right)
lake      (root.left.left)
porch     (root.left.right)
cat       (root.right.left)
.
.
etc.
```

I have three example files included (tree1_example.txt, etc.) for testing and as a guide for format. To run your own example file, go to the main function of Tree.py and insert the names of your files in tree.build_tree("file_name".txt).

# Identical-Binary-Trees
