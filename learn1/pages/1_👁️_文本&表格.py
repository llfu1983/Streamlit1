import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config("渲染",page_icon="👁️",layout="wide")

"""
# 文本渲染显示
---
"""

st.info("浅色的注释 st.caption()")
"正常的字体"
st.caption("浅色的注释")

st.info("代码")
"""```python 
def myprint(str):
    ss = time.strftime("[%Y-%m-%d %H:%M:%S]: ", time.localtime()) + str
    print(ss)
"""

"""
# 指标渲染显示
---
"""
st.info("单个指标")
st.metric(label="温度", value="70 °F", delta="1.2 °F")

st.info("一行多个指标")
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric(label="温度", value="70 °F", delta="1.2 °F")
c2.metric(label="Number1", value=None, delta="-15")
c3.metric(label="Number2", value=666,delta=166,delta_color="inverse")
c4.metric(label="HelloWorld",value="刘志昱",delta="说",delta_color="off")
c5.metric(label="温度", value="70 °F", delta="1.2 °F")

"""
# 表格渲染显示
---
"""

df_1_1 = pd.DataFrame(np.random.randint(0,10,(400,30)))

"""```python 
df_1_1 = pd.DataFrame(np.random.randint(0,10,(400,30)))
"""
st.caption("这样写的是页面变量")

st.info("DataFrame,size=(400,30)")
df_1_1

st.info("DataFrame,size=(4,3)")
df_1_1.iloc[:4,:3]

st.info("DataFrame table,size=(4,3)")
st.table(df_1_1.iloc[:4,:3])
st.caption("st.table的写法是静态table,不好用")

"""
# json渲染显示
---
"""
st.json(df_1_1.iloc[:4,:3].to_json())