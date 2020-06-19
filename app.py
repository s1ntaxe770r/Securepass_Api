from flask import Flask,jsonify
from gen import Password


app = Flask(__name__)

@app.route('/generate',methods=['GET'])
def generate():
    password = Password.generate()
    return jsonify({"password":password})

@app.route('/generate/<int:size>')
def fixeds(size):
    password = Password.generate(size)
    return jsonify({"password":password})


if __name__ == '__main__':
    app.run()
