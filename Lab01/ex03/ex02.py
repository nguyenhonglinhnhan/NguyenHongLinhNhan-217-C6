def daoNguocList(List):
  return List[::-1]

inputList = input("Nhập danh sách các số, cách nhau băng dấu phẩy: ")
numbers = list(map(int, inputList.split(",")))

listDaoNguoc = daoNguocList(numbers)
print("Danh sách sau khi được đảo ngược là:", listDaoNguoc)
