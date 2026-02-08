# hard-3-cache-confusion/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

cache = {}

@app.route("/")
def index():
    return """
<h2>User Profile Service</h2>
<p>Public profile API with performance caching enabled.</p>
<ul>
<li>GET /profile/&lt;uid&gt;</li>
<li>GET /health</li>
</ul>
<p>Admin users can view extended profile data.</p>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/profile/<uid>")
def profile(uid):
    key = uid

    if key in cache:
        return cache[key]

    if request.headers.get("X-Admin") == "1":
        resp = jsonify({"user":uid,"secret":"admin","flag":FLAG})
    else:
        resp = jsonify({"user":uid,"secret":"public"})

    cache[key] = resp
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
