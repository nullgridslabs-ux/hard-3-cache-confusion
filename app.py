# hard-3-cache-confusion/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

cache = {}

@app.route("/health")
def health():
    return "ok"

@app.route("/profile/<uid>")
def profile(uid):
    key = uid   # BUG: cache key ignores auth context

    if key in cache:
        return cache[key]

    if request.headers.get("X-Admin") == "1":
        resp = jsonify({"user":uid,"secret":"admin","flag":FLAG})
    else:
        resp = jsonify({"user":uid,"secret":"public"})

    cache[key] = resp
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
