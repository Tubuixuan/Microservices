# Tổng quan các luồng hoạt động:
# 1. Tạo các bảng trong cơ sở dữ liệu SQLite nếu chúng chưa tồn tại.
# 2. Khởi tạo ứng dụng FastAPI.
# 3. Định nghĩa dependency `get_db` để quản lý session kết nối cơ sở dữ liệu.
# 4. Tạo endpoint POST `/products/` để thêm sản phẩm mới vào cơ sở dữ liệu.
# 5. Tạo endpoint GET `/products/` để lấy danh sách sản phẩm với phân trang.
# 6. Cấu hình ứng dụng để chạy trên cổng 8001 thay vì cổng mặc định 8000.

import uvicorn  # Import uvicorn để chạy ứng dụng FastAPI.
from fastapi import FastAPI, Depends, HTTPException  # Import các công cụ từ FastAPI.
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

# Định nghĩa endpoint POST để tạo sản phẩm mới trong cơ sở dữ liệu.
@app.post("/products/", response_model=schemas.Product)  # Trả về schema `Product` sau khi tạo thành công.
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    # Sử dụng hàm `crud.create_product` để thêm sản phẩm vào cơ sở dữ liệu.
    return crud.create_product(db=db, product=product)

# Định nghĩa endpoint GET để lấy danh sách sản phẩm từ cơ sở dữ liệu.
@app.get("/products/", response_model=list[schemas.Product])  # Trả về danh sách schema `Product`.
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Sử dụng hàm `crud.get_products` để lấy dữ liệu từ cơ sở dữ liệu với phân trang.
    return crud.get_products(db=db, skip=skip, limit=limit)

# Thay đổi cổng mặc định từ 8000 sang 8001 khi chạy ứng dụng.
if __name__ == "__main__":
    # Chạy ứng dụng FastAPI trên cổng 8001 với reload tự động.
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)