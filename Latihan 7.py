# Latihan 7
# Hurdle Race 
# GET /hurdle-race/k/1 
# Req body: { "height": [1,2,3,3,2] } 
# Resp body: { "min_doses": 2 } 

import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/hurdle-race/k/<input_k>')

def hurdleRace(input_k):
    # Write your code here
    k2 = int(input_k)
    a = request.json["height"]
    maxi = max(a)
    if maxi > k2:
        return {"min_doses" : maxi - k2
        }
    else:
        return {"min_doses" : 0
        }
