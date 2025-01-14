from flask import Flask, render_template, request, jsonify
from test import con_my_sql

app = Flask(__name__)

# 入口
@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/add')
def add():  # put application's code here
    # return 'Hello World!'
    return render_template('register.html')

# 注册
@app.route('/register', methods=['post'])
def register():
    # name = request.form.get('username')
    # pwd = request.form.get('password')

    name = request.json.get('username')
    pwd = request.json.get('password')

    # 查询用户是否存在
    code = 'select * from users where username=%s'
    cursor_ans = con_my_sql(code, (name))
    cursor_select = cursor_ans.fetchall()

    if len(cursor_select) > 0:
        return '用户已存在'
    else:
        login_data[name] = pwd
        insertCode = 'INSERT INTO users (username, password) VALUES (%s, %s)'
        insertResult = con_my_sql(insertCode, (name, pwd))
        print(insertResult, 'BBBB')
        return '注册成功'

# 登录数据字典
login_data = {
    '张三': 123456
}

# 登录
@app.route('/login', methods=['post'])
def login():
    name = request.form.get('username')
    pwd = request.form.get('password')

    code = 'select * from users where username=%s'
    cursor_ans = con_my_sql(code, (name))
    cursor_select = cursor_ans.fetchall()
    print(cursor_select,'aaaa')

    if len(cursor_select) > 0:
        if pwd == cursor_select[0]['password']:
            return '登录成功'
        else:
            return '密码错误'
    else:
        return '用户不存在'

@app.route('/query', methods=['get'])
def query():
    # 接受url ？后的参数
    # param = request.args.get('param')
    # print(param, 'aaaa')
    code = 'select * from users'
    cursor_ans = con_my_sql(code)
    cursor_select = cursor_ans.fetchall()
    return jsonify(cursor_select)

# 校验【有人】推送地址校验，返回
@app.route('/check', methods=['get'])
def check():
    verify = request.args.get('verify')
    print(verify, 'check response verify')
    return verify

# 接收【有人】http数据的推送
@app.route('/receive', methods=['post'])
def receive():
    raw_data = request.data
    print(raw_data, 'receive data')
    return ''



if __name__ == '__main__':
    # 调试模式，html模板变动，页面也会跟着变。不需要重新启动服务
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

    # query
    username = 'xiaozhi'
    pwd = '123456'
    code = 'select * from users where username=%s'
    result = con_my_sql(code, (username))


