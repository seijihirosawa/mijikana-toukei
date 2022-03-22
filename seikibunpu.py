import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import japanize_matplotlib


st.title('身近な統計 補助教材')
st.header("正規分布")
st.markdown("#")

st.markdown("""
- 平均値と標準偏差を指定します。
- その分布の上側○％点と下側○％点を表示させてみましょう。
- その分布において、ある値を取る発生確率を表示させてみましょう。
- それぞれの値を変化させて、グラフがどのように変化するか確認してみましょう。
""")

st.markdown("#")
st.write("""
Step1:正規分布の平均μを入力してください。
""")
m = st.slider('平均μ：', -10.0, 10.0, 0.0)
st.markdown("#")
st.write("""
Step2:正規分布の標準偏差σを入力してください。
""")
s = st.slider('標準偏差σ', 0.0, 10.0, 1.0)
st.markdown("#")


# 確率密度の計算
x = np.arange(-4, 4, 0.01)
y = norm.pdf(x, m, s)

st.write("""
Step3:上側・下側%点を計算するか、ある値を取る発生確率を計算するかを選択してください。
""")
if st.checkbox("%点を計算する"):
    st.markdown("#")
    st.write("""
    Step4-1:
    値を入力することでそれぞれの％点を計算することができます。
    上側％以上の値を取る確率密度を青色、下側％以下の確率密度を緑色で表示します。
    """)
    st.markdown("#")
    ppu = st.slider("上側%点", 0.0, 100.0, 5.0)
    st.markdown("#")
    ppl = st.slider("下側%点", 0.0, 100.0, 5.0)
    st.markdown("#")
    st.markdown("#")
    # ％点計算
    pu = norm.ppf(1-ppu/100, loc=m, scale=s)
    st.write("上側"+str(ppu)+"%点の値："+str(round(pu, 3)))

    pl = norm.ppf(ppl/100, loc=m, scale=s)
    st.write("下側"+str(ppl)+"%点の値："+str(round(pl, 3)))
    st.markdown("#")
    st.markdown("#")
    # グラフ描画
    fig, ax = plt.subplots()
    ax.plot(x, y)
    # x 軸のラベルを設定する。
    ax.set_xlabel("確率変数")
    # y 軸のラベルを設定する。
    ax.set_ylabel("確率密度")

    # 正規分布とy=０に囲まれた％点を塗りつぶす
    Y = 0
    ax.fill_between(x, y, Y, where=x > pu)
    ax.fill_between(x, y, Y, where=x < pl, color="green")
    st.pyplot(fig)

st.markdown("#")
if st.checkbox("発生確率を計算する"):
    st.markdown("#")
    st.write("""
    Step4-2:値を入力することでその値を取る確率を計算することができます。
    上側、下側を選択することで、上側％以上の値を取る確率密度、下側％以下の確率密度をそれぞれ青色で表示します。
    """)
    if st.checkbox("上側"):
        st.markdown("#")
        x1 = st.slider("値x", -4.0, 4.0, 0.0)
        p1 = norm.cdf(x=x1, loc=m, scale=s)
        st.write(str(x1)+"は上側"+str(round((1-p1)*100, 2))+"%の値です")
        # グラフ描画
        fig, ax = plt.subplots()
        ax.plot(x, y)
        # x 軸のラベルを設定する。
        ax.set_xlabel("確率変数")
        # y 軸のラベルを設定する。
        ax.set_ylabel("確率密度")

        # 正規分布とy=０に囲まれた％点を塗りつぶす
        Y = 0
        ax.fill_between(x, y, Y, where=x > x1)
        st.markdown("#")
        st.pyplot(fig)
    elif st.checkbox("下側"):
        st.markdown("#")
        x1 = st.slider("値x", -4.0, 4.0, 0.0)
        p1 = norm.cdf(x=x1, loc=m, scale=s)
        st.write(str(x1)+"は下側"+str(round((p1)*100, 2))+"%の値です")
        # グラフ描画
        fig, ax = plt.subplots()
        ax.plot(x, y)
        # x 軸のラベルを設定する。
        ax.set_xlabel("確率変数")
        # y 軸のラベルを設定する。
        ax.set_ylabel("確率密度")

        # 正規分布とy=０に囲まれた％点を塗りつぶす
        Y = 0
        ax.fill_between(x, y, Y, where=x < x1)
        st.markdown("#")
        st.pyplot(fig)
