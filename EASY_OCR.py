import os
import csv
from easyocr import Reader

# Đường dẫn đến thư mục chứa ảnh biển số xe
folder_path = "plates"

# Đường dẫn đến file lưu nội dung biển số xe
output_file = "output.csv"

# Khởi tạo đối tượng OCR
reader = Reader(['en'])

# Mở file output trong chế độ ghi
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Ghi tiêu đề cột vào file
    writer.writerow(['Image', 'License Plate'])

    # Duyệt qua từng ảnh trong thư mục
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # Đường dẫn đầy đủ đến ảnh
            image_path = os.path.join(folder_path, filename)

            # Đọc ảnh và trích xuất nội dung biển số
            result = reader.readtext(image_path)

            # Lấy nội dung biển số (nếu có)
            license_plate = result[0][1] if result else 'Unknown'

            # Ghi thông tin ảnh và biển số vào file
            writer.writerow([filename, license_plate])

print("Trích xuất nội dung biển số thành công!")