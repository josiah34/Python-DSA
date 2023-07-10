## Code for Big O Notation



### O(n) 



# def print_items(n):
#     for i in range(n):
#         print(i)


## Ran n operations
# print_items(10)



## Drop constants 


def print_items_drop(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)
        
# Ran two of n times        (n+n)
# This would not be written as O(2n) but rather O(n)
# We drop the constant
# print_items_drop(10)


# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
            

# Ran n^2 times
# The inner loop runs n times for every iteration of the outer loop
# N * N = N^2
# O (n^2)

# print_items(20)



## Drop non-dominant terms

def print_items(n):
    ## These two loops are O(n^2)
    for i in range(n):
        for j in range(n):
            print(i,j)
    ## This loop is O(n)
    for k in range(n):
        print(k)

## The loop on the outside of of O(n) is the non-dominant term and is dropped
## So O(n^2 + n) becomes O(n^2)
# print_items(20)


## O(1) - Constant Time

# def add_items(n):
#     return n + n + n

## This function will always run 3 operations no matter the size of n. So it is O(1). The value of n does not create any more operations. 
# print(add_items(10))

## This is the most efficient Big O notation. It is constant time.



### Terms

# Loop within a Loop - O(n^2)

# Proportional - O(n)

# Divide and Conquer - O(log n)

# Constant - O(1)