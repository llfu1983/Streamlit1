import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config("图表渲染",page_icon="🔱",layout="wide")

"""
# 图表渲染
---
"""
st.info("st简单图表")
df = pd.DataFrame(np.random.randn(20,3),columns=["A","B","C"])
"这是折线图 st.line_chart(df)"
st.line_chart(df)
"这是面积图 st.area_chart(df)"
st.area_chart(df)
"这是棒棒图 st.bar_chart(df)"
st.bar_chart(df)

st.info("st简单图表")
st.pyplot(df.plot().figure,clear_figure=True)
"sdfsdf"
st.pyplot(df.boxplot().figure)
