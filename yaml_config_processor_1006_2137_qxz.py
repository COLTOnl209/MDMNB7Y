# 代码生成时间: 2025-10-06 21:37:50
import streamlit as st
import yaml
from pathlib import Path

"""
YAML配置文件处理器
"""

"""
配置文件处理器的Streamlit应用
"""
class YamlConfigProcessor:
    def __init__(self, config_path):
        """
        初始化处理器，加载YAML配置文件
        :param config_path: YAML配置文件的路径
        """
        self.config_path = config_path
        self.config = None
        self.load_config()

    def load_config(self):
        """
        加载YAML配置文件
        """
        try:
            with open(self.config_path, 'r') as file:
                self.config = yaml.safe_load(file)
        except Exception as e:
            st.error(f"加载配置文件失败：{e}")
            self.config = None

    def display_config(self):
        """
        显示配置文件内容
        """
        if self.config is not None:
            st.write(self.config)
        else:
            st.error("配置文件为空或未加载")

    def update_config(self, key, value):
        "