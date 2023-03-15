from flask import Flask

app = Flask(__name__, template_folder='./spa', static_folder="./spa", static_url_path='/')