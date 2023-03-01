# LIST LOOP
list1 =["sagar","vishal","sumeet","vaibhav"]

list2 = [5,7,3]
if 7 in list2:
    print("Yeees")

#for item in list1:
  #  print(item)

# LIST OF LIST

list3 = [ ["sagar",1],
    ["vishal",56],
    ["sumeet",6],
    ["vaibhav",30]]

dict1 = dict(list3)
print(dict1)

for items in dict1: # print only name
     print(items)
"""
for items,sval in dict1.items(): # print name value
    print(items,sval)
"""
#for items,secondVal in list3:
    #print(items,secondVal)

""" find greater than 6"""
numbersItems = [int,float,"sagar",12,58,5,9,1,3,78,4,3,2,99,5,10]

for findNum in numbersItems:
    if str(findNum).isnumeric() and findNum>6:
        print(findNum)

