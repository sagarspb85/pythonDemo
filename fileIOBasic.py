# File Io Basic

f = open("sagar.txt","rt")

print(f.readline())
print(f.readline())
# content = f.read()
# print("========",content )

# for line in f :
#     print(line,end="")



f.close()

# Appending
# w remove exsesting data & add new
# a Append data
# r+ read & write withour loss data
af = open("sagar.txt","r+")
af.write("sagar appending demo \n")

af.close()