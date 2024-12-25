# Tổng quan các luồng hoạt động:
# 1. Định nghĩa class `Product` đại diện cho bảng `products` trong cơ sở dữ liệu.
# 2. Khai báo các cột trong bảng, ánh xạ chúng với các thuộc tính của class.
# 3. Sử dụng SQLAlchemy để tự động hóa việc tạo bảng trong cơ sở dữ liệu từ class `Product`.

from sqlalchemy import Column, Integer, String  # Import các kiểu dữ liệu và công cụ để định nghĩa bảng và cột.
from .database import Base  # Import Base class từ module database, dùng để tạo các models.

# Định nghĩa class `Product` ánh xạ với bảng `products` trong cơ sở dữ liệu.
class Product(Base):
    __tablename__ = "products"  # Tên bảng trong cơ sở dữ liệu sẽ là "products".

    # Cột `id`: Khóa chính (primary key) của bảng.
    # `Integer`: Dữ liệu kiểu số nguyên.
    # `primary_key=True`: Đặt `id` làm khóa chính.
    # `index=True`: Tạo chỉ mục để tối ưu hóa truy vấn trên cột này.
    id = Column(Integer, primary_key=True, index=True)

    # Cột `name`: Tên sản phẩm.
    # `String`: Kiểu chuỗi ký tự.
    # `index=True`: Tạo chỉ mục để tối ưu hóa truy vấn trên cột này.
    name = Column(String, index=True)

    # Cột `description`: Mô tả sản phẩm.
    # `String`: Kiểu chuỗi ký tự.
    # `index=True`: Tạo chỉ mục để tối ưu hóa truy vấn trên cột này.
    description = Column(String, index=True)

    # Cột `price`: Giá sản phẩm.
    # `Integer`: Kiểu số nguyên, biểu diễn giá trị giá sản phẩm.
    price = Column(Integer)

    # Cột `quantity`: Số lượng sản phẩm còn trong kho.
    # `Integer`: Kiểu số nguyên, biểu diễn số lượng sản phẩm.
    quantity = Column(Integer)