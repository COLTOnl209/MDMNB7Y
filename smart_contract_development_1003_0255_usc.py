# 代码生成时间: 2025-10-03 02:55:24
import streamlit as st
from web3 import Web3
from solcx import compile_standard, install_solc

# 安装Solidity编译器
install_solc('0.8.0')

# 定义智能合约字符串
SMART_CONTRACT_CODE = """
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint storedData;

    constructor() {
        storedData = 0;
    }

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
"""

# 编译智能合约
compiled_sol = compile_standard({'language': 'Solidity', 'sources': {'': {'content': SMART_CONTRACT_CODE}}, 'settings': {'outputSelection': {'*': {'*': ['*']}}}})

# 获取abi和字节码
abi = compiled_sol['contracts']['']['SimpleStorage']['abi']
bytecode = compiled_sol['contracts']['']['SimpleStorage']['bin']

# Streamlit界面
def main():
    st.title('智能合约开发工具')
    
    with st.form('deploy_form'):
        # 获取用户输入的参数
        input_value = st.number_input('请输入初始化值 (可选)', min_value=0, max_value=100, value=0)
        submit_button = st.form_submit_button(label='部署智能合约')
    
    if submit_button:
        try:
            # 连接到以太坊节点
            w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

            # 检查节点是否连接成功
            if not w3.isConnected():
                st.error('无法连接到以太坊节点，请检查节点状态。')
                return

            # 从账户中解锁以部署合约
            account = w3.eth.accounts[0]
            w3.eth.personal.unlockAccount(account, '')

            # 部署智能合约
            SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
            tx_hash = SimpleStorage.constructor().transact()
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            # 显示合约地址和存储值
            contract_address = tx_receipt.contractAddress
            if contract_address:
                st.success(f'智能合约已部署至地址：{contract_address}')
                # 调用合约函数设置和获取值
                set_value_tx_hash = SimpleStorage.functions.set(input_value).transact({'from': account})
                w3.eth.wait_for_transaction_receipt(set_value_tx_hash)
                get_value = SimpleStorage.functions.get().call({'from': account})
                st.write(f'存储的值：{get_value}')
            else:
                st.error('智能合约部署失败。')
        except Exception as e:
            st.error(f'发生错误：{e}')

if __name__ == '__main__':
    main()
