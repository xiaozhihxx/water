from flask import Flask, render_template, request, jsonify, Response
from test import con_my_sql

app = Flask(__name__)

# 【有人】推送数据
# 根组织
@app.route('/receiveRootGroup', methods=['get', 'post'])
def receiveRootGroup():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receiveRootGroup')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receiveRootGroup')
        return Response(status=200)

# 鳜鱼池
@app.route('/receiveJueyu', methods=['get', 'post'])
def receiveJueyu():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receiveJueyu')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receiveJueyu')
        return Response(status=200)

if __name__ == '__main__':
    # 调试模式，html模板变动，页面也会跟着变。不需要重新启动服务
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)