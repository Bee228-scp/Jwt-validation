import jwt
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api", methods=["GET", "POST"])
def api():
    tok = request.headers.get("Authorization", "").replace("Bearer ", "")
    c = jwt.decode(tok, options={"verify_signature": False})
    return jsonify(message="Token accepted", role=c.get("role"))

app.run(port=5000)
