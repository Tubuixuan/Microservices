from flask import Flask, request
from product_service.app.logging_config import setup_logging
from product_service.app.monitoring import start_monitoring, monitor_request
import logging

# Cấu hình logging
setup_logging()
logger = logging.getLogger(__name__)

# Tạo ứng dụng Flask
app = Flask(__name__)

# Khởi động Prometheus metrics
start_monitoring(port=5001)

@app.route("/")
def home():
    with monitor_request(endpoint="/", method=request.method):
        logger.info("Accessed home endpoint")
        return {"message": "Welcome to Product Service"}

@app.route("/products")
def get_products():
    with monitor_request(endpoint="/products", method=request.method):
        logger.info("Accessed products endpoint")
        return {"products": ["Product A", "Product B", "Product C"]}

if __name__ == "__main__":
    logger.info("Starting Product Service...")
    app.run(port=5000)