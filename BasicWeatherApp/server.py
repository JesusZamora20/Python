from flask import Flask, render_template, request
fromt weather import get_current_weather

app = Flask(__name__)

@app.route('/')
@app.route('/index')

#8:09 
