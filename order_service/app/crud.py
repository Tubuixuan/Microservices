# Tổng quan các luồng hoạt động:
# 1. Định nghĩa các hàm để thao tác với cơ sở dữ liệu thông qua SQLAlchemy session (`db`).
# 2. Hàm `create_order` thêm một đơn hàng mới vào cơ sở dữ liệu.
# 3. Hàm `get_orders` lấy danh sách các đơn hàng từ cơ sở dữ liệu với khả năng phân trang.

from sqlalchemy.orm import Session  # Import Session để giao tiếp với cơ sở dữ liệu.
from . import models, schemas  # Import các models (ORM) và schemas (Pydantic) từ module hiện tại.

# Hàm tạo một đơn hàng mới trong cơ sở dữ liệu.
def create_order(db: Session, order: schemas.OrderCreate):
    # Chuyển dữ liệu từ schema `OrderCreate` thành dictionary để khởi tạo đối tượng ORM.
    db_order = models.Order(**order.dict())
    db.add(db_order)  # Thêm đối tượng đơn hàng mới vào session.
    db.commit()  # Ghi thay đổi vào cơ sở dữ liệu.
    db.refresh(db_order)  # Làm mới đối tượng để đồng bộ dữ liệu từ cơ sở dữ liệu.
    return db_order  # Trả về đối tượng đơn hàng vừa tạo.

# Hàm lấy danh sách các đơn hàng từ cơ sở dữ liệu với phân trang.
def get_orders(db: Session, skip: int = 0, limit: int = 10):
    # Thực hiện truy vấn trên bảng `Order`, bỏ qua `skip` bản ghi đầu tiên và lấy tối đa `limit` bản ghi.
    return db.query(models.Order).offset(skip).limit(limit).all()