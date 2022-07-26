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
        return "POST로 전달"
    
@app.route('/won')
def myimage():
    return render_template("myimage.html")

if __name__ == '__main__':
    app.run(debug=True)