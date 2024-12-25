# Tổng quan các luồng hoạt động:
# 1. Định nghĩa lớp `Order` đại diện cho bảng `orders` trong cơ sở dữ liệu.
# 2. Sử dụng SQLAlchemy để ánh xạ các cột của bảng `orders` thành các thuộc tính của lớp `Order`.
# 3. Định nghĩa các cột chính như `id`, `product_id`, `quantity`, và `status` với các kiểu dữ liệu tương ứng.
# 4. Cung cấp các thuộc tính mặc định như `status` với giá trị ban đầu là "Pending".

from sqlalchemy import Column, Integer, String  # Import các công cụ để định nghĩa bảng và cột.
from .database import Base  # Import Base class từ module database để định nghĩa các models.

# Định nghĩa lớp `Order` ánh xạ với bảng `orders` trong cơ sở dữ liệu.
class Order(Base):
    __tablename__ = "orders"  # Tên bảng trong cơ sở dữ liệu sẽ là "orders".

    # Cột `id`: Khóa chính (primary key) của bảng.
    # `Integer`: Dữ liệu kiểu số nguyên.
    # `primary_key=True`: Đặt `id` làm khóa chính.
    # `index=True`: Tạo chỉ mục để tối ưu hóa truy vấn trên cột này.
    id = Column(Integer, primary_key=True, index=True)

    # Cột `product_id`: ID của sản phẩm liên quan đến đơn hàng.
    # `Integer`: Kiểu số nguyên.
    # `index=True`: Tạo chỉ mục để tối ưu hóa truy vấn trên cột này.
    product_id = Column(Integer, index=True)

    # Cột `quantity`: Số lượng sản phẩm trong đơn hàng.
    # `Integer`: Kiểu số nguyên.
    quantity = Column(Integer)

    # Cột `status`: Trạng thái của đơn hàng.
    # `String`: Kiểu chuỗi ký tự.
    # `default="Pending"`: Giá trị mặc định là "Pending".
    status = Column(String, default="Pending")