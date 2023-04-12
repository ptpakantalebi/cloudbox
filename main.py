from flask import Flask,request
import random
import os
import glob
import base64
app = Flask(__name__,static_folder='static')
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
        return {"page":"/sign_up"}

def check_user(username,password):
    User = f"{username}_{password}"
    is_valid = False
    for Users in os.listdir("F:\\Repos\\Cloudstorage\\Members"):
        if User == Users:
            is_valid = True
    return is_valid

@app.route("/sign_up")
def get_information():
    return app.send_static_file("sign up.html")

@app.route("/sign_up",methods = ["POST"])
def create_folder():
    body = request.get_json()
    os.makedirs(os.path.join("F:\\Repos\\Cloudstorage\\Members",body["Username"]+"_"+body["Pwd"]))
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
            destition_file = open(os.path.join(f"F:\\Repos\\Cloudstorage\\Members\\{username}_{password}",os.path.join(body["address"],body["file_name"])) , "wb+")
            file_base64 = body["FILE"]
            base64_bytes = file_base64.encode('ascii')
            file_bytes = base64.b64decode(base64_bytes)
            newFileByteArray = bytearray(file_bytes)
            destition_file.write(newFileByteArray)
        if body['File'] == "False":
            os.makedirs(os.path.join(f"F:\\Repos\\Cloudstorage\\Members\\{username}_{password}",os.path.join(body["address"],body["folder_name"])))
    else:
        return {"page":"/sign_up"}
    return body
    # files_list = []
# folders_list = []
# def paths(p):
#     for t in glob.glob(os.path.join(p,"**\\*.*"),recursive=True):
#         files_list.append(t[len(p)+1:])
#         address = t[len(p):].split("\\")[1]
#         for e in range(len(t[len(p):].split("\\")[1:-1])):
#             folders_list.append(address)
#             address = os.path.join(address,t[len(p):].split("\\")[1:-1][e])
# print(paths("F:\Repos\Cloudstorage\SampleInput"))
# def copy_folder(files,folders,new_path,last_path):
#     for folder in folders:
#         if not os.path.exists(os.path.join(new_path,folder)):
#             os.makedirs(os.path.join(new_path,folder))
#     for file in files:
#         copy(os.path.join(last_path,file),os.path.join(new_path,file))
# copy_folder(files_list,folders_list,"F:\Repos\Cloudstorage\Sample output","F:\Repos\Cloudstorage\SampleInput")
# files_list = []
# folders_list = []
# def paths(p):
#     for t in glob.glob(os.path.join(p,"**\\*.*"),recursive=True):
#         files_list.append(t[len(p)+1:])
#         address = t[len(p):].split("\\")[1]
#         for e in range(len(t[len(p):].split("\\")[1:-1])):
#             folders_list.append(address)
#             address = os.path.join(address,t[len(p):].split("\\")[1:-1][e])
# print(paths("F:\Repos\Cloudstorage\SampleInput"))
# def copy_folder(files,folders,new_path,last_path):
#     for folder in folders:
#         if not os.path.exists(os.path.join(new_path,folder)):
#             os.makedirs(os.path.join(new_path,folder))
#     for file in files:
#         copy(os.path.join(last_path,file),os.path.join(new_path,file))
# copy_folder(files_list,folders_list,"F:\Repos\Cloudstorage\Sample output","F:\Repos\Cloudstorage\SampleInput")
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=443,debug=True)