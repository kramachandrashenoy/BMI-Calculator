# from flask import Flask, render_template, request
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     weight = float(request.form['weight'])
#     height = float(request.form['height']) / 100
#     bmi = weight / (height * height)
#     return render_template('result.html', bmi=bmi)

# if __name__ == '__main__':
#     if os.name == 'nt':  # Checks if the operating system is Windows
#         from waitress import serve
#         serve(app, host='0.0.0.0', port=8080)
#     else:
#         app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100
    bmi = weight / (height * height)
    return render_template('result.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
