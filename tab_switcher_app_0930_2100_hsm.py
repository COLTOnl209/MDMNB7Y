# 代码生成时间: 2025-09-30 21:00:46
import streamlit as st

# 定义一个函数用于返回标签页内容

def get_tab_content(tab_name):
# 改进用户体验
    """根据标签页名称返回对应的内容。"""
# 优化算法效率
    if tab_name == 'Home':
        return "Welcome to the Home page!"
    elif tab_name == 'About':
        return "This is the About page."
    elif tab_name == 'Contact':
        return "You can contact us here."
    else:
        return "Unknown tab."

# 设置页面标题
st.title('Tab Switcher App')

# 创建标签页
tabs = ["Home", "About", "Contact"]

# 允许用户选择标签页
selected_tab = st.sidebar.selectbox(
    "Choose a tab", tabs, index=0
)

# 显示所选标签页的内容
st.write(get_tab_content(selected_tab))
