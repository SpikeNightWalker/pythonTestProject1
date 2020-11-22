import yaml
import os
import pprint

from common import CommonUtil


class YamlUtil:
    '''
    Yaml处理类
    用于从yaml配置文件中读取字典，并持有该字典
    '''
    root_path = CommonUtil.get_abspath()
    _yaml_dict = None
    # with open(os.path.join(root_path, "config", "config.yml"), encoding="utf8") as config_file:
    with open(os.path.join(root_path, "config", "config.yml"), encoding="utf8") as config_file:
        content = config_file.read()
        _yaml_dict = yaml.load(content, yaml.FullLoader)
        # pprint.pprint(_yaml_dict)

    @classmethod
    def get_yaml(cls):
        '''
        类方法
        :return: 读取到的字典
        '''
        return cls._yaml_dict

