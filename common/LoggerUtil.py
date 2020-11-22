import logging
from logging import handlers

from common import CommonUtil
from common.ConfigUtil import *


# def get_or_default(value, default_value):
#     '''
#     用于过滤空值
#     如果value为空，则返回default_value
#     :param value:
#     :param default_value:
#     :return:
#     '''
#     return value if value else default_value

def _get_log():
    '''
    通过YamlUtil类获取yaml字典
    通过字典中的参数生成日志对象
    :return: 日志对象
    '''
    yaml_dict = YamlUtil.get_yaml()
    #使用导航方式获得配置文件中的参数
    name = CommonUtil.get_value_by_navigate_from_dict(yaml_dict, "log.name", "myLog")
    format = CommonUtil.get_value_by_navigate_from_dict(yaml_dict, "log.format", "%(asctime)s %(name)s %(levelname)s %(filename)s line:%(lineno)d %(message)s")
    level = CommonUtil.get_value_by_navigate_from_dict(yaml_dict, "log.level", "INFO")
    file_backup_count = CommonUtil.get_value_by_navigate_from_dict(yaml_dict, "log.file.backupCount", 5)
    file_encoding = CommonUtil.get_value_by_navigate_from_dict(yaml_dict, "log.file.encoding", "utf8")
    file_maxBytes = CommonUtil.get_value_by_navigate_from_dict(yaml_dict, "log.file.maxBytes", 1024)
    if file_maxBytes:
        file_maxBytes = eval(file_maxBytes)
    file_path = CommonUtil.get_value_by_navigate_from_dict(yaml_dict, "log.file.path", "../output/logs/testProject.log")
    file_path = CommonUtil.get_abspath(file_path)
    #创建日志对象
    log = logging.getLogger(name)
    log.setLevel(level)
    fmt = format
    formatter = logging.Formatter(fmt)
    #创建控制台处理器
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    log.addHandler(handler)
    #如果日志目录不存在，则创建目录
    parent_dir = os.path.dirname(file_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
    #创建文件日志处理器
    file_handler = handlers.RotatingFileHandler(file_path, encoding=file_encoding, maxBytes=file_maxBytes, backupCount=file_backup_count)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    return log

class MyLog():
    '''
    持有日志对象
    '''
    _log = _get_log()

    @classmethod
    def get_log(cls):
        '''
        :return: 日志对象
        '''
        return cls._log







