import xlrd


def read_excel(excel_path, sheet_name):
    """
        读取excel
    """
    result = []
    data = xlrd.open_workbook(excel_path)# 打开excel
    table = data.sheet_by_name(sheet_name) # Sheet名字
    for row in range(1, table.nrows):
        result.append(table.row_values(row))

    return result

if __name__ == "__main__":
    sheet_name = "Sheet1"
    excel_path = "接口测试用例模板.xlsx"
    result = read_excel(excel_path, sheet_name)
    print(result)


