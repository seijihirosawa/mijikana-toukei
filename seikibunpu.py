import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import japanize_matplotlib


st.title('身近な統計 補助教材')
st.header("正規分布")

st.write("""
#### 平均μを入力してください。
""")
m = st.slider('平均μ：', -10.0, 10.0, 0.0)
st.write("""
#### 標準偏差σを入力してください。
""")
s = st.slider('標準偏差σ', 0.0, 10.0, 1.0)

# 確率密度の計算
x = np.arange(-4, 4, 0.01)
y = norm.pdf(x, m, s)


# st.checkbox("上側確率・下側確率を計算する")

if st.checkbox("%点を計算する"):
    st.write("""
    #### 値を入力することで％点を計算することができます。
    """)
    ppu = st.slider("上側%点", 0.0, 100.0, 5.0)
    ppl = st.slider("下側%点", 0.0, 100.0, 5.0)

    # ％点計算
    pu = norm.ppf(1-ppu/100, loc=m, scale=s)
    st.write("上側"+str(ppu)+"%点の値："+str(round(pu, 3)))

    pl = norm.ppf(ppl/100, loc=m, scale=s)
    st.write("下側"+str(ppl)+"%点の値："+str(round(pl, 3)))
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
    ax.fill_between(x, y, Y, where=x < pl)
    st.pyplot(fig)

if st.checkbox("発生確率を計算する"):
    if st.checkbox("上側"):
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
        st.pyplot(fig)
    elif st.checkbox("下側"):
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
        st.pyplot(fig)
