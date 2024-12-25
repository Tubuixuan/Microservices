# Tổng quan các luồng hoạt động:
# 1. Tạo các bảng trong cơ sở dữ liệu SQLite nếu chúng chưa tồn tại.
# 2. Khởi tạo ứng dụng FastAPI.
# 3. Định nghĩa dependency `get_db` để quản lý session kết nối cơ sở dữ liệu.
# 4. Tạo endpoint POST `/orders/` để thêm đơn hàng mới vào cơ sở dữ liệu.
# 5. Tạo endpoint GET `/orders/` để lấy danh sách đơn hàng với phân trang.
# 6. Cấu hình ứng dụng để chạy trên cổng 8002 thay vì cổng mặc định 8000.

import uvicorn  # Import uvicorn để chạy ứng dụng FastAPI.
from fastapi import FastAPI, Depends  # Import FastAPI và Depends để quản lý dependency.
from sqlalchemy.orm import Session  # Import Session để giao tiếp với cơ sở dữ liệu.

from . import crud, models, schemas  # Import các module `crud`, `models`, và `schemas` của ứng dụng.
from .database import SessionLocal, engine  # Import SessionLocal và engine từ module `database`.

# Tạo các bảng trong cơ sở dữ liệu nếu chúng chưa tồn tại.
# `models.Base.metadata.create_all` sử dụng engine để kiểm tra và tạo bảng.
models.Base.metadata.create_all(bind=engine)

# Khởi tạo ứng dụng FastAPI.
app = FastAPI()

# Dependency: Hàm lấy session kết nối cơ sở dữ liệu.
def get_db():
    # Tạo một session từ SessionLocal.
    db = SessionLocal()
    try:
        yield db  # Trả về session để sử dụng trong các endpoint.
    finally:
        db.close()  # Đóng session sau khi sử dụng để giải phóng tài nguyên.

# Định nghĩa endpoint POST để tạo đơn hàng mới trong cơ sở dữ liệu.
@app.post("/orders/", response_model=schemas.Order)  # Trả về schema `Order` sau khi tạo thành công.
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Sử dụng hàm `crud.create_order` để thêm đơn hàng vào cơ sở dữ liệu.
    return crud.create_order(db=db, order=order)

# Định nghĩa endpoint GET để lấy danh sách đơn hàng từ cơ sở dữ liệu.
@app.get("/orders/", response_model=list[schemas.Order])  # Trả về danh sách schema `Order`.
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Sử dụng hàm `crud.get_orders` để lấy dữ liệu từ cơ sở dữ liệu với phân trang.
    return crud.get_orders(db=db, skip=skip, limit=limit)

# Thay đổi cổng mặc định từ 8000 sang 8002 khi chạy ứng dụng.
if __name__ == "__main__":
    # Chạy ứng dụng FastAPI trên cổng 8002 với reload tự động.
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)