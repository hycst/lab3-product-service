import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS: allow any origin; restrict to GET like the Rust version
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])

# Static catalog (same as Rust logic)
PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]

@app.get("/products")
def get_products():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    # Azure App Service provides PORT; locally you can default to 3030
    port = int(os.environ.get("PORT", "3030"))
    app.run(host="0.0.0.0", port=port)
