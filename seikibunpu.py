import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import japanize_matplotlib


st.title('身近な統計 補助教材')
st.header("正規分布")

st.write("""
### 平均μと標準偏差σ（>0）をスライドバーで入力してください。
""")

m = st.slider('平均μ：', -10.0, 10.0, 0.0)

s = st.slider('標準偏差σ', 0.0, 10.0, 1.0)

# グラフの描画
x = np.arange(-4, 4, 0.1)
y = norm.pdf(x, m, s)

fig, ax = plt.subplots()
ax.plot(x, y)
# x 軸のラベルを設定する。
ax.set_xlabel("確率変数")
# y 軸のラベルを設定する。
ax.set_ylabel("確率密度")
st.pyplot(fig)
