#### Problem 1 ####

L = [1,2,3,4,5]

sum = 0 
for i in L :
    sum += i    #O(n)
print(sum)

product = 1
for i in L:
    product *= i    #O(n)
print(product)

#The complexity will be O(n) + O(n) = O(n+n = 2n => n)


#### Problem 2 ####

L = [1,2,3,4,5]

for i in L:
    for j in L:
        print('{}{}'.format(i,j)) 

# The complexity will be O(n^2)


#### Problem 3 ####

#Linear search O(n)

#