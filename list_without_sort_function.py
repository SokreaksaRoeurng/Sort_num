
my_list = [2,4,6,8,7,9,3,1,5]
for i in range (len(my_list)):
    for j in range ( i+1, len(my_list)):

        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)
