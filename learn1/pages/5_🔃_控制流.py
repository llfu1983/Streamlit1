import streamlit as st
import numpy as np

st.set_page_config("控制流",layout="wide")

"""
# 控制流
---
## st.form 表单 && st.form_submit_button 表单提交按钮
"""

"""```python 
st.form(key: str, clear_on_submit: bool = False)")
参数：key：表单键名（注意，必须指定）。
clear_on_submit：是否在提交后清除表单内容。

st.form_submit_button(label='Submit') -> bool
注意，在st.form中，只有st.form_submit_button允许有回调函数。
"""

with st.form("calc"):
    num_1 = st.number_input("请输入第一个数",value=10)
    num_2 = st.number_input("请输入第二个数",value=10)
    if st.form_submit_button("计算乘积"):
        # st.write( "两个数的乘积是{0}".format(str(num_1*num_2)) )
        # "两个数的乘积是{0}".format(str(num_1*num_2))
        f"两个数的乘积是{num_1 * num_2}"

f"随机数:{np.random.randint(0,10000)}"
st.error("根据上面的随机数,说明表单提交后,也是整表重算")

"## st.stop立刻结束程序"

"""```python 
name = st.text_input('Name')
if not name:
    st.warning('Please input a name.')
    st.stop() # quit
st.success('Thank you for inputting a name.')
"""

"## st.experimental_rerun重新运行"
st.info("API说明这个实验,暂时不用")
