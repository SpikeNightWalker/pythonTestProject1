import json

from common import HttpUtil
from common.LoggerUtil import *
from common.ExcelUtil import *
from common.ConfigUtil import *
import unittest
from ddt import ddt, data

# 获得日志对象
log = MyLog.get_log()
# 获得excel内容
_excel_path = CommonUtil.get_value_by_navigate_from_dict(YamlUtil.get_yaml(), "excel.path")
_excel_path = CommonUtil.get_abspath(_excel_path)
_excel_sheet_name = CommonUtil.get_value_by_navigate_from_dict(YamlUtil.get_yaml(), "excel.sheetName")
_excel_content = HandleExcel(_excel_path, _excel_sheet_name).parseExcel()

@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.req = HttpUtil.HttpProcesser()
        pass

    @data(*_excel_content)
    def test_register_success(self, item):
        '''
        测试注册成功
        :param item:
        :return:
        '''
        resp = self.req.request(item.get("method"), item.get("url"), item.get("headers"), item.get("data"))
        expected = json.loads(item.get("expected"))
        expected_code = expected.get("code")
        expected_msg = expected.get("msg")
        try:
            self.assertEqual(expected_code, resp.get("code"))
            self.assertEqual(expected_msg, resp.get("msg"))
        except AssertionError:
            log.exception("断言失败")
            # raise表示抛出当前异常，不然会造成测试通过，因为AssertionError被你捕获了
            raise
        except Exception:
            log.exception("其他异常")
            raise







