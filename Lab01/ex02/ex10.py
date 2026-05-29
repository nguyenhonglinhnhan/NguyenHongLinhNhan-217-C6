def daoNguocChuoi(chuoi):
    return chuoi[::-1]
input_str = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là: ", daoNguocChuoi(input_str))