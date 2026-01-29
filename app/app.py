from flask import Flask, jsonify, request

# Create the Flask application object
app = Flask(__name__)

# Health check / root endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "Flask API is running"
    })

# Simple GET API
@app.route("/api/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({
        "greeting": f"Hello, {name}!"
    })

# Simple POST API
@app.route("/api/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Please provide 'a' and 'b'"}), 400

    result = data["a"] + data["b"]
    return jsonify({
        "result": result
    })

# Entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
