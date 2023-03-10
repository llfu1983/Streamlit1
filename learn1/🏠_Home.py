import streamlit as st

st.set_page_config("HH learn 1",page_icon="🧊",layout="wide")

st.sidebar.write("1️⃣ 111")

st.sidebar.write("2️⃣ 222")

"""
# 这是Streamlit的学习和测试文件
---
##  学习目标
- [多页面应用](https://docs.streamlit.io/library/get-started/multipage-apps)
    - markdown还是不错,可以大批量写入
    - 多页面无法多层,但是可以在页面里头加上sidebar
    - st.set_page_config("HH learn 1",page_icon="👋",layout="wide"),但是Emoji图标好像有问题
    - [Emoji表情](https://www.iludou.com/zongjie/56853)

- 基础的渲染效果,控件的简单应用
    - 文本的info,success,warning,error等都不错[link](https://santiago911-streamlit-experience-streamlit-experience-f92buw.streamlit.app/)
    - DataFrame直接魔术方法就很好;

- 缓存,全局变量,用户变量,页面变量的测试

- 数据库连接及交互控件的应用

- 布局、控制流和工具
"""