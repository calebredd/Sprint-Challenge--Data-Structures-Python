import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None #Other Binary Search Trees
        self.right = None #Other Binary Search Trees

    # Insert the given value into the tree
    def insert(self, value):
    #Thought behind tracking to end position:
        if self.value:
            if self.value > value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)
        else:
            self.value = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Does the current value exist
        if self.value:
            # Compare current value to the target
            if self.value == target:
                return True
            # If target is less than current value  
            if self.value > target:
            # if left value exists check left
                if self.left:
                    return self.left.contains(target)
                # If left value doesn't exist Else Return False
                else: return False

            # If target is greater than current value 
            else:
            # if right value exists check right
                if self.right:
                    return self.right.contains(target)
                # If right value doesn't exist Else Return False
                else: return False
        # Return False
        else:
            return False

i = 0
for name_1 in names_1:
    if (i == 0):
        searchTree = BSTNode(name_1)
        i +=1
    else:
        searchTree.insert(name_1)
for name_2 in names_2:
    if (searchTree.contains(name_2) ):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
