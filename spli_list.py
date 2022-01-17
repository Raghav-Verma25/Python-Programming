"""split the list in to it middle"""
a_list=[1,2,3,5,7,8]
length = len(a_list)
middle_index = length//2
first_half = (a_list)[:middle_index]

print(first_half)

second_half = (a_list)[middle_index:]



print(second_half)
