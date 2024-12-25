# Tổng quan các luồng hoạt động:
# 1. Triển khai một API Gateway sử dụng FastAPI để định tuyến các yêu cầu tới hai service: Product Service và Order Service.
# 2. Sử dụng `httpx.AsyncClient` để gửi các yêu cầu HTTP không đồng bộ đến các service.
# 3. Định nghĩa các endpoint tại API Gateway để:
#    - Lấy danh sách sản phẩm và đơn hàng từ các service.
#    - Tạo mới sản phẩm và đơn hàng thông qua các service.
# 4. Xử lý các lỗi HTTP từ các service và trả về mã lỗi tương ứng cho client.

from fastapi import FastAPI, HTTPException  # Import FastAPI để tạo ứng dụng và HTTPException để xử lý lỗi.
from httpx import AsyncClient  # Import AsyncClient từ httpx để gửi yêu cầu HTTP không đồng bộ.

app = FastAPI()  # Khởi tạo ứng dụng FastAPI.

# URLs của các service
# Định nghĩa URL của Product Service và Order Service.
PRODUCT_SERVICE_URL = "http://127.0.0.1:8001"
ORDER_SERVICE_URL = "http://127.0.0.1:8002"

# HTTP Client để giao tiếp với các service.
client = AsyncClient()  # Tạo một instance của httpx.AsyncClient để gửi yêu cầu HTTP.

# Endpoint gốc của API Gateway.
@app.get("/")
def root():
    # Trả về thông điệp xác nhận rằng API Gateway đang hoạt động.
    return {"message": "API Gateway is running!"}

# Routing đến Product Service.
@app.get("/products/")  # Endpoint để lấy danh sách sản phẩm.
async def get_products():
    # Gửi yêu cầu GET đến Product Service.
    response = await client.get(f"{PRODUCT_SERVICE_URL}/products/")
    # Nếu Product Service trả về lỗi, ném HTTPException với mã lỗi và chi tiết.
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    # Trả về dữ liệu JSON từ Product Service.
    return response.json()

@app.post("/products/")  # Endpoint để tạo sản phẩm mới.
async def create_product(product: dict):
    # Gửi yêu cầu POST đến Product Service với dữ liệu sản phẩm.
    response = await client.post(f"{PRODUCT_SERVICE_URL}/products/", json=product)
    # Nếu Product Service trả về lỗi, ném HTTPException với mã lỗi và chi tiết.
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    # Trả về dữ liệu JSON từ Product Service.
    return response.json()

# Routing đến Order Service.
@app.get("/orders/")  # Endpoint để lấy danh sách đơn hàng.
async def get_orders():
    # Gửi yêu cầu GET đến Order Service.
    response = await client.get(f"{ORDER_SERVICE_URL}/orders/")
    # Nếu Order Service trả về lỗi, ném HTTPException với mã lỗi và chi tiết.
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    # Trả về dữ liệu JSON từ Order Service.
    return response.json()

@app.post("/orders/")  # Endpoint để tạo đơn hàng mới.
async def create_order(order: dict):
    # Gửi yêu cầu POST đến Order Service với dữ liệu đơn hàng.
    response = await client.post(f"{ORDER_SERVICE_URL}/orders/", json=order)
    # Nếu Order Service trả về lỗi, ném HTTPException với mã lỗi và chi tiết.
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    # Trả về dữ liệu JSON từ Order Service.
    return response.json()