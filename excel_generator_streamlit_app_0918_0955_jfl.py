# 代码生成时间: 2025-09-18 09:55:28
import streamlit as st
import pandas as pd
from openpyxl import Workbook

"""
Excel表格自动生成器 Streamlit 应用
"""

# 初始化 Streamlit 应用标题
st.title('Excel表格自动生成器')

# 定义一个生成 Excel 文件的函数
def generate_excel_file(data, filename):
    try:
        wb = Workbook()
        ws = wb.active
        # 将数据写入 Excel
        for row in data:
            ws.append(row)
        # 保存 Excel 文件
        wb.save(filename)
        return filename
    except Exception as e:
        st.error(f'生成Excel文件时出错: {e}')
        return None

# 获取用户输入的数据
with st.form(key='data_form'):
    data_input = st.text_area(label='输入数据，每行一个值，用逗号分隔')
    submit_button = st.form_submit_button(label='生成Excel')

# 当用户提交表单时执行
if submit_button:
    # 解析用户输入的数据
    data_list = data_input.split('
')
    # 将每行数据分割为单独的元素，创建二维列表
    data_list = [line.split(',') for line in data_list]
    # 移除空行
    data_list = [line for line in data_list if line]

    # 生成 Excel 文件
    filename = 'generated_excel.xlsx'
    generated_file = generate_excel_file(data_list, filename)

    # 如果生成成功，显示下载链接
    if generated_file:
        st.download_button(
            label='下载生成的Excel文件',
            data=open(generated_file, 'rb').read(),
            file_name=generated_file,
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    else:
        st.error('未能生成Excel文件。')
