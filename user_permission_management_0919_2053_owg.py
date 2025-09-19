# 代码生成时间: 2025-09-19 20:53:40
import streamlit as st
from streamlit.elements import expander
from streamlit.code import code
import pandas as pd

"""
用户权限管理系统
"""

# 定义用户权限数据
USER_PERMISSIONS = {
    "user1": ["read", "write"],
    "user2": ["read"],
    "user3": ["write"]
}

"""
主页
"""
def main():
    st.title("用户权限管理系统")

    # 显示用户列表
    user_list = list(USER_PERMISSIONS.keys())
    user_expander = expander.Expander("用户列表")
    with user_expander:
        st.write(user_list)

    # 用户输入框
    user_input = st.text_input("请输入用户ID")
    if user_input:
        handle_user_input(user_input)

    # 添加用户按钮
    add_user_button = st.button("添加用户")
    if add_user_button:
        add_user()

    # 删除用户按钮
    delete_user_button = st.button("删除用户")
    if delete_user_button:
        delete_user()

"""
处理用户输入
"""
def handle_user_input(user_id):
    try:
        user_permissions = USER_PERMISSIONS.get(user_id, [])
        if not user_permissions:
            st.error(f"用户 {user_id} 不存在")
        else:
            st.write(f"用户 {user_id} 的权限：{user_permissions}")
    except Exception as e:
        st.error(f"处理用户输入时发生错误：{e}")

"""
添加用户
"""
def add_user():
    try:
        new_user_id = st.text_input("请输入新用户ID")
        if new_user_id and new_user_id not in USER_PERMISSIONS:
            USER_PERMISSIONS[new_user_id] = []
            st.success(f"用户 {new_user_id} 添加成功")
        else:
            st.error("用户ID已存在或输入无效")
    except Exception as e:
        st.error(f"添加用户时发生错误：{e}")

"""
删除用户
"""
def delete_user():
    try:
        user_id_to_delete = st.text_input("请输入要删除的用户ID")
        if user_id_to_delete in USER_PERMISSIONS:
            del USER_PERMISSIONS[user_id_to_delete]
            st.success(f"用户 {user_id_to_delete} 删除成功")
        else:
            st.error("用户ID不存在