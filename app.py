from distutils.log import debug
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        # 여기에 imglink 데이터가 넘어와서
        # face.py 에 있는 기능이 동작이 되어야함
        return "POST로 전달"
    
@app.route('/won')
def myimage():
    return render_template("myimage.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)