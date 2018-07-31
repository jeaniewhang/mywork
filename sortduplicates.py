# Declare variables
mylist = [1,3,5,7,2]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

# TODO: Sort 'myList' (Why do we sort first?)
mylist.sort()
# TODO: Loop through 'mylist' with a for-Loop
for ml in mylist:
    print(ml)

for index in range(len(mylist) - 1):
    print(index)
    print(mylist[index], mylist[index + 1])
    # TODO: Check if adjacent elements of 'mylist' are the same
    if mylist[index] == mylist[index + 1]:
        # TODO: if they are the same, set has_duplicates to True
        has_duplicates = True
        # TODO: Exit out of the for-loop (no need to check rest of list)
        break
print(has_duplicates) # Our outputs of the program
