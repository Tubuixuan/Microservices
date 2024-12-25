# Tổng quan các luồng hoạt động:
# 1. Định nghĩa các lớp dữ liệu (schemas) để mô tả và xác thực dữ liệu sản phẩm.
# 2. Sử dụng `Pydantic` để đảm bảo dữ liệu đầu vào tuân thủ cấu trúc định nghĩa.
# 3. Phân tách lớp dữ liệu cơ bản (`ProductBase`), lớp dữ liệu tạo mới (`ProductCreate`), và lớp đại diện sản phẩm hoàn chỉnh (`Product`).

from pydantic import BaseModel  # Import BaseModel từ Pydantic để định nghĩa và xác thực dữ liệu.

# Định nghĩa lớp cơ bản cho dữ liệu sản phẩm.
class ProductBase(BaseModel):
    name: str  # Tên sản phẩm (kiểu chuỗi, bắt buộc).
    description: str  # Mô tả sản phẩm (kiểu chuỗi, bắt buộc).
    price: int  # Giá sản phẩm (kiểu số nguyên, bắt buộc).
    quantity: int  # Số lượng sản phẩm trong kho (kiểu số nguyên, bắt buộc).

# Định nghĩa lớp dữ liệu dùng khi tạo mới sản phẩm.
# Kế thừa từ ProductBase và không thêm thuộc tính nào khác.
class ProductCreate(ProductBase):
    pass  # Không thêm thuộc tính nào, sử dụng trực tiếp các thuộc tính từ `ProductBase`.

# Định nghĩa lớp dữ liệu đại diện cho một sản phẩm hoàn chỉnh (bao gồm cả ID).
class Product(ProductBase):
    id: int  # ID sản phẩm (kiểu số nguyên, bắt buộc).

    # Cấu hình cho phép Pydantic làm việc với ORM (Object Relational Mapping).
    class Config:
        orm_mode = True  # Cho phép sử dụng dữ liệu từ các mô hình ORM như SQLAlchemy.