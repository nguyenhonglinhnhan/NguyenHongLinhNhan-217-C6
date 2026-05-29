def demSoLanXuatHien(list):
  countDict = {}
  for num in list:
    if num in countDict:
      countDict[num] += 1
    else:
      countDict[num] = 1
  return countDict
inputString = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
wordList = inputString.split()

soLanXuatHien = demSoLanXuatHien(wordList)
print("Số lần xuất hiện của các phần tử: ", soLanXuatHien)