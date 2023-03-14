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
"用web感觉很奇怪,用手机看到时还好"
st.pyplot(df.plot().figure,clear_figure=True)
"连续2个图,组图测试不行"
st.pyplot(df.boxplot().figure,clear_figure=True)

"---"
st.info("st.pyplot,用figure传参数")
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif']=['STXihei']  # SimHei
rcParams['axes.unicode_minus']=False #用来正常显示负号

fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(211)
ax1.plot(df.index,df["A"],label='折线图')
ax1.plot(df.index,df["B"],label='折线图')
ax1.plot(df.index,df["C"],label='折线图')

ax2 = fig.add_subplot(223)
ax2.violinplot(df,showmeans=False,showmedians=True)	# 小提琴图

ax3 = fig.add_subplot(224)
ax3.boxplot(df,labels=df.columns,showmeans=True)	# 箱线图
st.pyplot(fig,clear_figure=True)
