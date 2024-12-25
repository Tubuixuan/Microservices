# Tổng quan các luồng hoạt động:
# 1. Định nghĩa các schema sử dụng `Pydantic` để xác thực dữ liệu đơn hàng.
# 2. Schema `OrderBase` định nghĩa các trường cơ bản của một đơn hàng.
# 3. Schema `OrderCreate` kế thừa `OrderBase` và sử dụng cho việc tạo mới đơn hàng.
# 4. Schema `Order` bao gồm cả trường `id` (do cơ sở dữ liệu tự động tạo) và được cấu hình để hỗ trợ ORM mode.

from pydantic import BaseModel  # Import BaseModel từ Pydantic để định nghĩa schema.

# Định nghĩa schema cơ bản cho đơn hàng.
class OrderBase(BaseModel):
    product_id: int  # ID của sản phẩm liên quan đến đơn hàng.
    quantity: int  # Số lượng sản phẩm trong đơn hàng.
    status: str = "Pending"  # Trạng thái đơn hàng, giá trị mặc định là "Pending".

# Định nghĩa schema cho việc tạo mới đơn hàng.
# Kế thừa từ `OrderBase`, không bổ sung thêm thuộc tính nào.
class OrderCreate(OrderBase):
    pass  # Sử dụng trực tiếp các thuộc tính đã định nghĩa trong `OrderBase`.

# Định nghĩa schema cho đơn hàng hoàn chỉnh, bao gồm ID.
class Order(OrderBase):
    id: int  # ID của đơn hàng, được tự động tạo bởi cơ sở dữ liệu.

    # Cấu hình schema để hỗ trợ ORM mode.
    # Điều này cho phép sử dụng schema với các mô hình ORM như SQLAlchemy.
    class Config:
        orm_mode = True