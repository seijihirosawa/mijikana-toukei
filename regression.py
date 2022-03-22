import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import japanize_matplotlib
import random
import seaborn as sns
from sklearn.linear_model import LinearRegression


st.title('身近な統計 補助教材')
st.header("データと回帰直線")
st.markdown("#")

st.markdown("""
- 乱数から5点のx,y座標を抽出して回帰直線を引きます。
- 値を追加することで、回帰直線がどのように変化するか確認してみましょう。
""")
st.markdown("#")


def make_graph(x, y):
    with placeholder3:
        lr = LinearRegression()
        lr.fit(st.session_state.x, st.session_state.y)

        fig, ax = plt.subplots()
        ax.scatter(st.session_state.x, st.session_state.y)
        ax.set_xlim([0, 100])
        ax.set_ylim([0, 100])
        ax.plot(st.session_state.x, lr.predict(st.session_state.x), color="red",
                label="回帰直線")
        ax.set_xlabel("xの値", fontsize=12)
        ax.set_ylabel("yの値", fontsize=12)

        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
                  borderaxespad=0, fontsize=10)
        st.pyplot(fig)

    with placeholder4:
        st.write(
            '回帰式：y = '+str(round(lr.intercept_[0], 2)) +
            'x'+'{:+}'.format(round(lr.coef_[0][0], 2)))


placeholder1 = st.empty()
placeholder2 = st.empty()
st.markdown("#")
st.markdown("#")
placeholder3 = st.empty()
placeholder4 = st.empty()
st.markdown("#")
st.markdown("#")
placeholder5 = st.empty()
placeholder6 = st.empty()

with placeholder1:
    st.write("""Step1:ボタンをクリックして座標点をランダムに抽出してみましょう。\n""")

with placeholder2:
    if st.button("座標を5点抽出"):
        st.session_state.x = np.random.randint(0, 100, 5).reshape(-1, 1)
        st.session_state.y = np.random.randint(0, 100, 5).reshape(-1, 1)
        make_graph(st.session_state.x, st.session_state.y)

with placeholder5:
    st.write("Step2:ボタンをクリックして座標点を増やしてみましょう。\n")
with placeholder6:
    if st.button("値を1つ追加"):
        st.session_state.x = np.append(
            st.session_state.x, np.random.randint(0, 100, 1)).reshape(-1, 1)
        st.session_state.y = np.append(
            st.session_state.y, np.random.randint(0, 100, 1)).reshape(-1, 1)
        make_graph(st.session_state.x, st.session_state.y)
