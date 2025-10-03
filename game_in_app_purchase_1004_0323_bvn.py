# 代码生成时间: 2025-10-04 03:23:20
import streamlit as st
from streamlit.components.v1 import html

# 游戏内购系统
class GameInAppPurchase:
    def __init__(self):
        # 初始化游戏内购系统
        self.products = {
            'coin_pack_1000': {'price': 100, 'description': "1000 coins, 10% discount"},
            'coin_pack_5000': {'price': 500, 'description': "5000 coins, 20% discount"},
            'coin_pack_10000': {'price': 800, 'description': "10000 coins, 30% discount"},
        }
        self.purchased_products = []

    def display_product_options(self):
        # 显示游戏内购选项
        for product_id, product_info in self.products.items():
            st.write(f"Product ID: {product_id}")
            st.write(f"Price: ${product_info['price']}")
            st.write(f"Description: {product_info['description']}")

    def process_purchase(self, product_id):
        # 处理游戏内购订单
        if product_id in self.products:
            self.purchased_products.append(product_id)
            st.success("Purchase successful!")
        else:
            st.error("Invalid product ID")

    def run(self):
        # 运行游戏内购系统
        st.title("Game In-App Purchase System")
        self.display_product_options()
        
        purchase_button = st.button("Purchase")
        if purchase_button:
            product_id = st.selectbox("Select a product", list(self.products.keys()))
            self.process_purchase(product_id)

        if st.button("Show Purchased Products"):
            st.write("Purchased Products:")
            for product in self.purchased_products:
                st.write(product)

# 主函数
def main():
    game_purchase_system = GameInAppPurchase()
    game_purchase_system.run()

if __name__ == '__main__':
    main()