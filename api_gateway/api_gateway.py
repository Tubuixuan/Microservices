from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis
from circuit_breaker_wrapper import circuit_protected_function

app = Flask(__name__)

# Kết nối đến Redis container qua Docker
redis_client = Redis(host="localhost", port=6379)  # Redis đang chạy trên localhost qua Docker

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379",  # URI của Redis container
    default_limits=["100 per 15 minutes"]  # Giới hạn mặc định
)
limiter.init_app(app)

@app.route("/")
def home():
    return jsonify(message="Welcome to API Gateway. Routes: /api/service, /api/other_service")

@app.route("/api/service")
@limiter.limit(None)  # Không giới hạn số lượng yêu cầu, để tập trung kiểm tra Circuit Breaker
def service():
    def backend_service():
        # Đây là nơi gọi logic backend thực tế
        raise Exception("Simulated backend failure")  # Mô phỏng lỗi
    return circuit_protected_function("backend_service", backend_service)

@app.route("/api/other_service")
def other_service():
    def backend_service_other():
        # Logic gọi dịch vụ khác
        return {"data": "Response from other service"}
    return circuit_protected_function("other_service", backend_service_other)

if __name__ == "__main__":
    app.run(port=3001)