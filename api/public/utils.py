from flask import jsonify

from api.public.snap import snap_t
class call_return_base:
    @staticmethod
    def success(self, data="", msg='ok', code=0):
        '''
        返回成功信息
        :param data: <any>[""]
        :param msg:<string>['ok']
        :param code:<int>[0]
        :return:<dict>[{'code': 0, 'msg': 'ok', 'data': ""}]
        '''
        pass

    @staticmethod
    def failure(self, data="", msg='failure', code=1):
        '''
        返回失败信息
        :param data: <any>[""]
        :param msg:<string>['failure']
        :param code:<int>[1]
        :return:<dict>[{'code': 1, 'msg': 'failure', 'data': ""}]
        '''
        pass
err_list={
    4003:'密码错误'
}

class call_return(call_return_base):
    @staticmethod
    def success(data="", msg='ok', code=0):
        return {'code': code, 'msg': msg, 'data': data}

    @staticmethod
    def failure(data="", msg='failure', code=False):
        if code:
            if code in err_list:
                if msg=='failure':
                    return {'code': code, 'msg': err_list[int(code)], 'data': data}
                else:
                    return {'code': code, 'msg': msg, 'data': data}
            else:
                return {'code': code, 'msg': msg, 'data': data}

        return {'code': 1, 'msg': msg, 'data': data}

    @staticmethod
    def send_js(fun):
        def in_fun(*args,**kwargs):
            res = fun(*args,**kwargs)
            if type(res)==str:
                res = {'data':res}
            if type(res) != type(jsonify({'a':'b'})):
                res = jsonify(res)
            return res
        return in_fun

class test_call_return(call_return_base):
    def test_success(self):
        snap_t(msg='test_success')
        snap_t(call_return().success(), msg='test_success_def',acc_data={'code': 0, 'msg': 'ok', 'data': ''})
        snap_t(call_return().success(data='aa', msg='bb',code=10), msg='test_success_aa',acc_data={'code': 10, 'msg': 'bb', 'data': 'aa'})

    #
    def test_failure(self):
        snap_t(msg='test_failure')
        snap_t(call_return().failure(), msg='test_failure_def', acc_data={'code': 1, 'msg': 'failure', 'data': ''})
        snap_t(call_return().failure(data='aa', msg='bb', code=10), msg='test_failure_aa',
               acc_data={'code': 10, 'msg': 'bb', 'data': 'aa'})


if __name__ == '__main__':
    test_call_return().test_success()
    test_call_return().test_failure()