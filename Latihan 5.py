import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/picking-numbers', methods=["PUT"])
def pickingNumbers():
    a = request.json["data"] # kalau inputan array itu selalu di body 
    maksimum = 0
    for item in set(a):
        objek1 = a.count(item)
        objek2 = a.count(item + 1)
        hitung = objek1 + objek2
        if hitung > maksimum:
            maksimum = hitung
    return {"Hasil" : maksimum
    }

print(pickingNumbers([1, 2, 2, 3, 1, 2]))

