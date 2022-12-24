#define a function
def draw_tree(tree_height):
#Define parameters of function

#Loop
#The outer loop(each row of the tree)
  for i in range(tree_height):
#Inner loop
#printing an * for each column.
    for j in range(i+1):
      print("*", end="")
    print()

tree_height = int(input("Enter the height of the tree: "))
draw_tree(tree_height)