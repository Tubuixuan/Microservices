from flask import Flask, jsonify, request
from api_gateway.app.logging_config import setup_logging
from api_gateway.app.monitoring import start_monitoring, track_request

app = Flask(__name__)

# Set up logging
setup_logging()

# Start monitoring server
start_monitoring(port=5005)

@app.route("/health", methods=["GET"])
@track_request("/health")
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
@track_request("/<path:path>")
def forward_request(path):
    # Example forwarding logic
    app.logger.info(f"Forwarding request to {path}")
    return jsonify({"message": "Request forwarded", "path": path}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)