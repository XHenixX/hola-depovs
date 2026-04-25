from flask import Flask

app = Flask(__name__)
# cambio para trigger pipeline
@app.route("/")
def hola():
    return "Hola Mundo DevOps 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
