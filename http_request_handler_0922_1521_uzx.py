# 代码生成时间: 2025-09-22 15:21:40
import streamlit as st
from streamlit.components.v1 import html
import requests
import json

"""
HTTP Request Handler using Streamlit

This application creates a simple HTTP request handler using Streamlit framework.
It allows users to make HTTP requests to any URL and view the response.
"""

# Function to handle HTTP requests
def handle_http_request(method, url, headers=None, params=None, data=None):
    """
    Handles HTTP requests and returns the response.

    Args:
        method (str): HTTP method (GET, POST, PUT, DELETE)
        url (str): URL to make the request to
        headers (dict, optional): Headers for the request. Defaults to None.
        params (dict, optional): Query parameters for the request. Defaults to None.
        data (dict, optional): Data to send in the request body. Defaults to None.

    Returns:
        dict: HTTP response
    """
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        return {"error": str(e)}

# Streamlit UI
def main():
    st.title('HTTP Request Handler')

    # Input fields for request details
    method = st.selectbox('HTTP Method', ['GET', 'POST', 'PUT', 'DELETE'])
    url = st.text_input('URL', 'https://jsonplaceholder.typicode.com/')
    headers = st.text_area('Headers (JSON)', json.dumps({
        'Content-Type': 'application/json'
    }, indent=4), height=100)
    params = st.text_area('Query Parameters (JSON)', '{}', height=100)
    data = st.text_area('Request Body (JSON)', '{}', height=100)

    # Execute the HTTP request when the button is clicked
    if st.button('Send Request'):
        try:
            # Parse headers, params, and data from text inputs
            headers = json.loads(headers) if headers else None
            params = json.loads(params) if params else None
            data = json.loads(data) if data else None

            # Call the HTTP request handler function
            response = handle_http_request(method, url, headers=headers, params=params, data=data)

            # Display the response
            if 'error' in response:
                st.error('Error:', response['error'])
            else:
                st.json(response)
        except json.JSONDecodeError as e:
            st.error('Invalid JSON:', str(e))

if __name__ == '__main__':
    main()