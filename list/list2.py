def remove_element(list,n):
  return [x for x in list if x != n]

print(remove_element([1, 2, 3, 4, 5],2))