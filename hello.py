from markupsafe import escape
from flask import url_for, redirect, Flask, request, abort
from flask import jsonify
import pymysql
from pymysql import cursors
import json
app = Flask(__name__)  # 为Flask 类创造实例

db = pymysql.connect(host='localhost',
                     user='root',
                     password='.',
                     database='user',
                     autocommit=False,
                     cursorclass=cursors.DictCursor)  # 关闭自动提交事务

cursor = db.cursor()


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
def query_mysql(qq_re):
    data = []
    for i in range(1, 37):
        try:

            sql = f"select * from qq{i} where qq = '{qq_re}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result)==0:
                continue
            else:
                data.append(result)

        except Exception as e:
            return f"{e}"

    return data



@app.route('/query', methods=['GET', 'POST'])
def find_user():
    if 'qq' in request.args:
        qq_re = request.args.get('qq')
        data_response = query_mysql(qq_re)
        if len(data_response)==0:
            return "null 未查询到"
        else:
            for x in data_response:
                return x
    else:
        return "不存在该字段"


if __name__ == '__main__':
    app.run()