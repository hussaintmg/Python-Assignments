#Write a code to separate strings, numbers and Boolean data from the above list into separate lists.
List = [“Tahir”, 44, “AI and Data Science”, True]
List_str=[]
List_num=[]
List_bool=[]
for items in List:
  if type(item)==str:
    List_str.append(item)
  elif type(item)==int:
    List_num.append(item)
  else:
    List_bool.append(item)
print(f"Strings List '{List_str}'")
print(f"Numbers List '{List_num}'")
print(f"Booleans List '{List_bool}'")
