from flask import Flask,request
import random
import os
import glob
import base64
app = Flask(__name__,static_folder="static")
@app.route('/')
def home():
    return app.send_static_file('home.html')
    
@app.route("/login")
def login_page():
    return app.send_static_file("login.html")

@app.route("/login",methods = ["POST"])
def Users_login():
    body = request.get_json()
    if check_user(body["Username"],body["Pwd"]):
        return {"page":"/upload"}
    else:
        return {"page":"/signup"}

def check_user(username,password):
    User = f"{username}_{password}"
    is_valid = False
    for Users in os.listdir("F:\\project\\cloudbox\\Members"):
        if User == Users:
            is_valid = True
    return is_valid

@app.route("/signup")
def get_information():
    return app.send_static_file("sign up.html")

@app.route("/signup",methods = ["POST"])
def create_folder():
    body = request.get_json()
    os.makedirs(os.path.join("F:\\project\\cloudbox\\Members",body["Username"]+"_"+body["Pwd"]))
    return {"page":"/upload"}

@app.route("/upload",methods = ["GET"])
def copy():
    return app.send_static_file("uploadfile.html")

@app.route("/upload",methods = ["POST"])
def copy_2():
    username = request.authorization["username"]
    password = request.authorization["password"]
    if check_user(username,password):
        body = request.get_json()
        if body["File"] == "True":
            destition_file = open(os.path.join(f"F:\\project\\cloudbox\\Members\\{username}_{password}",os.path.join(body["address"],body["file_name"])) , "wb+")
            file_base64 = body["FILE"]
            base64_bytes = file_base64.encode('ascii')
            file_bytes = base64.b64decode(base64_bytes)
            newFileByteArray = bytearray(file_bytes)
            destition_file.write(newFileByteArray)
        if body['File'] == "False":
            os.makedirs(os.path.join(f"F:\\project\\cloudbox\\Members\\{username}_{password}",os.path.join(body["address"],body["folder_name"])))
    else:
        return {"page":"/sign_up"}
    return body

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=443,debug=True)