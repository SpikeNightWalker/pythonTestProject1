from openpyxl import load_workbook
from openpyxl.cell.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

class HandleExcel:
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def _get_all_rows(self):
        '''
        从excel中获取所有行
        :return:
        '''
        workbook = load_workbook(self.file_name)
        sheet = workbook[self.sheet_name]
        sheet: Worksheet
        self.all_rows = list(sheet.rows)

    def _get_title_list(self):
        '''
        获取列标题
        :return:
        '''
        title_list = []
        for cell in self.all_rows[0]: # type: Cell
            title_list.append(cell.value)
        self.title_list = title_list

    def _get_body_list(self):
        '''
        获取内容行
        :return:
        '''
        self.result_list = []
        for row in self.all_rows[1:]:
            body_list = []
            for cell in row:
                body_list.append(cell.value)
            self.result_list.append(dict(zip(self.title_list, body_list)))

    def parseExcel(self):
        '''
        excel解析
        :return:
        '''
        self._get_all_rows()
        self._get_title_list()
        self._get_body_list()
        return self.result_list


# if __name__ == '__main__':
#     bean = HandleExcel("excels/2.xlsx", "one")
#     result_list = bean.parseExcel()
#     for item in result_list:
#         print(f"name:{item['name']}, age:{item['age']}")
#     print(result_list)





