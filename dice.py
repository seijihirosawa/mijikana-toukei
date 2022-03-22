import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import japanize_matplotlib
import random
import seaborn as sns
from PIL import Image

st.title('身近な統計 補助教材')
st.header("2つのサイコロの目の和の確率分布")
st.markdown("#")

st.markdown("""
- 試行回数を選択して、サイコロを振るをクリックしてください。
- 確率変数の和の分布が正規分布に近づくことを確認します。
""")
st.text("")

trials_num_list = [10, 100]

st.text("")
st.write("Step1:2つのサイコロを振る回数を選択します")
trials_num = st.selectbox(
    "試行回数を選択：",
    trials_num_list
)
st.text("")
st.write("Step2:ボタンをクリックして、サイコロの目の和の分布が正規分布に近づくことを確認します。")

if st.button("サイコロを振る"):
    if trials_num == 10 or 100:
        dice_list = []
        placeholder1 = st.empty()
        placeholder2 = st.empty()
        placeholder3 = st.empty()
        placeholder4 = st.empty()

        for i in range(trials_num):
            with placeholder1:
                x1 = np.random.randint(1, 6+1, 1)
                x2 = np.random.randint(1, 6+1, 1)
                if x1 == 1:
                    img = Image.open("image/dice1.png")
                elif x1 == 2:
                    img = Image.open("image/dice2.png")
                elif x1 == 3:
                    img = Image.open("image/dice3.png")
                elif x1 == 4:
                    img = Image.open("image/dice4.png")
                elif x1 == 5:
                    img = Image.open("image/dice5.png")
                elif x1 == 6:
                    img = Image.open("image/dice6.png")
                st.image(img, width=80)
            with placeholder2:
                if x2 == 1:
                    img2 = Image.open("image/dice1.png")
                elif x2 == 2:
                    img2 = Image.open("image/dice2.png")
                elif x2 == 3:
                    img2 = Image.open("image/dice3.png")
                elif x2 == 4:
                    img2 = Image.open("image/dice4.png")
                elif x2 == 5:
                    img2 = Image.open("image/dice5.png")
                elif x2 == 6:
                    img2 = Image.open("image/dice6.png")
                st.image(img2, width=80)

            with placeholder3:
                dice_list.append(np.sum(x1+x2))
                st.write(str(i+1)+'回目  サイコロの目の和：' + str(dice_list))

            with placeholder4:
                fig = plt.figure(figsize=(20, 10))
                ax = sns.distplot(dice_list)
                ax.set_xlabel("サイコロの目の和", fontsize=30)
                ax.set_ylabel("確率", fontsize=30)
                plt.xticks(fontsize=20)
                plt.yticks(fontsize=20)
                st.pyplot(fig)
    # elif:
    #     dice_list = []
    #     for i in range(trials_num):
    #         x1 = np.random.randint(1, 6+1, 1)
    #         x2 = np.random.randint(1, 6+1, 1)
    #         with placeholder3:
    #             dice_list.append(np.sum(x1+x2))
    #             st.write(str(i+1)+'回目  サイコロの目の和：' + str(dice_list))
    # with placeholder4:
    #     fig = plt.figure(figsize=(20, 10))
    #     p = sns.distplot(dice_list)
    #     p.set_xlabel("サイコロの目の和", fontsize=30)
    #     p.set_ylabel("確率", fontsize=30)
    #     plt.xticks(fontsize=20)
    #     plt.yticks(fontsize=20)
    #     st.pyplot(fig)
