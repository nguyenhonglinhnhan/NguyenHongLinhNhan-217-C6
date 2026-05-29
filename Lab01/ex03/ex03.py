def taoTupleTuList(list):
  return tuple(list)

inputList = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputList.split(",")))

myTuple = taoTupleTuList(numbers)
print("List: ", numbers)
print("Tuple được tạo từ list là:", myTuple)