from flask import Flask, render_template
import requests

app = Flask(__name__)

URL = "https://opensheet.elk.sh/1AZ61TA_TcghJIK5hn09dprJDwX_r_osktzgPS1NlZlc/Productos"

@app.route("/")
def inicio():
    productos = requests.get(URL).json()
    return render_template("index.html", productos=productos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)