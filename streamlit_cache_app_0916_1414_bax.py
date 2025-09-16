# 代码生成时间: 2025-09-16 14:14:19
import streamlit as st
from functools import lru_cache
import time

"""
Streamlit application to demonstrate caching mechanism.

This app will show how to use the caching feature in Streamlit to optimize
repetitive calculations or data fetching operations."""

# Define a function to simulate a time-consuming operation
@lru_cache(maxsize=32)
def expensive_operation(x):
    """Simulate an expensive operation using a time delay."""
    time.sleep(2)  # Simulating a time-consuming task
    return x * x

# Streamlit interface
def main():
    st.title('Streamlit Caching Demo')
    
    # Input for the user
    number = st.number_input('Enter a number', min_value=1, max_value=100, value=10)
    
    # Button to trigger the computation
    if st.button('Compute Square'):
        try:
            # Retrieve result from cache if available
            result = expensive_operation(number)
            st.success(f'Square of {number} is {result}')
        except Exception as e:
            st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()