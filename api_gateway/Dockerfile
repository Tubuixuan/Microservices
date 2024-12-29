FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các file cần thiết
COPY . /app

# Cập nhật pip và cài đặt các thư viện yêu cầu
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Mở cổng cho dịch vụ
EXPOSE 8000

# Chạy dịch vụ với uvicorn
CMD ["uvicorn", "api_gateway:app", "--host", "0.0.0.0", "--port", "8000"]