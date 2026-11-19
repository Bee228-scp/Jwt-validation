import jwt
from flask import Flask, request, jsonify, abort

app = Flask(__name__)
KEY = "lab7-secret-key-1234567890-abcdef"

@app.route("/api", methods=["GET", "POST"])
def api():
    tok = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        c = jwt.decode(tok, KEY, algorithms=["HS256"],
                       issuer="lab7", audience="students")
    except jwt.InvalidTokenError:
        abort(401)
    return jsonify(message="Token accepted", role=c.get("role"))

app.run(port=5001)
