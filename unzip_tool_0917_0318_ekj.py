# 代码生成时间: 2025-09-17 03:18:43
import streamlit as st
import zipfile
import os
def unzip_file(file_path, extract_to):
    """
    解压指定的zip文件到指定的目录
    :param file_path: zip文件路径
    :param extract_to: 解压目标目录
    """
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return f"文件解压成功，保存在{extract_to}"
    except zipfile.BadZipFile:
        return "文件格式不正确，无法解压"
    except Exception as e:
        return f"解压过程中发生错误：{e}"
def main():
    st.title('压缩文件解压工具')
    st.subheader('上传zip文件')
    uploaded_file = st.file_uploader("选择一个zip文件", type=['zip'], accept_multiple_files=False)
    if uploaded_file is not None:
        file_path = os.path.join(os.getcwd(), 'uploaded_file.zip')
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getvalue())
        extract_to = os.path.join(os.getcwd(), 'extracted')
        st.subheader('开始解压')
        st.write('解压后的文件将保存在当前目录下的extracted文件夹中')
        result = unzip_file(file_path, extract_to)
        st.write(result)
        if '保存在' in result:
            st.subheader('解压结果预览')
            st.write(f'解压结果文件夹：{extract_to}')
            st.image(os.path.join(extract_to, 'preview.jpg'))  # 假设解压后的文件夹中有一个名为preview.jpg的图片文件
if __name__ == '__main__':
    main()