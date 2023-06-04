from markupsafe import escape
from flask import url_for,redirect,Flask,request,abort
from flask import jsonify

app = Flask(__name__) # 为Flask 类创造实例

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
# @app.route("/user/<name>")
# def hello(name):
#     return f"hello,{escape(name)}"
#
# @app.route("/post/<int:post_id>")
# def show_post_id(post_id):
#     return f"post id is {escape(post_id)}"
#
# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#     return f"Subpath is {escape(subpath)}"
#
# @app.route("/str/<string:zifu>")
# def show_substring(zifu):
#     return f"string is {escape(zifu)}"

# @app.route("/project/")   # 重定向页面
# def show_project():
#     return f"this is project page"
#
# @app.route("/about")
# def show_about():
#     return "this is about page}"

# @app.route('/')
# def index():
#     login_url = url_for('login',next='/')
#     return redirect(login_url)
#     return u'index'
#
#
# @app.route('/login')
# def login():
#     return 'login'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
@app.route('/query',methods=['GET','POST'])
def find_user():
    if 'qq' in request.args:
        qq_re = request.args.get('qq')
        response_data = [{'qq':'123456','phone':'456789'},{
            'qq':'789789','phone':'4567890'
        }]
        for x in response_data:
           if qq_re == x['qq']:
            return jsonify(x['phone'])
    else:
        return "不存在该字段"



if __name__ == '__main__':
    app.run()