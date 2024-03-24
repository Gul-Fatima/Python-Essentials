import math
lst = [1,82,39,47,45,9,7]
x = math.ceil(len(lst)/2)-1
# (a)An expression that evaluates to the index of the middle element of lst
print("Index of the middle element of lst: ",x)
# (b)An expression that evaluates to the middle element of lst
print("Middle element of lst: ",lst[x])
# (c)A statement that sorts the list lst in descending order
temp = lst[0]
for i in range(len(lst)):
   for j in range(len(lst)-1-i):
     if lst[j] < lst[j+1]:
         lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("List in descending order: ",lst)
# (d)A statement that removes the ﬁrst number of list lst and puts it at the end
first_no = lst[0]
lst.remove(first_no)
lst.append(first_no)
print(lst)
