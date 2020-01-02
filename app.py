from flask import Flask,jsonify
import random
from string import *

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
    symbols = ascii_letters + punctuation +  digits + ascii_lowercase
    main_random = random.SystemRandom()
    password =  "".join(main_random.choice(symbols)
                    for i in range(18))
    passwd = str(password)
   
   
    return jsonify({"password":passwd})

if __name__ == '__main__':
    app.run(debug=True)

