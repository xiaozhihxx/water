from flask import Flask, render_template, request, jsonify, Response
from test import con_my_sql

app = Flask(__name__)

# 【有人】推送数据
# 根组织
@app.route('/receiveRootGroup', methods=['get', 'post'])
def receiveRootGroup():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receiveRootGroup 根组织')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receiveRootGroup 根组织')
        return Response(status=200)

# 螃蟹
@app.route('/receivePangxie', methods=['get', 'post'])
def receivePangxie():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receivePangxie 螃蟹')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receivePangxie 螃蟹')
        return Response(status=200)

# 2号水产
@app.route('/receiveWater2', methods=['get', 'post'])
def receiveWater2():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receiveWater2 2号水产')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receiveWater2 2号水产')
        return Response(status=200)

# 1号水产
@app.route('/receiveWater1', methods=['get', 'post'])
def receiveWater1():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receiveWater1 1号水产')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receiveWater1 1号水产')
        return Response(status=200)


# 斑节虾池
@app.route('/receiveBanjie', methods=['get', 'post'])
def receiveBanjie():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receiveBanjie 斑节虾池')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receiveBanjie 斑节虾池')
        return Response(status=200)

# 鳜鱼池
@app.route('/receiveJueyu', methods=['get', 'post'])
def receiveJueyu():
    if request.method == 'GET':
        verify = request.args.get('verify')
        print(verify, 'get receiveJueyu 鳜鱼池')
        return verify
    elif request.method == 'POST':
        raw_data = request.json
        print(raw_data, 'post receiveJueyu 鳜鱼池')
        return Response(status=200)

if __name__ == '__main__':
    # 调试模式，html模板变动，页面也会跟着变。不需要重新启动服务
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)