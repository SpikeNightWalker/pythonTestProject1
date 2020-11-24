import traceback
import os
from random import randint

# 项目根路径，在该文件的上两级
_root_path = os.path.abspath(__file__ + "/../..")

_phone_prefix = [133, 130, 135]

def get_value_by_navigate_from_dict(dict_obj, navigate, default_value=None):
    '''
    通过导航从字典中取值
    导航就是类似这样的格式：log.file.name
        一路导航到想要的节点
    :param dict_obj: 源字典
    :param navigate: 导航
    :param default_value: 默认值
    :return: 如果导航获得空值或抛了异常，则返回默认值，否则返回导航到的值
    '''
    if dict_obj and navigate:
        try:
            sub_dict_obj = dict_obj
            for key in navigate.split("."):
                sub_dict_obj = sub_dict_obj.get(key, default_value)
            return sub_dict_obj
        except Exception as e:
            traceback.print_exc()
            return default_value
    else:
        return default_value

def get_abspath(*relative_path):
    if relative_path:
        path = os.path.join(_root_path, *relative_path)
        # print(path)
        return path
    return _root_path

def get_phone_number():
    '''
    随机生成手机号
    :return:
    '''
    prefix_three = str(_phone_prefix[randint(0, len(_phone_prefix) - 1)])
    suffix_eight = str(randint(10000000, 99999999))
    return prefix_three + suffix_eight

print(get_phone_number())



