# 代码生成时间: 2025-09-16 01:01:55
import streamlit as st
from sqlalchemy import create_engine, select, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import safe
def create_db_session():
    # 创建数据库连接（这里需要配置你的数据库信息）
    engine = create_engine('YOUR_DATABASE_URI', echo=False)
    Session = sessionmaker(bind=engine)
    return Session()

def get_user_by_id(session, user_id):
    # 使用safe对象防止SQL注入
    user = session.execute(select([user_table]).where(user_table.c.id == safe(user_id))).scalar_one_or_none()
    if user is None:
        raise ValueError("User not found.")
    return user

def main():
    st.title('SQL Injection Protection with Streamlit')
    user_id_input = st.text_input('Enter User ID to Search', '')
    if st.button('Search User'):
        try:
            with create_db_session() as session:
                user = get_user_by_id(session, user_id_input)
                st.write(f"User ID: {user['id']}, Username: {user['username']}")  # 访问user属性时需根据实际数据库表结构调整
        except ValueError as ve:
            st.error(str(ve))
        except SQLAlchemyError as e:
            st.error(f"Database error: {e}")

if __name__ == '__main__':
    main()