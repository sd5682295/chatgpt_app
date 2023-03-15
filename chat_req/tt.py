import pandas as pd


def read_excel_file(filename, col_names):
    # 读取Excel文件，假设第一行是列名
    df = pd.read_excel(filename, header=0)

    # 处理包含逗号的列数据
    for col_name in col_names:
        if ',' in str(df[col_name]):
            # 将逗号分隔的字符串转换为列表
            df[col_name] = df[col_name].str.split(',')

    # 将DataFrame转换为字典列表
    data_list = df.to_dict('records')

    return data_list
if __name__ == '__main__':
    print(read_excel_file('chat_api.xlsx',['parameter']))