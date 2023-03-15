from datetime import datetime, timedelta
import os
import re
import time
import uuid

import openai
import pandas as pd
import inspect

#
# base_path = ''

# 根据提供的数据，可以进行以下修改:
#
from api.public import snap


class MyClass:
    def __init__(self, msg):
        self.msg = msg

    def print_info(self, data):
        frame = inspect.currentframe()
        # 获取当前调用栈的信息
        filename = inspect.getframeinfo(frame).filename
        func_name = inspect.getframeinfo(frame).function
        lineno = inspect.getframeinfo(frame).lineno
        # 输出实例化所在文件名，类名，函数名和行号
        print(f"-----{filename}---MyClass---{func_name}---{lineno}/n参数类型，参数")
        # 输出参数data
        print(data)
        return data


class UserManagement:

    def __init__(self, basePath):
        self.user_path = basePath + 'user.xlsx'
        self.message_log_path = basePath + 'message_log.xlsx'

    def login(self, username, password):
        user = pd.read_excel(self.user_path)
        if username not in list(user['username']):
            new_data = {"id": uuid.uuid4().hex, "username": username, "password": password, "session": uuid.uuid4().hex,
                        "vipExpirationDate": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
                        "sessionTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        "isManage": False}
            user = user.append(new_data, ignore_index=True)
            user.to_excel(self.user_path, index=False)
            return {"resCode": 0, "session": new_data['session'], "vipExpirationDate": new_data['vipExpirationDate']}
        else:
            user_info = user[user['username'] == username]
            if user_info['password'].values[0] != password:
                return {"resCode": 1, "msg": "用户名或密码错误"}
            else:
                session = uuid.uuid4().hex
                user.loc[user['username'] == username, 'session'] = session
                vipExpirationDate = user_info['vipExpirationDate'].values[0]
                apiKey = user_info['apiKey'].values[0]
                sessionTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                user.loc[user['username'] == username, 'sessionTime'] = sessionTime
                user.to_excel(self.user_path, index=False)
                return {"resCode": 0, "session": session, 'apiKey': apiKey, "vipExpirationDate": vipExpirationDate}

    def check_session(self, session):
        user = pd.read_excel(self.user_path)
        if session not in list(user['session']):
            return {"resCode": 1, "msg": "没有登入"}
        else:
            user_info = user[user['session'] == session]
            apiKey = user_info['apiKey'].values[0]
            vipExpirationDate = user_info['vipExpirationDate'].values[0]
            return {"resCode": 0, "apiKey": apiKey, "vipExpirationDate": vipExpirationDate}

    def getUserInfoList(self, session):
        df = pd.read_excel(self.user_path)
        print(['getUserList1', session])
        user_info_list = df[df['session'] == session]

        if user_info_list.empty:
            return {'resCode': 1, 'msg': 'session不存在'}
        elif user_info_list['isManage'].iloc[0]:
            # 如果是管理员，则返回整张表的内容

            all_user_info_list = df.to_dict('records')
            print(['---tttttttttt--',type(all_user_info_list[0]['vipExpirationDate']), all_user_info_list[0]['vipExpirationDate']])
            return {'resCode': 0, 'userInfoList': all_user_info_list}
        else:
            return {'resCode': 2, 'msg': '不是管理员'}
    def delete_user(self, id, session):
        user = pd.read_excel(self.user_path)
        snap.snap_t([id,session],msg='delete0')
        MyClass('delete0').print_info([id,session])
        if session not in list(user['session']):
            return {"resCode": 1, "msg": "没有登入"}
        else:
            user.drop(user[user['id'] == id].index, inplace=True)
            user.to_excel(self.user_path, index=False)
            return {"resCode": 0, 'msg': '删除成功'}

    def edit_user_info(self, id=None, username=None, password=None, vipExpirationDate=None, session=None):
        user = pd.read_excel(self.user_path)
        if session not in list(user['session']):
            return {"resCode": 1, "msg": "没有登入"}
        else:
            user_info = user[user['id'] == id]
            if username is not None:
                user.loc[user['id'] == id, 'username'] = username
            if password is not None:
                user.loc[user['id'] == id, 'password'] = password
            if vipExpirationDate is not None:
                user.loc[user['id'] == id, 'vipExpirationDate'] = vipExpirationDate
            user.to_excel(self.user_path, index=False)
            return {"resCode": 0}
    #
    def create_user_info(self, username, password, vipExpirationDate, session):
        user = pd.read_excel(self.user_path)
        if session not in list(user['session']):
            return {"resCode": 1, "msg": "没有登入"}
        else:
            new_data = {'username': username,
                        'password': password,
                        'vipExpirationDate': vipExpirationDate,
                        'session': session}
            user = user.append(new_data, ignore_index=True)
            user.to_excel(self.user_path, index=False)
            return {"resCode": 0}
    #

    #
    def send_message(self, newMessage, session, apiKey):
        user = pd.read_excel(self.user_path)
        if session not in list(user['session']):
            return {"resCode": 1, "msg": "没有登入或者注册"}
        else:
            user_info = user[user['session'] == session]
            vipExpirationDate = user_info['vipExpirationDate'].values[0]
            if datetime.strptime(vipExpirationDate, "%Y-%m-%d %H:%M:%S") < datetime.now():
                return {"resCode": 2, "msg": "vip已过期"}
            else:
                # 调用chatgpt函数进行文本生成
                chat = ChatGPT(apiKey)
                chat.set_mode('test')
                resMessage = chat.chat(prompt=newMessage)
                data = {'username': user_info['username'].values[0],
                        'userid': user_info['id'].values[0],  # 添加 userid 项
                        'apiKey': apiKey,
                        'newMessage': newMessage,
                        'resMessage': resMessage,
                        'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                message_log = pd.read_excel(self.message_log_path)
                message_log = message_log.append(data, ignore_index=True)
                message_log.to_excel(self.message_log_path, index=False)
                return {"resCode": 0, "resMessage": resMessage}

    def saveApiKey(self, session, apiKey):
        user = pd.read_excel(self.user_path)
        if session not in list(user['session']):
            return {"resCode": 1, "msg": "session不存在"}
        else:
            user.loc[user['session'] == session, 'apiKey'] = apiKey
            user.to_excel(self.user_path, index=False)
            return {"resCode": 0, "msg": "保存成功"}


class ChatGPT:
    def __init__(self, api_key):
        self.mode = 'production'
        openai.api_key = api_key

    def set_mode(self, mode):
        self.mode = mode

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()

    def chat(self, prompt):
        print('调用api', prompt)
        if self.mode == 'test':
            response = '测试1测试1'
        else:
            response = self.generate_response(prompt)
        print("答案：", response)
        return response

'''---------------------------------------------------------
api_key = "YOUR_API_KEY"
chat = ChatGPT(api_key)
chat.chat("What is the meaning of life?")
------------------------------------------------------------
'''



