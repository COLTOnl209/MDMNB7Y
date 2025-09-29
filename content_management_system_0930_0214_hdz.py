# 代码生成时间: 2025-09-30 02:14:24
import streamlit as st
from streamlit.components.v1 import html
import json
import os

# 定义内容管理系统类
class ContentManagementSystem:
    def __init__(self):
        # 初始化数据库文件
        self.db_path = 'content.db.json'
        self.load_db()

    def load_db(self):
        """加载数据库文件"""
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump({}, f)
        else:
            with open(self.db_path, 'r') as f:
                self.db = json.load(f)
        else:
            self.db = {}

    def save_db(self):
        """保存数据库文件"""
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f)

    def add_content(self, title, content):
        """添加内容"""
        if title in self.db:
            st.error('内容已存在')
        else:
            self.db[title] = content
            self.save_db()
            st.success('内容添加成功')

    def update_content(self, title, content):
        """更新内容"""
        if title not in self.db:
            st.error('内容不存在')
        else:
            self.db[title] = content
            self.save_db()
            st.success('内容更新成功')

    def delete_content(self, title):
        """删除内容"""
        if title in self.db:
            del self.db[title]
            self.save_db()
            st.success('内容删除成功')
        else:
            st.error('内容不存在')

    def display_content(self):
        """展示所有内容"""
        for title, content in self.db.items():
            st.subheader(title)
            st.write(content)

# 初始化内容管理系统
cms = ContentManagementSystem()

def main():
    """主函数"""
    cms.load_db()

    with st.form('content_form'):
        title = st.text_input('标题')
        content = st.text_area('内容')
        button_add = st.form_submit_button(label='添加内容')
        button_update = st.form_submit_button(label='更新内容')
        button_delete = st.form_submit_button(label='删除内容')

        if button_add:
            cms.add_content(title, content)
        elif button_update:
            cms.update_content(title, content)
        elif button_delete:
            cms.delete_content(title)

    st.subheader('所有内容')
    cms.display_content()

if __name__ == '__main__':
    main()