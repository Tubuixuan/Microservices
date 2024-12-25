from prometheus_client import Counter, Histogram, start_http_server
import time

REQUEST_COUNT = Counter("order_service_requests_total", "Total requests to the service")
REQUEST_LATENCY = Histogram("order_service_request_latency_seconds", "Request latency")

def start_monitoring(port=5003):
    start_http_server(port)

def track_request(func):
    def wrapper(*args, **kwargs):
        REQUEST_COUNT.inc()
        with REQUEST_LATENCY.time():
            return func(*args, **kwargs)
    return wrapper