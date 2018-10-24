

def Set_String(**kwargs):
    """
        重设数据
    :param kwargs:
    :return:
    """
    for key,value in kwargs.items():
        kwargs[key]  = str(value[0])
    return kwargs