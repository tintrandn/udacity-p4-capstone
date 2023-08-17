from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = f"<h3>Udacity Capstone Project Home</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
