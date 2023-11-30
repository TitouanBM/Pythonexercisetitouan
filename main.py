
# 7.4.2 Create python file main.py and import the module mod.
# In main.py run the psum() and pmultiply() functions from the module mod using any two numbers.


import mod
mod.psum(10,40)

mod.pmultiply(2,5)



# 7.4.3 In main.py, also import Python's built in module platform. Then list the functions and variables in the platform module using the dir() function.

import platform

fun1= dir(platform)
print ('list of the fucntions and variables : ')
for x in fun1:
    print(x)