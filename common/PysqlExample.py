import pymysql
from common.ConfigUtil import YamlUtil
from common import CommonUtil

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

conn = pymysql.connect(host=_host, port=_port, user=_user,
                       password=_password, charset=_charset,
                       database=_database, cursorclass=pymysql.cursors.DictCursor)
# 获得游标，游标不能回头，跟SAX一样
cur = conn.cursor()
# result = cur.execute("select * from member where mobile_phone = %s limit 10", "15853714489")
# 返回值result是查询到多少条
result = cur.execute("select * from member limit 10")
'''
获取第一条
默认获取的都是tuple
(0, '小柠檬', '25D55AD283AA400AF464C76D713C07AD', '18837465912', 0, Decimal('0.00'), datetime.datetime(2020, 11, 11, 21, 34, 24))
'''
print(type(cur.fetchone()))

'''
获取前3条，如果上面把索引0的记录获取了，那这里就会从索引1开始获取，即获取1-4条
((0, '小柠檬', '25D55AD283AA400AF464C76D713C07AD', '18837465912', 0, Decimal('0.00'), datetime.datetime(2020, 11, 11, 21, 34, 24)), (1, '柠檬草', '25D55AD283AA400AF464C76D713C07AD', '13241562185', 1, Decimal('11132130.60'), datetime.datetime(2020, 11, 11, 16, 38, 11)))
'''
print(cur.fetchmany(3))

'''
获取所有
((0, '小柠檬', '25D55AD283AA400AF464C76D713C07AD', '18837465912', 0, Decimal('0.00'), datetime.datetime(2020, 11, 11, 21, 34, 24)),
(1, '柠檬草', '25D55AD283AA400AF464C76D713C07AD', '13241562185', 1, Decimal('11132130.60'), datetime.datetime(2020, 11, 11, 16, 38, 11)))
'''
print(cur.fetchall())


# 释放资源
cur.close()
conn.close()


