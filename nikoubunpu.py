import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import japanize_matplotlib


st.title('身近な統計 補助教材')
st.header("二項分布")
st.markdown("#")

st.markdown("""
- 成功確率と試行回数をスライドバーで入力します。
- 値を変更することで、分布がどのように変化するか確認してみましょう。
""")
st.markdown("#")


st.write("Step1:成功確率pと試行回数nをスライドバーで入力します。")
p = st.slider('成功確率p：', 0.0, 1.0, 0.5)
n = st.slider("試行回数n：", 0, 170, 50)
st.markdown("#")

# グラフの描画
x = np.arange(0, n, 1)
y = stats.binom.pmf(x, n, p)

fig, ax = plt.subplots()
ax.plot(x, y)
# x 軸のラベルを設定する。
ax.set_xlabel("確率")
# y 軸のラベルを設定する。
ax.set_ylabel("成功回数")
st.pyplot(fig)
