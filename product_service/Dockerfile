FROM python:3.11-slim  
# Thay đổi phiên bản Python thành 3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip  
# Cập nhật pip trước khi cài đặt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
