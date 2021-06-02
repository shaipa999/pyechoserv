from __future__ import print_function
import sys
import socket
from flask import Flask,redirect, url_for, request
app = Flask(__name__)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    if u_path == "index.html":
      data = ""
      try:
       with open('/code/index.html', 'r') as file:
        data = file.read()
      except:
       data = "File Not found"
      return data
    else:
     local_ip = ""
     try:
       hostname = socket.gethostname()
       local_ip = socket.gethostbyname(hostname) 
     except:
       local_ip = "Not_Found"
     return "DATA:" + u_path + "<br>IP:" + local_ip

