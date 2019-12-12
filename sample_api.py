from flask import Flask,request

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

app.run(port=3001)
