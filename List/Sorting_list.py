lst = [1,82,39,47,45,9,7]
temp = lst[0]
for i in range(len(lst)):
   for j in range(len(lst)-1-i):
     if lst[j] < lst[j+1]:
         lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("List in descending order: ",lst)
