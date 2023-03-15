import json
import os
import uuid

from flask import request, make_response, jsonify, render_template
from flask_cors import cross_origin


from api import app

from api.web.main import UserManagement

app.secret_key = 'sdfadfDDERFGer2123'
# 设置Flask_admin样式
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


@app.route('/')
@cross_origin(supports_credentials=True)
def index():
    html = render_template('chatgpt/index.html')
    resp = make_response(html)
    # res = get_md().run(request.args.get('data'))
    # snap_t(res,msg='d_md_res')
    # print(res)
    return resp

@app.route('/<payPath>/', methods=['POST'])
@cross_origin(supports_credentials=True)
def handle_payPath(payPath):
    # print(type(request.json),request.json)
    # parameters = json.loads(request.json)
    res = payPathHandler(payPath, request.json)
    return make_response(jsonify(res))




def payPathHandler(payPath, parameters):
    # 根据payPath和parameters来处理请求，返回响应数据
    UM = UserManagement('C:/文件管理/100project/chatgpt_app/api/db/')


    if payPath == 'sent':
        newMessage = parameters['newMessage']
        session = parameters['session']
        apiKey = parameters['apiKey']
        # 处理逻辑
        res = UM.send_message(newMessage,session,apiKey)
        print(f"sent: newMessage={newMessage}, session={session}, apiKey={apiKey}")
        return res
    elif payPath == 'login':
        username = parameters['username']
        password = parameters['password']
        # 处理逻辑
        res = UM.login(username, password)
        print(f"login: username={username}, password={password}")
        return res
    elif payPath == 'session':
        session = parameters['session']
        # 处理逻辑
        print(f"session: session={session}")
        res = UM.check_session(session)
        return res
    elif payPath == 'uerDelete':
        id = parameters['id']
        session = parameters['session']
        # 处理逻辑
        print(f"uerDelete: id={id}, session={session}")
        UM.delete_user(id,session)
        return {'code': 0, 'data': 'success'}
    elif payPath == 'editUseInfo':
        id=parameters['id']
        username = parameters['username']
        password = parameters['password']
        vipExpirationDate = parameters['vipExpirationDate']
        session = parameters['session']
        res = UM.edit_user_info((id, username, password, vipExpirationDate, session))
        # 处理逻辑
        print('editUseInfo', res)
        return res
    elif payPath == 'createUserInfo':
        username = parameters['username']
        password = parameters['password']
        vipExpirationDate = parameters['vipExpirationDate']
        session = parameters['session']
        # 处理逻辑
        print(f"createUserInfo: username={username}, password={password}, vipExpirationDate={vipExpirationDate}, session={session}")
        return {'code': 0, 'data': 'success'}
    elif payPath == 'getUserList':
        session = parameters['session']
        print(['getUserList0', session])
        res = UserManagement('C:/文件管理/100project/chatgpt_app/api/db/').getUserInfoList(session)
        return res
    elif payPath == 'saveApiKey':
        session = parameters['session']
        apiKey = parameters['apiKey']
        # print(['getUserList0', session])
        res = UserManagement('C:/文件管理/100project/chatgpt_app/api/db/').saveApiKey(session,apiKey)
        return res
    else:
        return {'code': -1, 'data': 'invalid payPath'}



if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
#     snap_t(get_md().run('多对多存储资料'))
    # res = get_res().get_md()
    # snap_t(res, msg='res')
    # # res = User().generate_auth_token()
    # # print(res)

