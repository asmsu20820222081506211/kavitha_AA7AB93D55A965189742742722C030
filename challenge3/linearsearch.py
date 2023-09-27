def linear_search_product(productlist,target):
  list=[]
  for index,product in enumerate(productlist):
    if product==target:
      list.append(index)
  return list
productlist=["rice","nuts","dals","fruits","vegetable","rice"]
product="rice"
print("\nproduct "+product+" is fount at indices: ")
print(linear_search_product(productlist,product))