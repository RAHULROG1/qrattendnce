from flask import Flask
from public import public
from admin import admin
from teacher import teacher
from api import api

app=Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(teacher,url_prefix='/teacher')
app.register_blueprint(api,url_prefix='/api')

app.secret_key="abc"


app.run(debug=True,port=5004,host="192.168.43.70")
