# 代码生成时间: 2025-09-23 00:03:44
import streamlit as st
from streamlit.components.v1 import html

# Streamlit页面设置
def setup_page():
    st.title('Payment Process')
    st.subheader('Step 1: Enter Payment Details')
    st.subheader('Step 2: Confirm Payment')
    st.subheader('Step 3: Payment Result')

# 输入支付详情
def input_payment_details():
    with st.form(key='payment_form'):
        # 输入字段
        user_name = st.text_input('User Name')
        payment_amount = st.number_input('Payment Amount', min_value=0.01)
        payment_method = st.selectbox('Payment Method', ('Credit Card', 'Debit Card', 'PayPal'))
        # 提交按钮
        submit_button = st.form_submit_button(label='Submit Payment')
    return user_name, payment_amount, payment_method, submit_button

# 确认支付信息
def confirm_payment_details(user_name, payment_amount, payment_method):
    st.subheader('Payment Confirmation')
    st.write(f'User Name: {user_name}')
    st.write(f'Payment Amount: ${payment_amount}')
    st.write(f'Payment Method: {payment_method}')
    confirm_button = st.button('Confirm Payment')
    return confirm_button

# 支付结果处理
def payment_result(confirmed):
    if confirmed:
        st.success('Payment Successful!')
    else:
        st.warning('Payment not confirmed.')

# 主函数
def main():
    setup_page()
    user_name, payment_amount, payment_method, submit_button = input_payment_details()
    if submit_button:
        confirmed = confirm_payment_details(user_name, payment_amount, payment_method)
        payment_result(confirmed)

# 运行应用程序
if __name__ == '__main__':
    main()