# 代码生成时间: 2025-10-10 22:07:49
import streamlit as st
import pandas as pd
import numpy as np
# TODO: 优化性能
import yfinance as yf
from datetime import datetime

"""
量化交易策略 Streamlit 应用
"""

# 设置 Streamlit 页面配置
st.set_page_config(page_title='Quantitative Trading Strategy', page_icon='📈')

# 定义主函数
def main():
    # 创建文本框，让用户输入股票代码
    ticker = st.text_input('输入股票代码:', 'AAPL')

    # 检查股票代码是否为空
# FIXME: 处理边界情况
    if ticker == '':
        st.error('股票代码不能为空！')
        return
# 改进用户体验

    # 下载股票数据
# 扩展功能模块
    try:
        data = yf.download(ticker, start=datetime(2020, 1, 1), end=datetime.now())
    except Exception as e:
        st.error(f'下载股票数据失败：{e}')
        return

    # 计算移动平均线
        # 短期移动平均线
        data['SMA_20'] = data['Close'].rolling(window=20).mean()
        # 长期移动平均线
        data['SMA_50'] = data['Close'].rolling(window=50).mean()
# NOTE: 重要实现细节

    # 绘制股票价格和移动平均线图
    st.line_chart(data[['Close', 'SMA_20', 'SMA_50']])

    # 买入和卖出信号
    # 当短期移动平均线上穿长期移动平均线时买入
    data['Buy_Signal'] = np.where((data['SMA_20'] > data['SMA_50']) & (data['SMA_20'].shift(1) <= data['SMA_50'].shift(1)), 1, 0)
    # 当短期移动平均线下穿长期移动平均线时卖出
    data['Sell_Signal'] = np.where((data['SMA_20'] < data['SMA_50']) & (data['SMA_20'].shift(1) >= data['SMA_50'].shift(1)), 1, 0)

    # 绘制买入和卖出信号图
    st.line_chart(data[['Buy_Signal', 'Sell_Signal']])

# 运行主函数
if __name__ == '__main__':
    main()