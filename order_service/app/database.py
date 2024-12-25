# Tổng quan các luồng hoạt động:
# 1. Định nghĩa URL kết nối cơ sở dữ liệu SQLite, sử dụng file `orders.db`.
# 2. Tạo engine SQLAlchemy để giao tiếp với cơ sở dữ liệu SQLite.
# 3. Cấu hình `SessionLocal` để tạo các phiên làm việc (sessions) với cơ sở dữ liệu.
# 4. Khởi tạo `Base` class, được dùng để định nghĩa các mô hình dữ liệu (models) ánh xạ với bảng trong cơ sở dữ liệu.

from sqlalchemy import create_engine  # Import create_engine để khởi tạo engine giao tiếp với cơ sở dữ liệu.
from sqlalchemy.ext.declarative import declarative_base  # Import declarative_base để khai báo Base class cho các models.
from sqlalchemy.orm import sessionmaker  # Import sessionmaker để tạo các session làm việc với cơ sở dữ liệu.

# Định nghĩa URL kết nối cơ sở dữ liệu SQLite.
# `sqlite:///./orders.db` chỉ định sử dụng SQLite với file cơ sở dữ liệu `orders.db` nằm cùng thư mục với file hiện tại.
SQLALCHEMY_DATABASE_URL = "sqlite:///./orders.db"

# Tạo engine để giao tiếp với cơ sở dữ liệu.
# `connect_args={"check_same_thread": False}`:
# - Tắt kiểm tra giới hạn một luồng duy nhất của SQLite.
# - Điều này cần thiết khi ứng dụng sử dụng nhiều luồng hoặc framework như FastAPI.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Tạo sessionmaker để quản lý các phiên giao tiếp với cơ sở dữ liệu.
# `autocommit=False`: Thay đổi không tự động được ghi vào cơ sở dữ liệu.
# `autoflush=False`: Không tự động đẩy các thay đổi vào cơ sở dữ liệu trước khi truy vấn.
# `bind=engine`: Liên kết session với engine để sử dụng trong các truy vấn.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Khởi tạo Base class từ declarative_base.
# Base được dùng làm nền tảng để định nghĩa các models.
# Các lớp con của Base sẽ ánh xạ (map) với các bảng trong cơ sở dữ liệu.
Base = declarative_base()