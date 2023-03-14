import streamlit as st

st.set_page_config("布局与容器",layout="wide")

"""
# 布局与容器
---
## 布局

### 边栏
"""
st.sidebar.write("边栏内容")

st.sidebar.button('边栏按钮')

"""
### 并排列
"""

c1,c2,c3 = st.columns(3)
c1.error("c1")
c2.success("c2")
c3.warning("c3")

"""
### 折叠栏
"""
with st.expander("点击查看折叠内容",False):
    st.success("这是内部的内容")

    "可以使用st.expander来隐藏不需要立刻展示的部分，以优化布局空间。"
    "请注意，即使st.expander在折叠状态下，其内部内容也会被渲染。"
    "所以，如果内容较多，还是建议更多地利用st.cache等功能分页处理。"
    "但是折叠/展开不会重算,倒是不错"

    """```python 
    def myprint(str):
        ss = time.strftime("[%Y-%m-%d %H:%M:%S]: ", time.localtime()) + str
        print(ss)
    """

import numpy as np

"""
### 选项卡(分页卡)
"""
st.error("非常有用的功能")

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

"""
### st.container 容器

st.container是一个占位容器。

Streamlit是自上而下渲染的。

如果你需要调整对象显示的顺序，就可以先设置一个容器，然后将渲染后的内容写入容器里。
"""

"""```python 
container = st.container()
container.write("容器1")
st.write("容器外")
container.write("容器1")
"""
container = st.container()
container.write("容器1")
st.write("容器外")
container.write("容器1")

"""
### st.empty 单一元素空容器

st.empty也是一个占位容器，不同的是，st.empty只接收“一个”对象的写入，再次写入会覆盖此前的内容。

比如下面的案例（倒计时），就很适合用st.empty。
"""
import time
with st.empty():
    for seconds in range(3):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ Done!")