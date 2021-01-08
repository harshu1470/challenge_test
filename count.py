string = input("enter your string\n")
count = []
for i in string:
    if i in count:
        count[i] += 1
    else:
        count = 1

