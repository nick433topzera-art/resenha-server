from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor rodando! 🚀"

@app.route("/api")
def api():
    return jsonify({"msg": "API funcionando!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
