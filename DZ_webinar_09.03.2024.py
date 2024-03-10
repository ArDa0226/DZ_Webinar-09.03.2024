

my_list = [0, 0, 1, 2, 1, 3, 4, 2, 1, 5, "string", "string", 2, 2]

def unik_elem(my_list):
    new_list = []
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

print(unik_elem(my_list))

def unik_elem_2(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unik_elem_2(my_list))