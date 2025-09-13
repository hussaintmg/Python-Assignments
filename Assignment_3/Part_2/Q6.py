#From the given list:
Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]
#a.	Create separate list of string and numbers
List_str=[]
List_num=[]
for items in Gadgets:
  if type(item)==str:
    List_str.append(item)
  else:
    List_num.append(item)

print("String List:", List_str)
print("Number List:", List_num)

#b.	Sort the string list in ascending and descending order
List_str.sort()
print("Ascending String List:", List_str)

List_str.sort(reverse=True)
print("Descending String List:", List_str)


#c.	Sort the string list by length of elements in the list
List_str.sort(key=len)
print("Sorted by length (ascending):", List_str)

List_str.sort(key=len, reverse=True)
print("Sorted by length (descending):", List_str)

#d.	Sort the numbers list in ascending and descending order
List_num.sort(key=len)
print("Ascending Numbers List:", List_num)

List_num.sort(key=len, reverse=True)
print("Descending Numbers List:", List_num)
