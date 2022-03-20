import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import japanize_matplotlib

st.title('身近な統計 補助教材')
st.header("平均値と中央値の関係")
st.markdown("#")

st.markdown("""
- 乱数から5個の数字を抽出して、平均値と中央値を計算します。
- 小さい値や大きい値を追加して平均値と中央値がどのように変化するか確認してみましょう。
""")

st.markdown("#")


def make_blank_graph():
    fig, ax = plt.subplots()
    ax.set_ylim([0, 100])
    st.pyplot(fig)


def make_graph(num_array):
    mean_array = round(np.mean(st.session_state.num_array_int), 2)
    med_array = np.median(st.session_state.num_array_int)
    with placeholder2:
        st.text('抽出された数字:'+str(st.session_state.num_array_int))
    with placeholder3:
        st.write('平均値：'+str(mean_array)+'　中央値：'+str(med_array))
    # グラフ描画
    with placeholder4:
        x = np.array(range(0, len(st.session_state.num_array_int)))
        y = st.session_state.num_array_int

        med_line = 0*x + med_array
        mean_line = 0*x + mean_array

        fig, ax = plt.subplots()
        ax.scatter(x, y)
        ax.set_ylim([0, 100])
        ax.plot(x, med_line, color="green", label="中央値")
        ax.plot(x, mean_line, color="red", label="平均値")
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
                  borderaxespad=0, fontsize=10)
        st.pyplot(fig)


st.write("Step1:ボタンをクリックして数字をランダムに抽出してみよう！")
placeholder1 = st.empty()
st.markdown("#")
st.markdown("#")
placeholder2 = st.empty()
placeholder3 = st.empty()
placeholder4 = st.empty()
st.markdown("#")
st.markdown("#")
st.write("Step2:小さい値や大きい値を追加してみよう！")
col1, col2 = st.columns(2)

with placeholder1:
    if st.button("5個の数字を抽出"):
        st.session_state.num_array_int = np.random.normal(
            50, 10, 5).astype(int)
        make_graph(st.session_state.num_array_int)

with col1:
    if st.button("1~9の値を追加"):
        st.session_state.num_array_int = np.append(
            st.session_state.num_array_int, np.random.randint(0, 10, 1))
        make_graph(st.session_state.num_array_int)

with col2:
    if st.button("90~100の値を追加"):
        st.session_state.num_array_int = np.append(
            st.session_state.num_array_int, np.random.randint(90, 101, 1))
        make_graph(st.session_state.num_array_int)
