from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request)

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

@app.route('/contact')
def contact():
    """
    フォーム表示
    """
    return render_template("contact.html")

@app.route('/contact/complete', methods=['GET', 'POST'])
def contact_complete():
    """
    フォームで送信後にフォーム画面にRedirect
    """
    # POSTされたとき
    if request.method == "POST":
        # なんらかの処理をPOSTされたデータにする。
        # dataにフォームの内容を積む
        data = request.form
        print(data)
        # Validationをかける。
        is_valid = False
        if not data["username"]:
            print("ユーザー名は必須です。")
        if not data["mail_address"]:
            print("メルアドは必須です。")
        if not data["desc"]:
            print("詳細は必須です。")
        return redirect(url_for('contact_complete'))
    return render_template("contact_complete.html")