import openpyxl as excel

from phyengine.MathEngine import FIRST, LAST
from phyengine import MathEngine

LAST = -1
FIRST = 0

EXCEL = 'xslx'
TXT = 'txt'

class RecordableValue:
    def __init__(self, x_expression: str = "0", y_expression: str = "0", window = None, **kwargs):
        self.kwargs = kwargs
        def check_expr(self, expr: str):
            new_expr = expr
            for item in kwargs.keys():
                new_expr = new_expr.replace(item, "self.kwargs['{}']".format(item))
            try:
                eval(new_expr)
            except Exception as error:
                print(error)
                raise ValueError("can not calculate expression {}".format(new_expr))
            return new_expr
        self.data: MathEngine.DataSet = MathEngine.DataSet()
        self.x_expr = check_expr(self, x_expression)
        self.y_expr = check_expr(self, y_expression)
        self.window = window
        if window: self.window.InitObjects(self)

    def record(self):
        self.data.append(eval(self.x_expr), eval(self.y_expr))

    def save(self, name: str = "temp", file_type = TXT):
        if file_type == TXT:
            with open('{}.txt'.format(name), 'w') as file:
                file.write('\n'.join(map(lambda k: '{}!{}'.format(*k), self.data)))
            print(self.data.data_)
        elif file_type == EXCEL:
            book = excel.Workbook()
            excel_data = book.create_sheet('Data', 0)
            for row in self.data:
                excel_data.append(row)
            book.save('{}.xlsx'.format(name))