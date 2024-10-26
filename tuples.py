variety_tuple = ("Computer", "Books", "Pens","Table", "Chair", 1, 2, 3, 4, 5)

#variety_tuple += ("Jacket",)
#print(variety_tuple)

variety_list = list(variety_tuple)
variety_list.append("Jacket")
variety_tuple = tuple(variety_list)
print(variety_tuple)