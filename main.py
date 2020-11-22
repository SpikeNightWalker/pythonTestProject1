import unittest

from common import CommonUtil
from common.ConfigUtil import YamlUtil

# 获得配置
yaml_config = YamlUtil.get_yaml()
# 获得测试用例目录
testcase_dir = CommonUtil.get_value_by_navigate_from_dict(YamlUtil.get_yaml(), "testcase.dir")
testcase_dir = CommonUtil.get_abspath(testcase_dir)
loader = unittest.TestLoader().discover(testcase_dir)

report_file = CommonUtil.get_value_by_navigate_from_dict(YamlUtil.get_yaml(), "testcase.reportFile")
report_file = CommonUtil.get_abspath(report_file)

with open(report_file, "w") as f:
    runner = unittest.TextTestRunner(f)
    runner.run(loader)





