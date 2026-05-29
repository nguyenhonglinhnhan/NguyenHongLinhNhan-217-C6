from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
  print("\n Chương trình Quản lý Sinh Viên")
  print("***************************MENU***************************")
  print("**   1. Thêm sinh viên                                  **")
  print("**   2. Cập nhật thông tin sinh viên theo ID            **")
  print("**   3. Xóa sinh viên theo ID                           **")
  print("**   4. Tìm kiếm sinh viên theo tên                     **")
  print("**   5. Sắp xếp sinh viên theo Điểm Trung Bình          **")
  print("**   6. Sắp xếp sinh viên theo Tên chuyên ngành         **")
  print("**   7. Hiển thị danh sách sinh viên                    **")
  print("**   0. Thoát chương trình                              **")
  print("**********************************************************")

  key = int(input("Nhập tùy chọn: "))
  if (key == 1):
    print("\nThêm sinh viên.")
    qlsv.nhapSinhVien()
    print("\n Thêm sinh viên thành công!")
  elif (key == 2):
    if (qlsv.soLuongSinhVien() > 0):
      print("\n2. Cập nhật thông tin sinh viên.")
      print("\nNhập ID: ")
      ID = int(input())
      qlsv.updateSinhVien(ID)
    else:
      print("\nDanh sách sinh viên trống!")
  elif (key == 3):
    if (qlsv.soLuongSinhVien() > 0):
      print("\n3. Xóa sinh viên theo ID.")
      print("\nNhập ID: ")
      ID = int(input())
      if (qlsv.deleteByID(ID)):
        print("\nSinh viên có id = {} đã được xóa.".format(ID))
      else:
        print("\nSinh viên có id = {} không tồn tại.".format(ID))
    else:
      print("\nDanh sách sinh viên trống!")
  
  elif (key == 4):
    if (qlsv.soLuongSinhVien() > 0):
      print("\n4. Tìm kiếm sinh viên theo tên.")
      print("\nNhập tên để tìm kiếm: ")
      name = input()
      searchResult = qlsv.findByName(name)
      qlsv.showSinhVien(searchResult)
    else:
      print("\nDanh sách sinh viên trống!")
  
  elif (key == 5):
    if (qlsv.soLuongSinhVien() > 0):
      print("\n5. Sắp xếp sinh viên theo Điểm Trung Bình (GPA).")
      qlsv.sortByDiemTB()
      qlsv.showSinhVien(qlsv.getListSinhVien())
    else:
      print("\nDanh sách sinh viên trống!")

  elif (key == 6):
    if (qlsv.soLuongSinhVien() > 0):
      print("\n6. Sắp xếp sinh viên theo tên chuyên ngành.")
      qlsv.sortByMajor()
      qlsv.showSinhVien(qlsv.getListSinhVien())
    else:
      print("\nDanh sách sinh viên trống!")
  
  elif (key == 7):
    if (qlsv.soLuongSinhVien() > 0):
      print("\n7. Hiển thị danh sách sinh viên.")
      qlsv.showSinhVien(qlsv.getListSinhVien())
    else:
      print("\nDanh sách sinh viên trống!")

  elif (key == 0):
    print("\n Bạn đã chọn thoát chương trình!")
    break

  else:
    print("\n Không có chức năng này!")
    print("\n Hãy chọn chức năng trong menu!")