# Tổng quan các luồng hoạt động:
# 1. Định nghĩa URL kết nối cơ sở dữ liệu.
# 2. Tạo engine để giao tiếp với cơ sở dữ liệu SQLite.
# 3. Tạo session maker để quản lý các phiên làm việc (session) với cơ sở dữ liệu.
# 4. Khởi tạo Base class để định nghĩa các models liên kết với các bảng trong cơ sở dữ liệu.

from sqlalchemy import create_engine  # Import create_engine để tạo engine giao tiếp với cơ sở dữ liệu.
from sqlalchemy.ext.declarative import declarative_base  # Import declarative_base để khai báo Base class cho các models.
from sqlalchemy.orm import sessionmaker  # Import sessionmaker để tạo các phiên làm việc với cơ sở dữ liệu.

# Định nghĩa URL kết nối cơ sở dữ liệu SQLite, đường dẫn file đặt trong thư mục hiện tại.
SQLALCHEMY_DATABASE_URL = "sqlite:///./products.db"

# Tạo engine giao tiếp với cơ sở dữ liệu.
# Engine thực hiện giao tiếp trực tiếp với SQLite database.
# connect_args={"check_same_thread": False}: Tắt kiểm tra giới hạn một luồng duy nhất để hỗ trợ ứng dụng đa luồng.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Tạo sessionmaker để quản lý các phiên giao tiếp với cơ sở dữ liệu.
# autocommit=False: Thay đổi trong session sẽ không được tự động ghi vào cơ sở dữ liệu.
# autoflush=False: Không tự động đẩy các thay đổi từ session vào cơ sở dữ liệu trước khi truy vấn.
# bind=engine: Liên kết session với engine để thực hiện truy vấn.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tạo một Base class để định nghĩa các models.
# Các lớp con của Base sẽ ánh xạ (map) với các bảng trong cơ sở dữ liệu.
Base = declarative_base()