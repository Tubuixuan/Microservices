# Tổng quan các luồng hoạt động:
# 1. Cung cấp các hàm để tương tác với cơ sở dữ liệu qua SQLAlchemy session (`db`).
# 2. Hàm `get_products` lấy danh sách các sản phẩm từ cơ sở dữ liệu với khả năng phân trang.
# 3. Hàm `create_product` tạo mới một sản phẩm trong cơ sở dữ liệu dựa trên thông tin đầu vào từ schema.

from sqlalchemy.orm import Session  # Import Session để thao tác với cơ sở dữ liệu thông qua ORM.
from . import models, schemas  # Import các models (ORM) và schemas (Pydantic) từ module hiện tại.

# Hàm lấy danh sách các sản phẩm từ cơ sở dữ liệu.
def get_products(db: Session, skip: int = 0, limit: int = 10):
    # Sử dụng session (`db`) để truy vấn bảng `Product`.
    # .offset(skip): Bỏ qua một số bản ghi đầu (phục vụ phân trang).
    # .limit(limit): Giới hạn số lượng bản ghi trả về.
    # .all(): Lấy tất cả các bản ghi kết quả truy vấn.
    return db.query(models.Product).offset(skip).limit(limit).all()

# Hàm tạo mới một sản phẩm trong cơ sở dữ liệu.
def create_product(db: Session, product: schemas.ProductCreate):
    # Tạo một đối tượng `Product` từ dữ liệu đầu vào.
    # **product.dict(): Chuyển dữ liệu từ schema `ProductCreate` sang dictionary để khởi tạo đối tượng ORM.
    db_product = models.Product(**product.dict())
    db.add(db_product)  # Thêm đối tượng mới vào session.
    db.commit()  # Ghi thay đổi vào cơ sở dữ liệu.
    db.refresh(db_product)  # Làm mới đối tượng để đồng bộ dữ liệu từ cơ sở dữ liệu.
    return db_product  # Trả về đối tượng sản phẩm vừa tạo.