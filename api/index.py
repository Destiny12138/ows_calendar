from flask import Flask
from flask import send_file
import requests
import io
import datetime

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
@app.route("/")
def index():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400"
    }  # 发送头信息
    today = str(datetime.date.today())
    year = today[0:4]
    mon = today[5:7]+today[8:]
    req = requests.get(
        url=f"http://img.owspace.com/Public/uploads/Download/{year}/{mon}.jpg", headers=header)
    byte = req.content
    print(byte)
    # image = file("http://img.owspace.com/Public/uploads/Download/2023/0113.jpg")
    # resp = Response(image, mimetype="image/jpeg")
    # return resp
    # return send_file('/www/wwwroot/wordpress/wp-content/uploads/2022/09/wp_editor_md_9dca9e7ab09ca81213f36522cd10336c.jpg', mimetype='image/gif')
    return send_file(io.BytesIO(byte),
        mimetype='image/png')
from flask import render_template, jsonify
