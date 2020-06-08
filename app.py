#created by AdnanMahida
from flask import Flask #flask module
from flask_cors import CORS, cross_origin #Cross Origin Resource Sharing

app = Flask(__name__)
CORS(app) #pass app using CORS