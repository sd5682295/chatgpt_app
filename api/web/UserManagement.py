import uuid

import pymysql
from datetime import datetime, timedelta

from api.web.main import ChatGPT


class UserManagement:

    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='password', db='mydb', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def login(self, username, password):
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `username`=%s"
            cursor.execute(sql, username)
            result = cursor.fetchone()
            if not result:
                session = uuid.uuid4().hex
                vipExpirationDate = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
                with self.db.cursor() as cursor:
                    sql = "INSERT INTO `user`(`id`, `username`, `password`, `session`, `vipExpirationDate`, `sessionTime`, `isManage`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (uuid.uuid4().hex, username, password, session, vipExpirationDate, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), False))
                    self.db.commit()
                return {"resCode": 0, "session": session, "vipExpirationDate": vipExpirationDate, "apiKey": result['apiKey'] if 'apiKey' in result else ''}
            else:
                if result['password'] != password:
                    return {"resCode": 1, "msg": "用户名或密码错误"}
                else:
                    session = uuid.uuid4().hex
                    with self.db.cursor() as cursor:
                        sql = "UPDATE `user` SET `session`=%s, `sessionTime`=%s WHERE `username`=%s"
                        cursor.execute(sql, (session, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), username))
                        self.db.commit()
                    return {"resCode": 0, "session": session, "vipExpirationDate": result['vipExpirationDate'], "apiKey": result['apiKey'] if 'apiKey' in result else ''}

    def check_session(self, session):
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `session`=%s"
            cursor.execute(sql, session)
            result = cursor.fetchone()
            if not result:
                return {"resCode": 1, "msg": "没有登入"}
            else:
                api_key = result['apiKey']
                vipExpirationDate = result['vipExpirationDate']
                return {"resCode": 0, "apiKey": api_key, "vipExpirationDate": vipExpirationDate}

    def getUserInfoList(self, session):
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `session`=%s"
            cursor.execute(sql, session)
            result = cursor.fetchone()
            if not result:
                return {'resCode': 1, 'msg': 'session不存在'}
            elif result['isManage']:
                with self.db.cursor() as cursor:
                    sql = "SELECT * FROM `user`"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                return {'resCode': 0, 'userInfoList': result}
            else:
                return {'resCode': 2, 'msg': '不是管理员'}

    def delete_user(self, id, session):
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `session`=%s"
            cursor.execute(sql, session)
            result = cursor.fetchone()
            if not result:
                return {"resCode": 1, "msg": "没有登入"}
            else:
                with self.db.cursor() as cursor:
                    sql = "DELETE FROM `user` WHERE `id`=%s"
                    cursor.execute(sql, id)
                    self.db.commit()
                return {"resCode": 0, 'msg': '删除成功'}

    def edit_user_info(self, id=None, username=None, password=None, vipExpirationDate=None, session=None):
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `session`=%s"
            cursor.execute(sql, session)
            result = cursor.fetchone()
            if not result:
                return {"resCode": 1, "msg": "没有登入"}
            else:
                if username is not None:
                    with self.db.cursor() as cursor:
                        sql = "UPDATE `user` SET `username`=%s WHERE `id`=%s"
                        cursor.execute(sql, (username, id))
                        self.db.commit()
                if password is not None:
                    with self.db.cursor() as cursor:
                        sql = "UPDATE `user` SET `password`=%s WHERE `id`=%s"
                        cursor.execute(sql, (password, id))
                        self.db.commit()
                if vipExpirationDate is not None:
                    with self.db.cursor() as cursor:
                        sql = "UPDATE `user` SET `vipExpirationDate`=%s WHERE `id`=%s"
                        cursor.execute(sql, (vipExpirationDate, id))
                        self.db.commit()
                return {"resCode": 0}

    def create_user_info(self, username, password, vipExpirationDate, session):
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `session`=%s"
            cursor.execute(sql, session)
            result = cursor.fetchone()
            if not result:
                return {"resCode": 1, "msg": "没有登入"}
            else:
                with self.db.cursor() as cursor:
                    sql = "INSERT INTO `user`(`id`, `username`, `password`, `vipExpirationDate`, `session`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (uuid.uuid4().hex, username, password, vipExpirationDate, session))
                    self.db.commit()
                return {"resCode": 0}

    def send_message(self, newMessage, session, apiKey):
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `session`=%s"
            cursor.execute(sql, session)
            result = cursor.fetchone()
            if not result:
                return {"resCode": 1, "msg": "没有登入或者注册"}
            else:
                vipExpirationDate = result['vipExpirationDate']
                if datetime.strptime(vipExpirationDate, "%Y-%m-%d %H:%M:%S") < datetime.now():
                    return {"resCode": 2, "msg": "vip已过期"}
                else:
                    # 调用chatgpt函数进行文本生成
                    chat = ChatGPT(apiKey)
                    chat.set_mode('test')
                    resMessage = chat.chat(prompt=newMessage)

                    # 插入消息记录
                    data = {'userid': result['id'], 'username': result['username'], 'apiKey': apiKey,
                            'newMessage': newMessage, 'resMessage': resMessage,
                            'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    with self.db.cursor() as cursor:
                        sql = "INSERT INTO `message_log`(`userid`, `username`, `apiKey`, `newMessage`, `resMessage`, `createTime`) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (result['id'], result['username'], apiKey, newMessage, resMessage,
                                             datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                        self.db.commit()
                    return {"resCode": 0, "resMessage": resMessage}

    def saveApiKey(self, session, apiKey):
        # 检查session是否存在
        sql = "SELECT COUNT(*) FROM {} WHERE session='{}'".format(self.user_table_name, session)
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        if not res[0]:
            return {"resCode": 1, "msg": "session不存在"}
        else:
            # 更新apiKey
            sql = "UPDATE {} SET apiKey='{}' WHERE session='{}'".format(self.user_table_name, apiKey, session)
            self.cursor.execute(sql)
            self.db.commit()
            return {"resCode": 0, "msg": "保存成功"}
