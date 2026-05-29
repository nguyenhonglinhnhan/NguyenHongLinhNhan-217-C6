def truyCapPhanTu(data):
  firstElement = data[0]
  lastElement = data[-1]
  return firstElement, lastElement

inputList = eval(input("Nhập tuple, ví dụ: (1, 2, 3, 4, 5): "))
first, last = truyCapPhanTu(inputList)
print("Phần tử đầu tiên của tuple là:", first)
print("Phần tử cuối cùng của tuple là:", last)