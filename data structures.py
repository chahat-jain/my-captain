
# TASK 1
import math
r = float(input("enter radius:"))
A= (math.pi)*r*r
print("Area of the circle is:",A)

#============================================
# TASK 2
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
