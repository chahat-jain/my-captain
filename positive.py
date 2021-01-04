# code to print positive Numbers in a range 
def positive(L):
    for x in L: 
        # checking condition 
        if x >= 0: 
           print(x, end = " ") 

# list of numbers 
list1 = [12, -7, 5, 64, -14] 
positive(list1)
print()
list2 = [12, 14, -95, 3]
positive(list2)
