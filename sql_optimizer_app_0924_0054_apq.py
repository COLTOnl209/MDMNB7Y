# 代码生成时间: 2025-09-24 00:54:01
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Define the function to connect to the database
def connect_to_database(db_url):
    try:
        engine = create_engine(db_url)
        return engine
    except Exception as e:
        st.error(f"Failed to connect to database: {e}")
        return None

# Define the function to optimize SQL queries
def optimize_query(sql_query, engine):
    try:
        # This is a placeholder for actual query optimization logic
        # In a real scenario, this would involve analyzing the query and making
        # recommendations on how to improve its performance.
        # For demonstration, we'll just return the original query.
        optimized_query = f"-- Optimized query
{sql_query}"
        return optimized_query
    except Exception as e:
        st.error(f"Failed to optimize query: {e}")
        return None

# Streamlit app
def main():
    st.title('SQL Query Optimizer')

    # Ask for database connection details
    db_url = st.text_input('Database URL', 'postgresql://user:password@host:port/dbname')
    if db_url:
        engine = connect_to_database(db_url)
        if engine:
            # Ask for a SQL query
            sql_query = st.text_area('Enter SQL Query', height=300)
            if sql_query:
                # Optimize the query
                optimized_query = optimize_query(sql_query, engine)
                if optimized_query:
                    st.code(optimized_query, language='sql')
                else:
                    st.error('No optimized query available.')
            else:
                st.error('Please enter a SQL query to optimize.')
        else:
            st.error('Please check your database connection details.')
    else:
        st.error('Please enter a valid database URL.')

if __name__ == '__main__':
    main()