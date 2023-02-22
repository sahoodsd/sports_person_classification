from flask import Flask,request,jsonify
# import utils

app = Flask(__name__)


@app.route('/classify_image', methods=['get', 'post'])
def classify_image():
    return "hai"


if __name__ == "__main__":
    app.run(port=5000)
