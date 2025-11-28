from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/save", methods=["POST"])
def save_data():
    data = request.json
    with open("data/dados.json", "w") as f:
        import json
        json.dump(data, f)
    return jsonify({"status": "ok"})

app.run(host="0.0.0.0", port=5000)
