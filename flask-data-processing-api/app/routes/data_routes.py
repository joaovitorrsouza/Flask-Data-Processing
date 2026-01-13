from flask import Blueprint, request, jsonify
from app.services.data_service import handle_upload, fetch_data

data_bp = Blueprint("data", __name__)

@data_bp.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "CSV file is required"}), 400

    file = request.files["file"]
    result = handle_upload(file)

    return jsonify(result), 201

@data_bp.route("/metrics", methods=["GET"])
def metrics():
    data = fetch_data()
    return jsonify(data), 200

@data_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200
