from prometheus_client import Counter, Histogram, start_http_server
from contextlib import contextmanager
import time

# Metrics cho Prometheus
REQUEST_COUNT = Counter("product_service_request_count", "Total HTTP requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("product_service_request_latency_seconds", "Request latency", ["endpoint"])

def start_monitoring(port=5001):
    """Khởi động server Prometheus metrics"""
    start_http_server(port)
    print(f"Prometheus metrics available at http://localhost:{port}")

@contextmanager
def monitor_request(endpoint: str, method: str):
    """Đo thời gian và ghi nhận số lượng request"""
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    start_time = time.time()
    try:
        yield  # Đánh dấu điểm bắt đầu của context manager
    finally:
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(time.time() - start_time)