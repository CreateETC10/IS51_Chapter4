# def get_number():
#     return 5
# def set_number(num):
#     number=num
#     print("From set_number, num is:",str(num))
#     return number
# num=get_number()
# set_number(6)
# print("End of program. Num is:", str(num))


# def add_number(num1, num2):
#     print("num1:",str(num1))
#     print("num2:", str(num2))
#     val=num1+num2
#     print("From add_number, val is:", str(val))
#     return val
# output=add_number(2,5)#7
# print("Output of {} and {} is {}.".format(str(2), str(5), output))


def get_firstname(full_name):  # Joseph Greene
    space = full_name.index(" ")
    first_name = full_name[:space]
    return first_name


my_name = get_firstname("Joseph Greene")
print("Hello, my name is " + my_name + ".")
names = ["Lucas Phan", "Joseph Greene", "Joe Biden",
         "Mike Tyson", "Tom Brady", "Koby Bryant"]
for name in names:
    my_name = get_firstname(name)
    print("Hello, my name is " + my_name + ".")
    if my_name == "Tom":
        print(name+" plays football")
    elif my_name == "Koby":
        print(my_name+" plays basketball")
    else:
        print(my_name+" is not into sports")
