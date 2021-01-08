string = input("enter your string")
length= len(string)
def change(string,length):
    if string[0]== 'a' and string[length-1] == 'd':
        string1 = "mango"
        print(string)
    elif 'o' in string  or 'u' in string:
        print(string.upper())
    elif 'i' in string and 'f' in string:
        print(string.title())
    else:
        print("not exist")

print(change(string,length))
