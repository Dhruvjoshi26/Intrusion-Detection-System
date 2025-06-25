from flask import Flask, render_template
import threading
import detect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start_detection():
    threading.Thread(target=detect.detect_intrusion).start()
    return "Intrusion Detection Started!"

if __name__ == "__main__":
    app.run(debug=True)
