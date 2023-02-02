from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route('/hello')
def hello():
    return "/helloworld"

@app.route('/name/<name>',
           methods=["GET"],
           endpoint="route_endpoint")
def route_name(name):
    return render_template("index.html", name=name)

# 以下のように記載することでもGET,POSTで受け付けることができる。
@app.get("/gpUrl")
@app.post("/gpUrl")
def gpUrl():
    pass