from functools import wraps
from flask import request
from prometheus_client import Counter, Histogram, start_http_server

REQUEST_COUNT = Counter("api_gateway_requests_total", "Total requests to API Gateway", ["method", "endpoint", "http_status"])
REQUEST_LATENCY = Histogram("api_gateway_request_latency_seconds", "Latency of requests in seconds")

def start_monitoring(port=5005):
    start_http_server(port)

def track_request(endpoint):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with REQUEST_LATENCY.time():
                response = func(*args, **kwargs)
                # Kiểm tra nếu response là tuple
                if isinstance(response, tuple):
                    response_body, status_code = response
                else:
                    response_body, status_code = response, 200  # Mặc định HTTP 200
                # Cập nhật Prometheus metrics
                REQUEST_COUNT.labels(
                    method=request.method,
                    endpoint=endpoint,
                    http_status=status_code
                ).inc()
                return response
        return wrapper
    return decorator