import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import japanize_matplotlib
import random


st.title('身近な統計 補助教材')
st.header("ヒストグラムと箱ひげ図")
st.markdown("#")

st.markdown("""
- データ数を選択して入力し、ヒストグラムと箱ひげ図を表示してみましょう。
- データ数を変更して、表示してみましょう。
""")
st.markdown("#")


st.write("Step1:ランダムに数値を取得するデータ数を指定します。")

data_num_list = [50, 100, 200, 300]
data_num = st.selectbox(
    "データ数を選択：",
    data_num_list
)
st.markdown("#")
st.write("Step2:取得したデータの散布図を表示します。")
placeholder1 = st.empty()
placeholder_text = st.empty()
placeholder2 = st.empty()

st.markdown("#")
st.markdown("#")
st.write("Step3:取得したデータのヒストグラムを表示します。")
placeholder3 = st.empty()
placeholder4 = st.empty()
st.markdown("#")
st.markdown("#")
st.write("Step4:取得したデータの箱ひげ図を表示します。")
placeholder5 = st.empty()
placeholder6 = st.empty()

with placeholder1:
    if st.button("データを表示"):
        st.session_state.data = np.round(np.random.normal(50, 10, data_num))
        y = np.zeros(data_num)
        st.session_state.fig, st.session_state.ax = plt.subplots()
        st.session_state.ax.scatter(st.session_state.data, y)
        with placeholder_text:
            st.text("抽出された数字："+str(st.session_state.data))
        with placeholder2:
            st.pyplot(st.session_state.fig)

st.markdown("#")


with placeholder3:
    if st.button("ヒストグラムを表示"):
        with placeholder_text:
            st.text("抽出された数字："+str(st.session_state.data))
        with placeholder2:
            st.pyplot(st.session_state.fig)
        with placeholder4:
            st.session_state.fig2, st.session_state.ax2 = plt.subplots()
            st.session_state.ax2.hist(st.session_state.data)
            st.session_state.ax2.set_xlabel("xの値")
            st.session_state.ax2.set_ylabel("度数")
            st.pyplot(st.session_state.fig2)

st.markdown("#")

with placeholder5:
    if st.button("箱ひげ図を表示"):
        with placeholder_text:
            st.text("抽出された数字："+str(st.session_state.data))
        with placeholder2:
            st.pyplot(st.session_state.fig)
        with placeholder4:
            st.pyplot(st.session_state.fig2)
        with placeholder6:
            st.session_state.fig3, st.session_state.ax3 = plt.subplots()
            st.session_state.ax3.boxplot(st.session_state.data, vert=False)
            st.pyplot(st.session_state.fig3)
