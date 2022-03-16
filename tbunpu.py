import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import japanize_matplotlib


st.title('身近な統計 補助教材')
st.header("t分布")

st.write("""
### 自由度ν（>0）をスライドバーで入力してください。
""")

jiyuudo = st.slider('自由度ν：', 0.0, 100.0, 5.0)

# グラフの描画
x = np.arange(-4, 4, 0.1)
y = stats.t.pdf(x, jiyuudo)

fig, ax = plt.subplots()
ax.plot(x, y)
# x 軸のラベルを設定する。
ax.set_xlabel("確率変数")
# y 軸のラベルを設定する。
ax.set_ylabel("確率密度")
st.pyplot(fig)