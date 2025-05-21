import notebook
import jupyter

# Kiểu số nguyên (int)
so_nguyen = 10

# Kiểu số thực (float)
so_thuc = 3.14

# Kiểu chuỗi (str)
chuoi = "Xin chào AI!"

# Kiểu boolean (bool)
dung_sai = True

# Kiểu danh sách (list)
danh_sach = [1, 2, 3, 4, 5]

# Kiểu tuple (immutable list)
bo_nho = (30, 50, 40)

# Kiểu từ điển (dictionary)
du_lieu = {"ten": "ChatGPT", "tuoi": 6}

# In ra màn hình
print(so_nguyen, so_thuc, chuoi, dung_sai, danh_sach, bo_nho, du_lieu)

# List - Danh sách có thể thay đổi
ten_hoc_vien = ["Nam", "Hà", "Linh"]
print("Danh sách ban đầu:", ten_hoc_vien)

# Thêm phần tử
ten_hoc_vien.append("Minh")
print("Sau khi thêm Minh:", ten_hoc_vien)

# Xóa phần tử
ten_hoc_vien.remove("Hà")
print("Sau khi xóa Hà:", ten_hoc_vien)

# Dictionary - Lưu trữ dữ liệu dạng cặp key-value
hoc_vien = {
    "ten": "Nam",
    "tuoi": 20,
    "khoa_hoc": "AI cơ bản"
}

print("Thông tin học viên:", hoc_vien)

# Truy cập dữ liệu
print("Tên học viên:", hoc_vien["ten"])

# Cập nhật dữ liệu
hoc_vien["tuoi"] = 21
print("Thông tin sau khi cập nhật:", hoc_vien) 

# Danh sách trống
danh_sach_hoc_vien = []

# Nhập 3 học viên từ bàn phím
for i in range(3):
    ten = input(f"Nhập tên học viên {i+1}: ")
    danh_sach_hoc_vien.append(ten)

# In danh sách sau khi nhập
print("Danh sách học viên:", danh_sach_hoc_vien)
