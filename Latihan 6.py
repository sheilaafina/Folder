import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/cat-and-mouse/x/<input_x>', methods=["GET"]) # pake x karena kita akan input variable di input_x

def catAndMouse(input_x):
    x = int(input_x) # path parameter
    y = int(request.args.get("y")) # query parameter
    z = int(request.headers.get("z")) # header parameter
    if abs(x-z) < abs(y-z):
        message = ("Cat A")
    elif abs(x-z) > abs(y-z):
        message = ("Cat B")
    elif abs(x-z) == abs(y-z):
        message = ("Mouse C")
    return {"Message": message
    }