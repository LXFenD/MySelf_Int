from django.http import JsonResponse


class Restful_Api():
    """
    定义resetapi接口协议
    """
    ok = 200
    param_error = 400
    unauth = 403
    server_error = 500





def Restful_api(code=Restful_Api.ok,message=None,data=None,kwargs=None):
    """

    :param code: 返回请求码
    :param message:  返回请求信息
    :param data:  返回数据
    :param kwargs:  其他数据
    :return:
    """
    json_dict = {'code':code,'message':message,'data':data}
    if kwargs and kwargs.keys() and isinstance(kwargs,dict):
        json_dict.update(kwargs)
    response = JsonResponse(json_dict)
    response.setdefault('Access-Control-Origin', '*')
    response.setdefault('Access-Control-Allow-Origin', '*')
    response.setdefault('Access-Control-Allow-Methods', '*')
    response.setdefault('Access-Control-Allow-Headers', 'content_type')
    return response


def ok(data=None,message="请求成功",):
    """
    请求成功
    :param data:
    :return:
    """
    return Restful_api(message=message,data=data)

def param_error(message="请求参数错误！！",data=None):
    """
    请求参数错误失败
    :param data:
    :return:
    """
    return Restful_api(code=Restful_Api.param_error,message=message,data=data)


def unauth(data=None,message="无权限！！",):
    """
    请求没有用户权限
    :param data:
    :return:
    """
    return Restful_api(code=Restful_Api.unauth,message=message,data=data)


def server_error(data=None,message="服务器逻辑出错！！",):
    """
    请求服务器出错！！
    :param data:
    :return:
    """
    return Restful_api(code=Restful_Api.server_error,message=message,data = data)


