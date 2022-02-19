from nbformat import write
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#titleの追加
st.title("Streamlit 入門")
#コマンドの追加
st.write("Display Image")

text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味は",text,"です"

condition = st.slider("あなたの今の調子は？",0,100,50)
"コンディション:",condition

#selectbox
#option = st.selectbox(
#    "あなたの好きな数字を教えてください",
#    list(range(1,11))
#)
#"あなたの好きな数字は、",option,"デス"

#checkbox
#if st.checkbox("Show Image"):
#    img = Image.open("img1.jpg")
#    st.image(img, caption="yukihami", use_column_width = True)

