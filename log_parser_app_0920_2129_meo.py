# 代码生成时间: 2025-09-20 21:29:52
import streamlit as st
import os
import re
from datetime import datetime

"""
Log Parser Application using Streamlit
"""

# 主函数，用于解析日志文件
@st.cache(allow_output_mutation=True)
def parse_log_file(log_content):
    # 定义日志解析模式
    log_pattern = re.compile(r'\[(.*?)\] (.*?)\: (.*)')
    logs = []
    for line in log_content.splitlines():
        match = log_pattern.match(line)
        if match:
            # 解构日志行
            timestamp, level, message = match.groups()
            # 格式化时间戳
            formatted_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
            logs.append({'time': formatted_time, 'level': level, 'message': message})
    return logs

"""
Streamlit前端页面
"""
def main():
    st.title('Log File Parser Tool')

    # 上传日志文件
    uploaded_file = st.file_uploader('Choose a log file', type=['log', 'txt'])
    if uploaded_file is not None:
        try:
            # 读取文件内容
            log_content = uploaded_file.read().decode('utf-8')
            # 解析日志文件
            parsed_logs = parse_log_file(log_content)
            
            # 展示解析结果
            st.subheader('Parsed Log Entries')
            for log in parsed_logs:
                st.write(f'Time: {log[