FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các file yêu cầu trước
COPY requirements.txt /app/requirements.txt

# Cập nhật pip và cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Sao chép toàn bộ mã nguồn
COPY . /appv

# Thiết lập biến môi trường (nếu cần)
ENV PYTHONUNBUFFERED=1

# Mở cổng cho dịch vụ
EXPOSE 8001

# Chạy dịch vụ với uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]