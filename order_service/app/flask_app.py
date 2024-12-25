from flask import Flask, jsonify
from order_service.app.logging_config import setup_logging
from order_service.app.monitoring import start_monitoring, track_request

app = Flask(__name__)

# Set up logging
setup_logging()

# Start monitoring server
start_monitoring(port=5003)

@app.route("/health", methods=["GET"])
@track_request
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)