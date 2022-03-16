import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import japanize_matplotlib


st.title('身近な統計 補助教材')
st.header("ポアソン分布")

st.write("""
### 平均λ（>0）をスライドバーで入力してください。
""")

heikin = st.slider('平均λ：', 0.0, 15.0, 1.0)

# グラフの描画
x = np.arange(0, 20, 1)
y = stats.poisson.pmf(x, heikin)

fig, ax = plt.subplots()
ax.plot(x, y)
# x 軸のラベルを設定する。
ax.set_xlabel("発生回数")
# y 軸のラベルを設定する。
ax.set_ylabel("確率")
st.pyplot(fig)
