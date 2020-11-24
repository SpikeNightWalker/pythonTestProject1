import pymysql
from common.ConfigUtil import YamlUtil
from common import CommonUtil
from common.LoggerUtil import MyLog

log = MyLog.get_log()
_yaml_content = YamlUtil.get_yaml()
_host = CommonUtil.get_value_by_navigate_from_dict(_yaml_content, "mysql.host", "localhost")
_port = CommonUtil.get_value_by_navigate_from_dict(_yaml_content, "mysql.port", 3306)
_user = CommonUtil.get_value_by_navigate_from_dict(_yaml_content, "mysql.user", "root")
_password = str(CommonUtil.get_value_by_navigate_from_dict(_yaml_content, "mysql.password", "123456"))
_charset = CommonUtil.get_value_by_navigate_from_dict(_yaml_content, "mysql.charset", "utf8")
_database = CommonUtil.get_value_by_navigate_from_dict(_yaml_content, "mysql.database", "utf8")

'''
注意：密码是字符串类型，charset设置为utf8（在mysql中utf8是utf-8的实现，两者是不同的）
游标读到的数据默认以tuple呈现，可以通过cursorclass=pymysql.cursors.DictCursor将返回值类型改为字典（其实是list<dict>）
'''

class HandleMysql:
    def __init__(self):
        try:
            self._conn = pymysql.connect(host=_host, port=_port, user=_user,
                                         password=_password, charset=_charset,
                                         database=_database, cursorclass=pymysql.cursors.DictCursor)
            # 获得游标，游标不能回头，跟SAX一样
            self._cur = self._conn.cursor()
        except:
            log.exception("数据库连接失败")
            raise

    def get_count(self, sql, args=None):
        return self._cur.execute(sql, args)

    def execute(self, sql, args=None):
        self._cur.execute(sql, args)
        return self._cur

    def close(self):
        self._cur.close()
        self._conn.close()


if __name__ == '__main__':
    mysql = HandleMysql()
    cur = mysql.execute("select * from member limit 10")
    print(cur.fetchmany(2))
    cur = mysql.execute("select * from member limit 10")
    print(cur.fetchmany(2))
    cur = mysql.execute("select count(*) from member where mobile_phone = %s", "123")
    print(cur.fetchall())
    mysql.close()



