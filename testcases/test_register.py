import json

from common import HttpUtil
from common.LoggerUtil import *
from common.ExcelUtil import *
from common.ConfigUtil import *
import unittest
from ddt import ddt, data
from common.MysqlUtil import HandleMysql

# 获得日志对象
log = MyLog.get_log()
# 获得excel内容
_excel_path = CommonUtil.get_value_by_navigate_from_dict(YamlUtil.get_yaml(), "excel.path")
_excel_path = CommonUtil.get_abspath(_excel_path)
_excel_sheet_name = CommonUtil.get_value_by_navigate_from_dict(YamlUtil.get_yaml(), "excel.sheetName")
_excel_content = HandleExcel(_excel_path, _excel_sheet_name).parseExcel()





@ddt
class TestRegister(unittest.TestCase):

    def get_new_phone(self):
        while True:
            phone_number = CommonUtil.get_phone_number()
            count = self.mysql.get_count("select * from member where mobile_phone = %s", phone_number)
            if 0 == count:
                return phone_number

    @classmethod
    def setUpClass(cls) -> None:
        cls.req = HttpUtil.HttpProcesser()
        cls.mysql = HandleMysql()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.mysql.close()

    @data(*_excel_content)
    def test_register_success(self, item):
        '''
        测试注册成功
        :param item:
        :return:
        '''
        data = json.loads(item.get("data")) # type: dict
        data.update({"mobile_phone":self.get_new_phone()})
        log.debug("data=%s", data)
        resp = self.req.request(item.get("method"), item.get("url"), item.get("headers"), data)
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







