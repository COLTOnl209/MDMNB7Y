# 代码生成时间: 2025-09-19 11:21:47
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.exc import SQLAlchemyError
import os

# 数据库配置
DATABASE_URI = 'postgresql://user:password@localhost:5432/mydatabase'

# 创建数据库引擎
def create_db_engine(uri):
    return create_engine(uri)

# 迁移数据库函数
def migrate_database(engine, migration_script):
    with engine.connect() as connection:
        try:
            connection.execute(migration_script)
            print("Database migration completed successfully.")
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")

# Streamlit界面
def main():
    st.title('Database Migration Tool')
    
    # 输入数据库URI
    db_uri = st.text_input('Database URI', DATABASE_URI)
    
    # 输入迁移脚本
    migration_script = st.text_area('Migration Script')
    
    # 执行迁移按钮
    if st.button('Migrate Database'):
        try:
            # 创建数据库引擎
            db_engine = create_db_engine(db_uri)
            
            # 执行迁移
            migrate_database(db_engine, migration_script)
            st.success('Migration completed successfully!')
        except Exception as e:
            st.error(f'An error occurred: {e}')
            
if __name__ == '__main__':
    main()