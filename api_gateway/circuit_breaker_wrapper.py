import pybreaker
from flask import jsonify

# Tạo Circuit Breaker
api_circuit_breaker = pybreaker.CircuitBreaker(
    fail_max=5,          # Tối đa 5 lỗi liên tiếp
    reset_timeout=30     # Thời gian mở 30 giây
)

# Hàm fallback khi dịch vụ không khả dụng
def circuit_fallback(service_name):
    return jsonify({
        "message": f"The service '{service_name}' is temporarily unavailable. Please try again later."
    }), 503

# Hàm bọc logic Circuit Breaker
def circuit_protected_function(service_name, func, *args, **kwargs):
    try:
        # Gọi dịch vụ qua Circuit Breaker
        return api_circuit_breaker.call(func, *args, **kwargs)
    except pybreaker.CircuitBreakerError:
        # Kích hoạt fallback khi Circuit Breaker đang mở
        return circuit_fallback(service_name)