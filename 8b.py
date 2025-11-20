# auth_jwt_min.py
from flask import Flask,request,jsonify
import jwt,datetime
a=Flask(__name__);KEY="mysecretkey"
U={"username":"admin","password":"1234"}

@a.post("/login")
def login():
 d=request.json
 if d==U:
  t=jwt.encode({"user":d["username"],"exp":datetime.datetime.utcnow()+datetime.timedelta(m=5)},KEY)
  return jsonify({"token":t})
 return jsonify({"error":"Invalid"}),401

@a.get("/secure-data")
def sec():
 h=request.headers.get("Authorization")
 if not h:return jsonify({"error":"No token"}),401
 try:jwt.decode(h,KEY,algorithms=["HS256"]);return jsonify({"message":"Access granted ✅"})
 except jwt.ExpiredSignatureError:return jsonify({"error":"Expired"}),401
 except:return jsonify({"error":"Invalid"}),401

if __name__=="__main__":a.run()
