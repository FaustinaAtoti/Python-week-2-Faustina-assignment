# 1
my_list =[]
print("empty list:",my_list) 
# 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("new list:",my_list)

# 3
my_list.insert(1,15)
print(my_list)

# 4
list_two = [50,60,70]
my_list.extend(list_two)
print(my_list)

# 5
my_list.remove(70)
print(my_list)

# 6
sorted(my_list) 
print(my_list)

# 7
index = my_list.index(30)
print("index of 30:",index)
