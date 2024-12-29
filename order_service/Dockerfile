FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép tất cả mã nguồn
COPY . /app

# Cập nhật pip và cài đặt thư viện từ requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Mở cổng cho dịch vụ
EXPOSE 8002

# Lệnh khởi động dịch vụ
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]