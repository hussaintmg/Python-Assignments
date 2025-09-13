#Create a list [32,54,66,11,77,10,90]
list=[32,54,66,11,77,10,90]

#a.	Remove items from the list with values less than 20.
for  num in list:
  if num<25:
    list.pop(num)

#b.	Sort the list in ascending and descending order.
list.sort()
list.sort(reverse=True)

#c.	Now, compute the average value of the list items.
average = sum(list) / len(list)

print("Average value:", average)

