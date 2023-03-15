from flask import Flask

app = Flask(__name__, template_folder='./www', static_folder="./www", static_url_path='/')
base_path = "E:\\allfiles\\allfiles\\100project\\chatgpt_app"