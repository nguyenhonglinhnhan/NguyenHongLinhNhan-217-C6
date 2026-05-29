def xoaPhanTu(dictiionary, key):
  if key in dictiionary:
    del dictiionary[key]
    return True
  else:
    return False

myDict = {"a": 1, "b": 2, "c": 3, "d": 4}
keyToDelete = 'b' 
result = xoaPhanTu(myDict, keyToDelete)
if result:
  print("Phần tử đã được xóa từ dictionary: ", myDict)
else:
  print("Không tìm thấy key trong dictionary.")