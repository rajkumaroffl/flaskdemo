from flask import Flask

app=Flask(__name__)

@app.route('/raj')
def home():
    return "Hi Raj"

@app.route('/hello')
def hello_world():
    return '<h1>hello<h1><h3> world<h3>'



if __name__ =="__main__":
    app.run(debug=True)

