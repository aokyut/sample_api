from flask import Flask,request
import os
import json

app = Flask(__name__)

@app.route("/",methods=["POST"])
def post_json():
    posted_json = request.get_json()
    src_path = posted_json["src"]
    ref_path = posted_json["ref"]
    reso = int(posted_json["reso"])

    return src_path

@app.route("/",methods=["GET"])
def get():
    return "Hello"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get('PORT', 8080)))
