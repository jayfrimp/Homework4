from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route ('/covid')
def tracker():
    data=dict(
        newcase=40,
        total=300,
        active=99,
        recov=195,
        death=6,
    )
    return jsonify(data)